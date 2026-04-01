from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import time

from detector import is_sensitive
from integrity import calculate_hash
from logger import log_event

# Counter for bulk detection
event_counter = 0


class TestHandler(FileSystemEventHandler):

    def on_moved(self, event):
        global event_counter
        event_counter += 1

        print(f"moved - {event.src_path} -> {event.dest_path}")

        # Sensitive detection
        if is_sensitive(event.src_path):
            print(f"🚨 HIGH ALERT: Sensitive file moved -> {event.src_path}")

        # Hash (destination path)
        file_hash = calculate_hash(event.dest_path)

        # Logging (FIXED arrow)
        log_event("MOVED", f"{event.src_path} -> {event.dest_path} | HASH: {file_hash}")

        # Bulk detection
        if event_counter > 10:
            print("⚠️ WARNING: Multiple file operations detected (possible exfiltration)")


    def on_any_event(self, event):
        if event.event_type == "moved":
            return

        global event_counter
        event_counter += 1

        print(f"{event.event_type} - {event.src_path}")

        # Sensitive detection
        if is_sensitive(event.src_path):
            print(f"🚨 HIGH ALERT: Sensitive file activity -> {event.src_path}")

        # Hash
        file_hash = calculate_hash(event.src_path)

        # Logging
        log_event(event.event_type, event.src_path + f" | HASH: {file_hash}")

        # Bulk detection
        if event_counter > 10:
            print("⚠️ WARNING: Multiple file operations detected (possible exfiltration)")


def start_monitor(path):
    observer = Observer()
    handler = TestHandler()
    observer.schedule(handler, path, recursive=True)
    observer.start()

    print("Monitoring started...")

    try:
        while True:
            time.sleep(2)
    except KeyboardInterrupt:
        observer.stop()

    observer.join()