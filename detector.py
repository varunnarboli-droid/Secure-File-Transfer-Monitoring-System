import os
from config import SENSITIVE_PATHS

def is_sensitive(path):
    path = os.path.abspath(path).lower()

    for sensitive_path in SENSITIVE_PATHS:
        sensitive_path = os.path.abspath(sensitive_path).lower()

        if path.startswith(sensitive_path):
            return True

    return False