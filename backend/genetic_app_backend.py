
import grpc
from concurrent import futures
from cryptography.fernet import Fernet

class EncryptedMessage:
    def __init__(self, payload):
        self.payload = payload

    @staticmethod
    def encrypt_payload(data, cipher):
        return cipher.encrypt(data.encode())

    @staticmethod
    def decrypt_payload(data, cipher):
        return cipher.decrypt(data.encode()).decode()

# Encryption Helper
class EncryptionHelper:
    def __init__(self, key):
        self.cipher = Fernet(key)

    def encrypt(self, message):
        return self.cipher.encrypt(message.encode())

    def decrypt(self, encrypted_message):
        return self.cipher.decrypt(encrypted_message.encode()).decode()

# gRPC Service Implementation
class GeneticAnalysisService:
    def __init__(self, encryption_helper):
        self.encryption_helper = encryption_helper

    def AnalyzeGeneticData(self, request, context):
        try:
            decrypted_payload = self.encryption_helper.decrypt(request.payload)
            disorders = ["Disease A", "Disease B"] if "mutation" in decrypted_payload else []

            response_payload = f"Identified {len(disorders)} genetic disorders. Details: {', '.join(disorders)}"
            encrypted_response = self.encryption_helper.encrypt(response_payload)

            return EncryptedMessage(payload=encrypted_response.decode())
        except Exception as e:
            error_message = f"Error during analysis: {str(e)}"
            encrypted_error = self.encryption_helper.encrypt(error_message)
            return EncryptedMessage(payload=encrypted_error.decode())

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    encryption_key = Fernet.generate_key()
    encryption_helper = EncryptionHelper(encryption_key)

    service = GeneticAnalysisService(encryption_helper)
    print("Starting server on port 50051...")
    server.add_insecure_port("[::]:50051")
    server.start()
    server.wait_for_termination()

if __name__ == "__main__":
    serve()
