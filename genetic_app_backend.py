
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.primitives import hashes, hmac
from cryptography.hazmat.primitives.serialization import (
    load_pem_private_key,
    load_pem_public_key,
    Encoding,
    PrivateFormat,
    PublicFormat,
    NoEncryption,
)
from cryptography.fernet import Fernet

class HybridEncryptionHelper:
    """
    A hybrid encryption helper class combining RSA for key exchange and Fernet for symmetric encryption.
    """

    def __init__(self):
        # Generate RSA key pair for asymmetric encryption
        self.private_key = rsa.generate_private_key(public_exponent=65537, key_size=2048)
        self.public_key = self.private_key.public_key()

    def export_keys(self):
        """Exports the private and public keys in PEM format."""
        private_key_pem = self.private_key.private_bytes(
            encoding=Encoding.PEM,
            format=PrivateFormat.PKCS8,
            encryption_algorithm=NoEncryption(),
        )
        public_key_pem = self.public_key.public_bytes(
            encoding=Encoding.PEM, format=PublicFormat.SubjectPublicKeyInfo
        )
        return private_key_pem, public_key_pem

    def encrypt(self, data, peer_public_key_pem):
        """Encrypts the data using hybrid encryption (RSA + Fernet)."""
        # Load peer's public key
        peer_public_key = load_pem_public_key(peer_public_key_pem)

        # Generate a symmetric key for Fernet
        symmetric_key = Fernet.generate_key()

        # Encrypt the symmetric key with the peer's public RSA key
        encrypted_symmetric_key = peer_public_key.encrypt(
            symmetric_key,
            padding.OAEP(mgf=padding.MGF1(algorithm=hashes.SHA256()), algorithm=hashes.SHA256(), label=None),
        )

        # Encrypt the data using Fernet
        fernet = Fernet(symmetric_key)
        encrypted_data = fernet.encrypt(data.encode())

        # Create an HMAC signature for data integrity
        h = hmac.HMAC(symmetric_key, hashes.SHA256())
        h.update(encrypted_data)
        signature = h.finalize()

        return encrypted_symmetric_key, encrypted_data, signature

    def decrypt(self, encrypted_symmetric_key, encrypted_data, signature):
        """Decrypts the data using hybrid encryption (RSA + Fernet)."""
        # Decrypt the symmetric key with the private RSA key
        symmetric_key = self.private_key.decrypt(
            encrypted_symmetric_key,
            padding.OAEP(mgf=padding.MGF1(algorithm=hashes.SHA256()), algorithm=hashes.SHA256(), label=None),
        )

        # Verify HMAC signature for data integrity
        h = hmac.HMAC(symmetric_key, hashes.SHA256())
        h.update(encrypted_data)
        h.verify(signature)  # Will raise an exception if the signature is invalid

        # Decrypt the data using Fernet
        fernet = Fernet(symmetric_key)
        decrypted_data = fernet.decrypt(encrypted_data).decode()

        return decrypted_data



from logger import Logger

class LoggedHybridEncryptionHelper(HybridEncryptionHelper):
    def encrypt(self, data, peer_public_key_pem):
        Logger.log_info("Starting encryption process.")
        try:
            encrypted_symmetric_key, encrypted_data, signature = super().encrypt(data, peer_public_key_pem)
            Logger.log_info("Encryption successful.")
            return encrypted_symmetric_key, encrypted_data, signature
        except Exception as e:
            Logger.log_error(f"Encryption failed: {e}")
            raise

    def decrypt(self, encrypted_symmetric_key, encrypted_data, signature):
        Logger.log_info("Starting decryption process.")
        try:
            decrypted_data = super().decrypt(encrypted_symmetric_key, encrypted_data, signature)
            Logger.log_info("Decryption successful.")
            return decrypted_data
        except Exception as e:
            Logger.log_error(f"Decryption failed: {e}")
            raise
