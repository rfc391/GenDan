
from cryptography.fernet import Fernet
from genetic_app_backend import EncryptionHelper

def main():
    # Generate a key for encryption
    key = Fernet.generate_key()
    print(f"Generated Key: {key.decode()}")

    # Initialize the EncryptionHelper with the key
    helper = EncryptionHelper(key)

    # Sample message for encryption and decryption
    message = "This is a test message."
    print(f"Original Message: {message}")

    # Encrypt the message
    encrypted_message = helper.encrypt(message)
    print(f"Encrypted Message: {encrypted_message.decode()}")

    # Decrypt the message
    decrypted_message = helper.decrypt(encrypted_message.decode())
    print(f"Decrypted Message: {decrypted_message}")

if __name__ == "__main__":
    main()
