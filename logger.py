import psutil
import getpass
from datetime import datetime
from config import LOG_FILE

def get_process_name():
    try:
        return psutil.Process().name()
    except:
        return "Unknown"

def get_user():
    try:
        return getpass.getuser()
    except:
        return "Unknown"

def log_event(event, path):
    user = get_user()
    process = get_process_name()

    log_entry = f"""
[{datetime.now()}]
EVENT: {event}
PATH: {path}
USER: {user}
PROCESS: {process}
----------------------------------
"""

    # ✅ FIX: UTF-8 encoding
    with open(LOG_FILE, "a", encoding="utf-8") as f:
        f.write(log_entry)