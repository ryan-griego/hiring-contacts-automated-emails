import os
import sys
import logging
from pymongo import MongoClient
from datetime import datetime
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s:%(levelname)s:%(message)s',
    handlers=[
        logging.FileHandler("email_send.log"),  # Log to a file
        logging.StreamHandler(sys.stdout)  # Log to the terminal
    ]
)

# Environment variables
MONGODB_URI = os.getenv("MONGODB_URI")
DATABASE_NAME = os.getenv("MONGODB_DATABASE")
COLLECTION_NAME = os.getenv("MONGODB_COLLECTION")

def get_recent_documents(client, limit=12):
    """
    Fetches the next 12 documents with status 'Sent' and sentFollowUp1 as False.
    """
    db = client[DATABASE_NAME]
    collection = db[COLLECTION_NAME]

    # Query for documents that haven't been sent yet
    query = {
        "sentFollowUp1": False,
        "status": "Sent",
        "jobPosterName": {"$exists": True, "$ne": None, "$ne": ""},
        "jobPosterEmail": {"$exists": True, "$ne": None, "$ne": ""},
        # Checks if outcome is None or empty string - helps me see what are the next jobs to get outcomes for
        "outcome": {"$in": [None, ""]}
    }

    # Fetch documents sorted by timestamp in ascending order (next to be sent)
    documents = list(collection.find(query).sort("timestamp", 1).limit(limit))

    logging.info(f"Fetched {len(documents)} documents.")
    return documents

def main():
    # Connect to MongoDB
    try:
        client = MongoClient(MONGODB_URI)
        logging.info("Connected to MongoDB.")
    except Exception as e:
        logging.critical(f"Failed to connect to MongoDB: {e}")
        sys.exit(1)

    # Fetch recent documents (next 12)
    documents = get_recent_documents(client, limit=12)
    if not documents:
        logging.info("No documents found.")
        client.close()
        sys.exit(0)

    # Print the next 12 documents that would be selected
    for doc in documents:
        job_id = doc.get("jobId")
        job_title = doc.get("jobTitle")
        company_name = doc.get("companyName")
        email_to_send = doc.get("jobPosterEmail")
        timestamp = doc.get("timestamp")
        companyOfficialUrl = doc.get("companyOfficialUrl")
        print(f"Document {job_id}: {companyOfficialUrl} -> {job_title} at {company_name}will be sent to {email_to_send}. Timestamp: {timestamp}")
        #print(f"Document {job_id}: {job_title} at {company_name} will be sent to {email_to_send}. Timestamp: {timestamp}")

    # Close MongoDB connection
    client.close()
    logging.info("MongoDB connection closed.")

if __name__ == "__main__":
    main()
