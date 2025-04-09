
import pytest
from genetic_app_backend import HybridEncryptionHelper

def test_hybrid_encryption_workflow():
    helper = HybridEncryptionHelper()
    private_key_pem, public_key_pem = helper.export_keys()

    # Test data
    data = "Test message for encryption"

    # Encrypt data
    encrypted_symmetric_key, encrypted_data, signature = helper.encrypt(data, public_key_pem)

    # Ensure encrypted components are not None
    assert encrypted_symmetric_key is not None
    assert encrypted_data is not None
    assert signature is not None

    # Decrypt data
    decrypted_data = helper.decrypt(encrypted_symmetric_key, encrypted_data, signature)

    # Verify decrypted data matches original
    assert decrypted_data == data

def test_invalid_signature_detection():
    helper = HybridEncryptionHelper()
    private_key_pem, public_key_pem = helper.export_keys()

    # Test data
    data = "Test message for encryption"

    # Encrypt data
    encrypted_symmetric_key, encrypted_data, signature = helper.encrypt(data, public_key_pem)

    # Modify the signature to simulate tampering
    tampered_signature = signature[:-1] + b'0'

    # Ensure decryption fails with tampered signature
    with pytest.raises(Exception):
        helper.decrypt(encrypted_symmetric_key, encrypted_data, tampered_signature)
