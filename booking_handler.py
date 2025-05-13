import csv
from datetime import datetime
import os

def validate_and_save(name, contact, date, event_type, notes):
    if not name or not contact or not date or not event_type:
        return False, "All fields except notes are required."
    try:
        event_date = datetime.strptime(date, "%Y-%m-%d")
        if event_date < datetime.now():
            return False, "Event date must be in the future."
    except ValueError:
        return False, "Invalid date format. Use YYYY-MM-DD."

    file_exists = os.path.isfile("booking.csv")
    with open("booking.csv", "a", newline="") as csvfile:
        writer = csv.writer(csvfile)
        if not file_exists:
            writer.writerow(["Name", "Contact", "Date", "EventType", "Notes", "Timestamp"])
        writer.writerow([name, contact, date, event_type, notes.strip(), datetime.now().strftime("%Y-%m-%d %H:%M:%S")])

    return True, "Saved"
