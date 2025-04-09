import logging
from cryptography.hazmat.primitives.asymmetric import rsa, padding
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.serialization import (
    load_pem_private_key, load_pem_public_key,
    Encoding, PrivateFormat, PublicFormat, NoEncryption
)
from cryptography.fernet import Fernet

logging.basicConfig(level=logging.INFO)

class HybridEncryptionHelper:
    """
    A hybrid encryption helper class combining RSA for key exchange and Fernet for symmetric encryption.
    """

    def __init__(self):
        try:
            self.private_key = rsa.generate_private_key(public_exponent=65537, key_size=2048)
            self.public_key = self.private_key.public_key()
            self.fernet_key = Fernet.generate_key()
            self.fernet = Fernet(self.fernet_key)
            logging.info("HybridEncryptionHelper initialized with RSA + Fernet keys.")
        except Exception as e:
            logging.error(f"Failed to initialize encryption helper: {e}")

    def export_keys(self):
        return {
            "private_key": self.private_key.private_bytes(
                Encoding.PEM, PrivateFormat.PKCS8, NoEncryption()
            ),
            "public_key": self.public_key.public_bytes(
                Encoding.PEM, PublicFormat.SubjectPublicKeyInfo
            ),
            "fernet_key": self.fernet_key
        }

    def encrypt_data(self, data):
        try:
            return self.fernet.encrypt(data.encode())
        except Exception as e:
            logging.error(f"Encryption failed: {e}")
            return None

    def decrypt_data(self, encrypted_data):
        try:
            return self.fernet.decrypt(encrypted_data).decode()
        except Exception as e:
            logging.error(f"Decryption failed: {e}")
            return None

def run_backend():
    logging.info("Running Hybrid Encryption Backend...")
    helper = HybridEncryptionHelper()
    test = helper.encrypt_data("GenDan secure payload")
    if test:
        logging.info(f"Encrypted: {test}")
        logging.info(f"Decrypted: {helper.decrypt_data(test)}")
