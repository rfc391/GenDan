
import os
from cryptography.fernet import Fernet

class SecureStorage:
    """A class to securely store and retrieve sensitive data."""

    def __init__(self, storage_path, encryption_key=None):
        self.storage_path = storage_path
        os.makedirs(storage_path, exist_ok=True)
        self.key = encryption_key or Fernet.generate_key()
        self.cipher = Fernet(self.key)

    def save(self, filename, data):
        """Encrypt and save data to a file."""
        encrypted_data = self.cipher.encrypt(data.encode())
        file_path = os.path.join(self.storage_path, filename)
        with open(file_path, 'wb') as file:
            file.write(encrypted_data)
        return file_path

    def load(self, filename):
        """Decrypt and load data from a file."""
        file_path = os.path.join(self.storage_path, filename)
        if not os.path.exists(file_path):
            raise FileNotFoundError(f"File not found: {file_path}")
        with open(file_path, 'rb') as file:
            encrypted_data = file.read()
        return self.cipher.decrypt(encrypted_data).decode()

# Example usage:
# storage = SecureStorage(storage_path="./secure_data")
# storage.save("example.txt", "This is sensitive data.")
# print(storage.load("example.txt"))
