import os
import sys
from datetime import datetime, timedelta
import pytz
from pymongo import MongoClient
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail
from jinja2 import Template
from dotenv import load_dotenv

import logging

# Load environment variables from .env file
load_dotenv()

# Configure logging
logging.basicConfig(
    filename='email_send.log',
    level=logging.INFO,
    format='%(asctime)s:%(levelname)s:%(message)s'
)

# Environment variables
MONGODB_URI = os.getenv("MONGODB_URI")
DATABASE_NAME = os.getenv("MONGODB_DATABASE")
COLLECTION_NAME = os.getenv("MONGODB_COLLECTION")
SENDGRID_API_KEY = os.getenv("SENDGRID_API_KEY")
FROM_EMAIL = os.getenv("FROM_EMAIL")
PORTFOLIO_URL = os.getenv("PORTFOLIO_URL")
LINKEDIN_URL = os.getenv("LINKEDIN_URL")
GITHUB_URL = os.getenv("GITHUB_URL")
CALENDLY_URL = os.getenv("CALENDLY_URL")  # Ensure this is set in your .env

def load_html_template(template_name):
    """
    Loads an HTML template from the email_templates folder.
    """
    try:
        templates_dir = os.path.join(os.path.dirname(__file__), "email_templates")
        template_path = os.path.join(templates_dir, template_name)
        with open(template_path, "r", encoding="utf-8") as template_file:
            return template_file.read()
    except Exception as e:
        logging.error(f"Failed to load HTML template: {e}")
        sys.exit(1)

def get_recent_documents(client, limit=5):
    """
    Fetches recent documents with jobType 'test2' and sentFollowUp1 as False.
    Processes documents starting from the lowest jobId.
    """
    db = client[DATABASE_NAME]
    collection = db[COLLECTION_NAME]

    # Define the query
    query = {
        "sentFollowUp1": False,
        "status": "Sent",
        "jobPosterName": {"$exists": True, "$ne": None},
        "jobPosterEmail": {"$exists": True, "$ne": None}
    }

    # Fetch and sort documents by jobId in ascending order
    documents = list(collection.find(query).sort("timestamp", 1).limit(limit))

    # Filter by timestamp
    three_months_ago = datetime.now(pytz.UTC) - timedelta(days=90)
    valid_documents = []

    for doc in documents:
        timestamp = doc.get("timestamp")
        if timestamp:
            try:
                doc_timestamp = datetime.fromisoformat(timestamp.replace("Z", "+00:00"))
                if doc_timestamp <= three_months_ago:
                    valid_documents.append(doc)
            except ValueError:
                print(f"Invalid timestamp format for document: {doc}")

    logging.info(f"Filtered {len(valid_documents)} documents to process.")
    return valid_documents

def send_email(sendgrid_client, from_email, to_email, subject, html_content):
    """
    Sends an email using SendGrid.
    """
    message = Mail(
        from_email=from_email,
        to_emails=to_email,
        subject=subject,
        html_content=html_content
    )
    try:
        response = sendgrid_client.send(message)
        logging.info(f"Email sent to {to_email}: Status Code {response.status_code}")
        logging.debug(f"Response Body: {response.body}")
        logging.debug(f"Response Headers: {response.headers}")
        return True
    except Exception as e:
        logging.error(f"Error sending email to {to_email}: {e}")
        return False

def update_document_sent(client, job_id):
    """
    Updates the document's sentFollowUp1 field to True after sending the email.
    """
    db = client[DATABASE_NAME]
    collection = db[COLLECTION_NAME]
    result = collection.update_one({"jobId": job_id}, {"$set": {"sentFollowUp1": True}})
    if result.modified_count > 0:
        logging.info(f"Document with jobId {job_id} updated successfully.")
    else:
        logging.warning(f"No document found with jobId {job_id} to update.")

def populate_template(document):
    """
    Populates the HTML template with data from the document.
    """
    html_template = load_html_template("email_a_long.html")
    template = Template(html_template)
    # Prepare data for template
    data = {
        "ContactNameOrTitle": document.get("jobPosterName", "Hiring Manager"),
        "JobTitle": document.get("jobTitle", "the position"),
        "CompanyName": document.get("companyName", "your company"),
        "YouTubeVideoURL_Project1": document.get("YouTubeVideoURL_Project1", "https://patient-appointment-booking.ryangriego.com/"),
        "YouTubeThumbnailURL_Project1": document.get("YouTubeThumbnailURL_Project1", "https://res.cloudinary.com/dm7y3yvjp/image/upload/v1736276434/patient-healthcare-booking-app_tbka9n.png"),
        "YouTubeVideoURL_Project2": document.get("YouTubeVideoURL_Project2", "https://chatrrg.ryangriego.com/"),
        "YouTubeThumbnailURL_Project2": document.get("YouTubeThumbnailURL_Project2", "https://res.cloudinary.com/dm7y3yvjp/image/upload/v1741036737/trizify-thumbnail_cuk7lw.png"),
        "PortfolioURL": PORTFOLIO_URL,
        "LinkedInURL": LINKEDIN_URL,
        "GitHubURL": GITHUB_URL,
        "CalendlyURL": CALENDLY_URL,
        "CurrentYear": datetime.now().year
    }
    rendered_html = template.render(data)
    logging.debug(f"Populated HTML template for jobId {document.get('jobId')}.")
    return rendered_html

def main():
    # Initialize SendGrid client
    try:
        sendgrid_client = SendGridAPIClient(SENDGRID_API_KEY)
    except Exception as e:
        logging.critical(f"Failed to initialize SendGrid client: {e}")
        sys.exit(1)

    # Connect to MongoDB
    try:
        client = MongoClient(MONGODB_URI)
        logging.info("Connected to MongoDB.")
    except Exception as e:
        logging.critical(f"Failed to connect to MongoDB: {e}")
        sys.exit(1)

    # Fetch recent documents
    documents = get_recent_documents(client, limit=5)
    if not documents:
        logging.info("No documents found to send emails.")
        client.close()
        sys.exit(0)

    for doc in documents:
        # Retrieve the hiring contact's email from the document
        hiring_contact_email = doc.get("jobPosterEmail")

        # Check if the hiring contact's email exists
        if not hiring_contact_email:
            logging.warning(f"No hiring contact email found for jobId {doc.get('jobId')}. Skipping.")
            continue

        # Ensure hiring_contact_email is a list
        if not isinstance(hiring_contact_email, list):
            hiring_contact_email = [hiring_contact_email]

        logging.info(f"Sending email to: {hiring_contact_email}")

        # Populate HTML template
        html_content = populate_template(doc)

        # Define email subject
        subject = f"Follow-Up on {doc.get('jobTitle')} Application at {doc.get('companyName')}"

        # Send email to jobPosterEmail
        for recipient in hiring_contact_email:
            success = send_email(sendgrid_client, FROM_EMAIL, recipient, subject, html_content)
            if success:
                print(f"SENT EMAIL to {recipient}")
                timestamp = datetime.fromisoformat(doc["timestamp"].replace("Z", "+00:00"))
                print(f"Human-readable timestamp: {timestamp}")
            else:
                print(f"FAILED to send email to {recipient}")
                logging.error(f"Failed to send email to {recipient}. Document not updated.")

        # Send a duplicate email to your email
        duplicate_email = 'ryangriego@gmail.com'
        duplicate_success = send_email(sendgrid_client, FROM_EMAIL, duplicate_email, subject, html_content)
        if duplicate_success:
            print(f"SENT DUPLICATE EMAIL to {duplicate_email}")
        else:
            print(f"FAILED to send duplicate email to {duplicate_email}")
            logging.error(f"Failed to send duplicate email to {duplicate_email}.")

        # Update the document to mark it as processed
        update_document_sent(client, doc.get("jobId"))

    # Close MongoDB connection
    client.close()
    logging.info("MongoDB connection closed.")

if __name__ == "__main__":
    main()
