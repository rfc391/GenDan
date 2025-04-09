
import unittest
from cryptography.fernet import Fernet
from genetic_app_backend import EncryptionHelper

class TestEncryptionHelper(unittest.TestCase):
    def test_encryption_decryption(self):
        key = Fernet.generate_key()
        helper = EncryptionHelper(key)
        
        message = "This is a test message."
        encrypted = helper.encrypt(message)
        decrypted = helper.decrypt(encrypted.decode())
        
        self.assertEqual(message, decrypted)

if __name__ == "__main__":
    unittest.main()
