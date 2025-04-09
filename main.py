
from genetic_app_backend import HybridEncryptionHelper

def main():
    # Initialize the hybrid encryption helper
    helper = HybridEncryptionHelper()
    
    # Export public and private keys
    private_key_pem, public_key_pem = helper.export_keys()
    
    # Simulate encryption with the public key
    data = "This is a secure message."
    encrypted_symmetric_key, encrypted_data, signature = helper.encrypt(data, public_key_pem)
    
    # Output the encrypted components
    print("Encrypted symmetric key:", encrypted_symmetric_key)
    print("Encrypted data:", encrypted_data)
    print("HMAC signature:", signature)
    
    # Simulate decryption with the private key
    decrypted_data = helper.decrypt(encrypted_symmetric_key, encrypted_data, signature)
    print("Decrypted data:", decrypted_data)

if __name__ == "__main__":
    main()
