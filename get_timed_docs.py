import os
from datetime import datetime, timedelta
from pymongo import MongoClient
from dotenv import load_dotenv
import pytz

# Load environment variables
load_dotenv()

MONGODB_URI = os.getenv("MONGODB_URI")
DATABASE_NAME = os.getenv("MONGODB_DATABASE")
COLLECTION_NAME = os.getenv("MONGODB_COLLECTION")

def get_recent_documents(client, limit=30):
    db = client[DATABASE_NAME]
    collection = db[COLLECTION_NAME]

    # Calculate the threshold date (3 months ago) in UTC
    three_months_ago = datetime.now(pytz.UTC) - timedelta(days=90)
    print(f"Three months ago (UTC): {three_months_ago}")

    # Fetch documents without filtering by timestamp
    raw_documents = list(collection.find({}).limit(limit))

    # Manually filter documents in Python
    valid_documents = []
    for doc in raw_documents:
        timestamp = doc.get("timestamp")
        if timestamp:
            try:
                # Convert the timestamp string or MongoDB ISODate to a datetime object
                if isinstance(timestamp, str):
                    timestamp_dt = datetime.fromisoformat(timestamp.replace("Z", "+00:00"))
                else:
                    timestamp_dt = timestamp  # Assume it's already a datetime object

                # Compare the timestamp
                if timestamp_dt > three_months_ago:
                    valid_documents.append(doc)
            except ValueError:
                print(f"Invalid timestamp format for document: {doc['_id']}")

    # Print results
    print(f"Found {len(valid_documents)} documents:")
    for i, doc in enumerate(valid_documents, start=1):
        human_readable_ts = timestamp_dt.strftime('%Y-%m-%d %H:%M:%S')
        print(f"Document {i}: {doc}")
        print(f"Readable Timestamp: {human_readable_ts}")

    return valid_documents

def main():
    try:
        client = MongoClient(MONGODB_URI)
        print("✅ Connected to MongoDB.")
        get_recent_documents(client)
    except Exception as e:
        print(f"❌ Error: {e}")
    finally:
        client.close()
        print("🔒 MongoDB connection closed.")

if __name__ == "__main__":
    main()
