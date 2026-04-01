import hashlib

def calculate_hash(file_path):
    try:
        with open(file_path, "rb") as f:
            sha256 = hashlib.sha256()
            while chunk := f.read(8192):
                sha256.update(chunk)
        return sha256.hexdigest()
    except:
        return None