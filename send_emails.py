# import os
# import sys
# import time
# from datetime import datetime
# from dotenv import load_dotenv
# from pymongo import MongoClient
# from sendgrid import SendGridAPIClient
# from sendgrid.helpers.mail import Mail
# from jinja2 import Template
# import logging

# # Load environment variables from .env file
# load_dotenv()

# # Configure logging
# logging.basicConfig(
#     filename='email_send.log',
#     level=logging.INFO,
#     format='%(asctime)s:%(levelname)s:%(message)s'
# )

# # Environment variables
# MONGODB_URI = os.getenv("MONGODB_URI")
# DATABASE_NAME = os.getenv("MONGODB_DATABASE")
# COLLECTION_NAME = os.getenv("MONGODB_COLLECTION")
# SENDGRID_API_KEY = os.getenv("SENDGRID_API_KEY")
# FROM_EMAIL = os.getenv("FROM_EMAIL")
# PORTFOLIO_URL = os.getenv("PORTFOLIO_URL")
# LINKEDIN_URL = os.getenv("LINKEDIN_URL")
# GITHUB_URL = os.getenv("GITHUB_URL")
# CALENDLY_URL = os.getenv("CALENDLY_URL")  # Ensure this is set in your .env

# # HTML Template
# HTML_TEMPLATE = """
# <!DOCTYPE HTML
#   PUBLIC "-//W3C//DTD XHTML 1.0 Transitional //EN"
#   "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
# <html xmlns="http://www.w3.org/1999/xhtml"
#       xmlns:v="urn:schemas-microsoft-com:vml"
#       xmlns:o="urn:schemas-microsoft-com:office:office">

# <head>
#   <!--[if gte mso 9]>
#   <xml>
#     <o:OfficeDocumentSettings>
#       <o:AllowPNG/>
#       <o:PixelsPerInch>96</o:PixelsPerInch>
#     </o:OfficeDocumentSettings>
#   </xml>
#   <![endif]-->
#   <meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
#   <meta name="viewport" content="width=device-width, initial-scale=1.0">
#   <meta name="x-apple-disable-message-reformatting">
#   <!--[if !mso]><!-->
#   <meta http-equiv="X-UA-Compatible" content="IE=edge"><!--<![endif]-->
#   <title>Outreach Email</title>

#   <style type="text/css">
#     body {
#       margin: 0;
#       padding: 0;
#       background-color: #f0f0f5;
#       -webkit-text-size-adjust: 100%;
#       color: #000000;
#       font-family: 'Lato', sans-serif;
#     }

#     table, tr, td {
#       vertical-align: top;
#       border-collapse: collapse;
#     }

#     p {
#       margin: 0;
#       padding:0;
#     }

#     a {
#       color: #0000ee;
#       text-decoration: underline;
#     }

#     h1, h2, h3, h4 {
#       margin:0;
#       font-weight: normal;
#     }

#     .v-text-align {
#       text-align: center !important;
#     }

#     /* Responsive Styles */
#     @media only screen and (max-width: 620px) {
#       .u-row .u-col {
#         display: block !important;
#         width: 100% !important;
#       }
#       .hide-mobile {
#         display: none !important;
#       }
#     }

#     .brand-gradient {
#       background: linear-gradient(to right, #0f3159, #1a9ba2);
#     }

#     .heading-text {
#       font-family: 'Oswald', sans-serif;
#       letter-spacing: 0.5px;
#       color:#ffffff;
#     }

#     .divider {
#       width:60px;
#       height:4px;
#       background:#ffffff;
#       margin:20px auto 0 auto;
#       border-radius:2px;
#     }

#     .skills-icon {
#       width:40px;
#       display:block;
#       margin:0 auto 5px;
#     }

#     .skills-title {
#       font-size:14px;
#       color:#000;
#       text-align:center;
#       font-weight:bold;
#       letter-spacing:0.5px;
#       margin-top: 5px;
#     }

#     .contact-links a {
#       color: #ffffff;
#       font-size:16px;
#       font-weight:700;
#       text-decoration:none;
#       margin:0 5px;
#     }

#     .contact-links a:hover {
#       text-decoration:underline;
#     }

#     .highlight {
#       color: #1a9ba2;
#       font-weight:700;
#     }

#     .cta-button {
#       display:inline-block;
#       background: #1a9ba2;
#       color:#ffffff;
#       text-decoration:none;
#       padding:10px 20px;
#       border-radius:4px;
#       font-weight:700;
#       margin-top:20px;
#     }

#     .cta-button:hover {
#       background:#147f86;
#     }

#     .project-img {
#       border-radius:8px;
#       max-width:100%;
#       height:auto;
#     }

#     h2.project-header {
#       font-family:'Oswald',sans-serif;font-size:24px;text-align:center;margin-bottom:15px;color:#ffffff;
#     }

#     .project-section-text {
#       color:#ffffff;font-size:14px;line-height:1.6;margin-top:15px;text-align:center;
#     }
#   </style>

#   <!--[if !mso]><!-->
#   <link href="https://fonts.googleapis.com/css?family=Lato:400,700" rel="stylesheet" type="text/css">
#   <link href="https://fonts.googleapis.com/css2?family=Epilogue:wght@500&display=swap" rel="stylesheet" type="text/css">
#   <link href="https://fonts.googleapis.com/css?family=Open+Sans:400,700" rel="stylesheet" type="text/css">
#   <link href="https://fonts.googleapis.com/css2?family=Oswald:wght@300;700&display=swap" rel="stylesheet" type="text/css">
#   <!--<![endif]-->
# </head>

# <body class="clean-body u_body" style="margin:0;padding:0;background-color:#f0f0f5;color:#000000;">

#   <table width="100%" cellpadding="0" cellspacing="0" style="background-color:#f0f0f5;">
#     <tr>
#       <td>

#         <!-- Header / Hero Section -->
#         <div style="margin:0 auto;max-width:600px;background:#ffffff;">
#           <table width="100%" cellpadding="0" cellspacing="0">
#             <tr>
#               <td align="center" style="background:#1a9ba2;padding:30px;">
#                 <h1 class="heading-text" style="font-size:34px; line-height:1.4;">
#                   Ryan Griego
#                 </h1>
#                 <p style="font-size:14px;color:#ebf9f9;margin-top:10px;letter-spacing:0.5px;">
#                   Software Developer
#                 </p>
#                 <div class="divider"></div>
#               </td>
#             </tr>
#             <tr>
#               <td style="padding:20px;text-align:center;background:#0f3159;">
#                 <div class="contact-links" style="margin-bottom:10px;">
#                   <a href="{{PortfolioURL}}" target="_blank">Portfolio</a>
#                   <span class="hide-mobile" style="color:#ffffff;">|</span>
#                   <a href="{{LinkedInURL}}" target="_blank">LinkedIn</a>
#                   <span class="hide-mobile" style="color:#ffffff;">|</span>
#                   <a href="{{GitHubURL}}" target="_blank">GitHub</a>
#                 </div>
#                 <table align="center" cellpadding="0" cellspacing="0">
#                   <tr>
#                     <td align="center" style="border-top:1px solid #5ac1a9;padding:10px 0 0;">
#                       <p style="color:#ffffff;font-size:14px;margin-top:10px;line-height:1.6;">
#                         Phone: (949) 310-8534 | Email: <a href="mailto:ryangriego@gmail.com" style="color:#ffffff;text-decoration:underline;">ryangriego@gmail.com</a>
#                       </p>
#                     </td>
#                   </tr>
#                 </table>
#               </td>
#             </tr>
#           </table>
#         </div>

#         <!-- Greeting Section -->
#         <div style="margin:20px auto;max-width:600px;background:#ffffff;border-radius:6px;overflow:hidden;">
#           <table width="100%" cellpadding="0" cellspacing="0">
#             <tr>
#               <td style="padding:30px 20px;font-family:'Open Sans',sans-serif;font-size:16px;line-height:1.6;color:#000;">
#                 <p>Hello {{ContactNameOrTitle}},</p>
#                 <p>Last year, I applied for the {{JobTitle}} position at {{CompanyName}}. I’m reaching out to see if there may be any current or upcoming opportunities within {{CompanyName}} that align with my experience as a Software Developer.</p>
#                 <br>
#                 <p>I’ve admired the innovative projects at your company and I’d love the chance to contribute my skills and creativity. Below, you’ll find two of my recent side projects, both featuring short demos that highlight what I bring to the table.</p>
#               </td>
#             </tr>
#           </table>
#         </div>

#         <!-- Project #1 Section -->
#         <div style="margin:20px auto;max-width:600px;background:#ffffff;border-radius:6px;overflow:hidden;">
#           <table width="100%" cellpadding="0" cellspacing="0">
#             <tr>
#               <td style="background:#0f3159;padding:20px;" valign="top" width="60%">
#                 <h2 class="project-header">Project #1</h2>
#                 <div style="text-align:center;">
#                   <a href="{{YouTubeVideoURL_Project1}}" target="_blank" style="text-decoration:none;">
#                     <img src="{{YouTubeThumbnailURL_Project1}}" alt="Watch Project #1 Demo" class="project-img"/>
#                   </a>
#                   <p style="color:#ffffff;font-size:14px;margin-top:10px;">Click above to watch a quick demo</p>
#                 </div>
#                 <p class="project-section-text">
#                   This project demonstrates my ability to integrate APIs, handle data visualization, and craft intuitive user interfaces.
#                 </p>
#               </td>
#               <td style="background:#1a9ba2;padding:20px;vertical-align:middle;" width="40%">
#                 <h2 style="color:#ffffff;font-family:'Oswald',sans-serif;font-size:18px;line-height:1.4;margin:0;text-align:center;">
#                   My Approach
#                 </h2>
#                 <p style="color:#ffffff;font-size:14px;line-height:1.6;margin-top:10px;text-align:center;">
#                   I focus on writing clean, maintainable code, ensuring that each project I develop is scalable, responsive, and user-friendly.
#                 </p>
#               </td>
#             </tr>
#           </table>
#         </div>

#         <!-- Project #2 Section (Matching Layout) -->
#         <div style="margin:20px auto;max-width:600px;background:#ffffff;border-radius:6px;overflow:hidden;">
#           <table width="100%" cellpadding="0" cellspacing="0">
#             <tr>
#               <!-- Swap the colors for a similar but distinct look -->
#               <td style="background:#1a9ba2;padding:20px;" valign="top" width="60%">
#                 <h2 class="project-header">Project #2</h2>
#                 <div style="text-align:center;">
#                   <a href="{{YouTubeVideoURL_Project2}}" target="_blank" style="text-decoration:none;">
#                     <img src="{{YouTubeThumbnailURL_Project2}}" alt="Watch Project #2 Demo" class="project-img"/>
#                   </a>
#                   <p style="color:#ffffff;font-size:14px;margin-top:10px;">Click above to watch a quick demo</p>
#                 </div>
#                 <p class="project-section-text">
#                   This e-commerce prototype features live product data, custom checkout flows, and responsive design..
#                 </p>
#               </td>
#               <td style="background:#0f3159;padding:20px;vertical-align:middle;" width="40%">
#                 <h2 style="color:#ffffff;font-family:'Oswald',sans-serif;font-size:18px;line-height:1.4;margin:0;text-align:center;">
#                   Key Strengths
#                 </h2>
#                 <p style="color:#ffffff;font-size:14px;line-height:1.6;margin-top:10px;text-align:center;">
#                   Experienced in modern frameworks, I adapt quickly to new technologies and workflows.
#                 </p>
#               </td>
#             </tr>
#           </table>
#         </div>

#         <!-- Skills Section -->
#         <div style="margin:20px auto;max-width:600px;background:#ffffff;border-radius:6px;overflow:hidden;">
#           <table width="100%" cellpadding="0" cellspacing="0">
#             <tr>
#               <td style="padding:20px;text-align:center;">
#                 <h2 style="font-family:'Oswald',sans-serif;font-size:24px;color:#0f3159;">Core Skills</h2>
#                 <p style="color:#000;font-size:14px;line-height:1.6;margin-top:10px;">
#                   I excel with modern JavaScript frameworks, and have experience across the full stack:
#                 </p>
#               </td>
#             </tr>
#             <tr>
#               <td style="padding:20px;">
#                 <table width="100%" cellpadding="0" cellspacing="0">
#                   <tr>
#                     <td align="center" width="33.3%" style="padding:10px;">
#                       <img src="https://res.cloudinary.com/dm7y3yvjp/image/upload/v1712253454/next-js-icon_bmql3q.png" class="skills-icon" alt="Next.js"/>
#                       <div class="skills-title">Next.js</div>
#                     </td>
#                     <td align="center" width="33.3%" style="padding:10px;">
#                       <img src="https://res.cloudinary.com/dm7y3yvjp/image/upload/v1626231480/portfolio/icons/javascript_ifuclz.png" class="skills-icon" alt="JavaScript"/>
#                       <div class="skills-title">JavaScript</div>
#                     </td>
#                     <td align="center" width="33.3%" style="padding:10px;">
#                       <img src="https://res.cloudinary.com/dm7y3yvjp/image/upload/v1626231952/portfolio/icons/vue_fq4345.png" class="skills-icon" alt="Vue"/>
#                       <div class="skills-title">Vue</div>
#                     </td>
#                   </tr>
#                   <tr>
#                     <td align="center" width="33.3%" style="padding:10px;">
#                       <img src="https://res.cloudinary.com/dm7y3yvjp/image/upload/v1712253652/nuxt-js-icon_wxwrc2.png" class="skills-icon" alt="Nuxt.js"/>
#                       <div class="skills-title">Nuxt.js</div>
#                     </td>
#                     <td align="center" width="33.3%" style="padding:10px;">
#                       <img src="https://res.cloudinary.com/dm7y3yvjp/image/upload/v1626231480/portfolio/icons/react_yz6djo.png" class="skills-icon" alt="React"/>
#                       <div class="skills-title">React</div>
#                     </td>
#                     <td align="center" width="33.3%" style="padding:10px;">
#                       <img src="https://res.cloudinary.com/dm7y3yvjp/image/upload/v1710817780/php-logo_yrgo45.png" class="skills-icon" alt="PHP"/>
#                       <div class="skills-title">PHP</div>
#                     </td>
#                   </tr>
#                                     <tr>
#                     <td align="center" width="33.3%" style="padding:10px;">
#                       <img src="https://res.cloudinary.com/dm7y3yvjp/image/upload/v1734466160/node.js_iyy3w3.png" class="skills-icon" alt="Node.js"/>
#                       <div class="skills-title">Node.js</div>
#                     </td>
#                     <td align="center" width="33.3%" style="padding:10px;">
#                       <img src="https://res.cloudinary.com/dm7y3yvjp/image/upload/v1734466160/tailwind_pbl1nz.png" class="skills-icon" alt="Tailwind CSS"/>
#                       <div class="skills-title">Tailwind CSS</div>
#                     </td>
#                     <td align="center" width="33.3%" style="padding:10px;">
#                       <img src="https://res.cloudinary.com/dm7y3yvjp/image/upload/v1734466160/typescript_iuyq3e.png" class="skills-icon" alt="TypeScript"/>
#                       <div class="skills-title">TypeScript</div>
#                     </td>
#                   </tr>
#                 </table>
#               </td>
#             </tr>
#           </table>
#         </div>

#         <!-- CTA Section -->
#         <div style="margin:20px auto;max-width:600px;background:#ffffff;border-radius:6px;overflow:hidden;">
#           <table width="100%" cellpadding="0" cellspacing="0">
#             <tr>
#               <td style="padding:30px 20px;font-family:'Open Sans',sans-serif;font-size:16px;line-height:1.6;color:#000;text-align:center;">
#                 <p>If you’d like to discuss how I can bring value to {{CompanyName}},<br> please feel free to:</p>
#                 <a href="{{CalendlyURL}}" target="_blank" class="cta-button">Schedule a Call</a>
#                 <p style="margin-top:20px;">
#                   You can also reply directly to this email if that’s easier for you. I appreciate your time and consideration, and I look forward to the possibility of working together!
#                 </p>
#                 <p style="margin-top:20px;">Warm regards,<br>Ryan Griego</p>
#               </td>
#             </tr>
#             <tr>
#               <td style="background:#f0f0f5;padding:10px;text-align:center;color:#888888;font-size:12px;">
#                 &copy; {{CurrentYear}} Ryan Griego. All Rights Reserved.
#               </td>
#             </tr>
#           </table>
#         </div>

#       </td>
#     </tr>
#   </table>
# </body>
# </html>
# """

# def get_recent_documents(client, limit=3):
#     """
#     Fetches recent documents with jobType 'test' and sentFollowUp1 as False.
#     """
#     db = client[DATABASE_NAME]
#     collection = db[COLLECTION_NAME]
#     query = {"jobType": "test2", "sentFollowUp1": False}
#     documents = list(collection.find(query).limit(limit))
#     logging.info(f"Fetched {len(documents)} documents to send emails.")
#     return documents

# def send_email(sendgrid_client, from_email, to_email, subject, html_content):
#     """
#     Sends an email using SendGrid.
#     """
#     message = Mail(
#         from_email=from_email,
#         to_emails=to_email,
#         subject=subject,
#         html_content=html_content
#     )
#     try:
#         response = sendgrid_client.send(message)
#         logging.info(f"Email sent to {to_email}: Status Code {response.status_code}")
#         logging.debug(f"Response Body: {response.body}")
#         logging.debug(f"Response Headers: {response.headers}")
#         return True
#     except Exception as e:
#         logging.error(f"Error sending email to {to_email}: {e}")
#         return False

# def update_document_sent(client, job_id):
#     """
#     Updates the document's sentFollowUp1 field to True after sending the email.
#     """
#     db = client[DATABASE_NAME]
#     collection = db[COLLECTION_NAME]
#     result = collection.update_one({"jobId": job_id}, {"$set": {"sentFollowUp1": True}})
#     if result.modified_count > 0:
#         logging.info(f"Document with jobId {job_id} updated successfully.")
#     else:
#         logging.warning(f"No document found with jobId {job_id} to update.")

# def populate_template(document):
#     """
#     Populates the HTML template with data from the document.
#     """

#     full_name = document.get("jobPosterName", "Hiring Manager")
#     first_name = full_name.split()[0] if full_name else "Hiring Manager"
#     template = Template(HTML_TEMPLATE)
#     # Prepare data for template
#     data = {
#         "ContactNameOrTitle": first_name,
#         "JobTitle": document.get("jobTitle", "the position"),
#         "CompanyName": document.get("companyName", "your company"),
#         "YouTubeVideoURL_Project1": document.get("YouTubeVideoURL_Project1", "https://www.youtube.com/watch?v=your_video_id1"),  # Replace or fetch from document
#         "YouTubeThumbnailURL_Project1": document.get("YouTubeThumbnailURL_Project1", "https://img.youtube.com/vi/your_video_id1/0.jpg"),  # Replace or fetch from document
#         "YouTubeVideoURL_Project2": document.get("YouTubeVideoURL_Project2", "https://www.youtube.com/watch?v=your_video_id2"),  # Replace or fetch from document
#         "YouTubeThumbnailURL_Project2": document.get("YouTubeThumbnailURL_Project2", "https://img.youtube.com/vi/your_video_id2/0.jpg"),  # Replace or fetch from document
#         "PortfolioURL": PORTFOLIO_URL,
#         "LinkedInURL": LINKEDIN_URL,
#         "GitHubURL": GITHUB_URL,
#         "CalendlyURL": CALENDLY_URL,  # Ensure this is set in your .env
#         "CurrentYear": datetime.now().year
#     }
#     rendered_html = template.render(data)
#     logging.debug(f"Populated HTML template for jobId {document.get('jobId')}.")
#     return rendered_html

# def main():
#     # Initialize SendGrid client
#     try:
#         sendgrid_client = SendGridAPIClient(SENDGRID_API_KEY)
#     except Exception as e:
#         logging.critical(f"Failed to initialize SendGrid client: {e}")
#         sys.exit(1)

#     # Connect to MongoDB
#     try:
#         client = MongoClient(MONGODB_URI)
#         logging.info("Connected to MongoDB.")
#     except Exception as e:
#         logging.critical(f"Failed to connect to MongoDB: {e}")
#         sys.exit(1)

#     # Fetch recent documents
#     documents = get_recent_documents(client, limit=3)
#     if not documents:
#         logging.info("No documents found to send emails.")
#         client.close()
#         sys.exit(0)

#     for doc in documents:
#         # to_email = doc.get("jobPosterEmail", [])
#         to_email = ['ryangriego@gmail.com']

#         if not to_email:
#             logging.warning(f"No email found for jobId {doc.get('jobId')}. Skipping.")
#             continue
#         to_email = to_email[0]  # Assuming single email per document
#         print(to_email)
#         # Populate HTML template
#         html_content = populate_template(doc)

#         # Define email subject
#         subject = f"Follow-Up on {doc.get('jobTitle')} Application at {doc.get('companyName')}"

#         # Send email
#         success = send_email(sendgrid_client, FROM_EMAIL, to_email, subject, html_content)
#         if success:
#             # Update MongoDB document
#             update_document_sent(client, doc.get("jobId"))
#         else:
#             logging.error(f"Failed to send email to {to_email}. Document not updated.")

#         # Removed the 5-minute delay

#     # Close MongoDB connection
#     client.close()
#     logging.info("MongoDB connection closed.")

# if __name__ == "__main__":
#     main()


import os
import sys
from datetime import datetime
from dotenv import load_dotenv
from pymongo import MongoClient
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail
from jinja2 import Template
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

def get_recent_documents(client, limit=3):
    """
    Fetches recent documents with jobType 'test' and sentFollowUp1 as False.
    """
    db = client[DATABASE_NAME]
    collection = db[COLLECTION_NAME]
    query = {"jobType": "test2", "sentFollowUp1": False}
    documents = list(collection.find(query).limit(limit))
    logging.info(f"Fetched {len(documents)} documents to send emails.")
    return documents

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
    print(html_template)
    template = Template(html_template)
    # Prepare data for template
    data = {
        "ContactNameOrTitle": document.get("jobPosterName", "Hiring Manager"),
        "JobTitle": document.get("jobTitle", "the position"),
        "CompanyName": document.get("companyName", "your company"),
        "YouTubeVideoURL_Project1": document.get("YouTubeVideoURL_Project1", "https://www.youtube.com/watch?v=your_video_id1"),
        "YouTubeThumbnailURL_Project1": document.get("YouTubeThumbnailURL_Project1", "https://img.youtube.com/vi/your_video_id1/0.jpg"),
        "YouTubeVideoURL_Project2": document.get("YouTubeVideoURL_Project2", "https://www.youtube.com/watch?v=your_video_id2"),
        "YouTubeThumbnailURL_Project2": document.get("YouTubeThumbnailURL_Project2", "https://img.youtube.com/vi/your_video_id2/0.jpg"),
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
    documents = get_recent_documents(client, limit=3)
    if not documents:
        logging.info("No documents found to send emails.")
        client.close()
        sys.exit(0)

    for doc in documents:
        #to_email = doc.get("jobPosterEmail", ["ryangriego@gmail.com"])[0]
        to_email = ['ryangriego@gmail.com']
        print(to_email)

        if not to_email:
            logging.warning(f"No email found for jobId {doc.get('jobId')}. Skipping.")
            continue

        # Populate HTML template
        html_content = populate_template(doc)

        # Define email subject
        subject = f"Follow-Up on {doc.get('jobTitle')} Application at {doc.get('companyName')}"

        # Send email
        success = send_email(sendgrid_client, FROM_EMAIL, to_email, subject, html_content)
        if success:
            # Update MongoDB document
            update_document_sent(client, doc.get("jobId"))
        else:
            logging.error(f"Failed to send email to {to_email}. Document not updated.")

    # Close MongoDB connection
    client.close()
    logging.info("MongoDB connection closed.")

if __name__ == "__main__":
    main()
