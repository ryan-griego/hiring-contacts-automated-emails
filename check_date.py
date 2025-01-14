from datetime import datetime, timedelta
import pytz

def is_date_older_than_3_months(date_string):
    """
    Converts a date string to a datetime object and checks if it is 3 months or older
    from the current date.
    """
    try:
        # Convert the string to a datetime object with timezone
        date_object = datetime.fromisoformat(date_string.replace("Z", "+00:00"))

        # Get the current date 3 months ago in UTC
        three_months_ago = datetime.now(pytz.UTC) - timedelta(days=90)

        # Check if the date is older than 3 months
        if date_object < three_months_ago:
            return True
        return False
    except ValueError as e:
        print(f"Error parsing date string: {e}")
        return False

# Test the function
date_string = "2024-02-01T10:00:00.000Z"
if is_date_older_than_3_months(date_string):
    print(f"The date {date_string} is at least 3 months old.")
else:
    print(f"The date {date_string} is not older than 3 months.")
