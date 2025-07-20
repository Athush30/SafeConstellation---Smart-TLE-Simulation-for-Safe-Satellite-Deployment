import csv
import os

LOG_FILE = "events_log.csv"

def init_logger():
    if not os.path.exists(LOG_FILE):
        with open(LOG_FILE, mode='w', newline='') as f:
            writer = csv.writer(f)
            writer.writerow(["Satellite", "Timestamp", "Event", "TLE Line 1", "TLE Line 2"])

def log_event(name, timestamp, event, tle1="", tle2=""):
    with open(LOG_FILE, mode='a', newline='') as f:
        writer = csv.writer(f)
        writer.writerow([name, timestamp, event, tle1, tle2])
