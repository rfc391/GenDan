import os
import logging
from cryptography.fernet import Fernet

logging.basicConfig(level=logging.INFO)

class SecureStorage:
    """Secure storage with Fernet encryption."""

    def __init__(self, storage_path="secure_data", key_file="key.key"):
        self.storage_path = storage_path
        self.key_file = os.path.join(storage_path, key_file)
        os.makedirs(storage_path, exist_ok=True)
        self.key = self._load_or_generate_key()
        self.cipher = Fernet(self.key)

    def _load_or_generate_key(self):
        if os.path.exists(self.key_file):
            with open(self.key_file, 'rb') as kf:
                logging.info("Loaded encryption key from disk.")
                return kf.read()
        else:
            key = Fernet.generate_key()
            with open(self.key_file, 'wb') as kf:
                kf.write(key)
            logging.info("Generated and saved new encryption key.")
            return key

    def save(self, filename, data):
        try:
            encrypted_data = self.cipher.encrypt(data.encode())
            file_path = os.path.join(self.storage_path, filename)
            with open(file_path, 'wb') as file:
                file.write(encrypted_data)
            logging.info(f"Data saved securely at {file_path}")
        except Exception as e:
            logging.error(f"Error saving data: {e}")

    def load(self, filename):
        try:
            file_path = os.path.join(self.storage_path, filename)
            with open(file_path, 'rb') as file:
                encrypted_data = file.read()
            decrypted_data = self.cipher.decrypt(encrypted_data).decode()
            logging.info(f"Data loaded from {file_path}")
            return decrypted_data
        except Exception as e:
            logging.error(f"Error loading data: {e}")
            return None

    def initialize(self):
        logging.info("SecureStorage is initialized and ready.")

# Standalone usage example
if __name__ == '__main__':
    store = SecureStorage()
    store.initialize()
    store.save("example.txt", "This is a secret message.")
    print(store.load("example.txt"))
