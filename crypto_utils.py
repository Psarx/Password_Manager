import os
import hashlib
import base64

def hash_master_password(password: str) -> str:
    """Hash the master password with a random salt and return salt+hash."""
    salt = os.urandom(16)
    key = hashlib.pbkdf2_hmac(
        'sha256', #hash algorithm
        password.encode('utf-8'), #convert pass to bytes
        salt,
        100_000 #iterations
    )
    
    return base64.b64encode(salt+key).decode('utf-8')

def verify_master_password(stored_hash : str , password_attempt : str) -> bool:
    decoded = base64.b64decode(stored_hash.encode('utf-8'))
    salt = decoded[:16]
    original_key = decoded[16:]
    attempt_key = hashlib.pbkdf2_hmac(
        'sha256',
        password_attempt.encode('utf-8'),
        salt,
        100_000,
    )
    return attempt_key == original_key
