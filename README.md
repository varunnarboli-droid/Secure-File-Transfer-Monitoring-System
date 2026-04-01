# Secure File Transfer Monitoring System

##  Overview
This project monitors file system activities and detects unauthorized file transfers, ensuring data integrity using SHA256 hashing.

##  Features
- File activity monitoring (create, delete, move)
- Sensitive file detection
- SHA256 integrity checks
- Real-time alerts
- Bulk file transfer detection
- Logging and reporting

##  Technologies
- Python
- watchdog
- hashlib
- psutil

##  Project Structure
   SecureFileMonitor/
├── main.py
├── monitor.py
├── detector.py
├── integrity.py
├── logger.py
├── report.py
├── config.py

##  How to Run

```bash
pip install watchdog psutil
python main.py
