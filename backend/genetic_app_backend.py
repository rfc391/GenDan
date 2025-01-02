
import grpc
from concurrent import futures
from cryptography.fernet import Fernet
import genetic_data_pb2 as pb2
import genetic_data_pb2_grpc as pb2_grpc

# Encryption Helper
class EncryptionHelper:
    def __init__(self, key):
        self.cipher = Fernet(key)

    def encrypt(self, message):
        return self.cipher.encrypt(message.encode())

    def decrypt(self, encrypted_message):
        return self.cipher.decrypt(encrypted_message.encode()).decode()

# gRPC Service Implementation
class GeneticAnalysisService(pb2_grpc.GeneticAnalysisServicer):
    def __init__(self, encryption_helper):
        self.encryption_helper = encryption_helper

    def AnalyzeGeneticData(self, request, context):
        try:
            decrypted_payload = self.encryption_helper.decrypt(request.encrypted_payload)
            disorders = ["Disease A", "Disease B"] if "mutation" in decrypted_payload else []

            response_payload = f"Identified {len(disorders)} genetic disorders. Details: {', '.join(disorders)}"
            encrypted_response = self.encryption_helper.encrypt(response_payload)

            response = pb2.EncryptedResponse(
                encrypted_payload=encrypted_response.decode()
            )
        except Exception as e:
            error_message = f"Error during analysis: {str(e)}"
            encrypted_error = self.encryption_helper.encrypt(error_message)
            response = pb2.EncryptedResponse(
                encrypted_payload=encrypted_error.decode()
            )
        return response

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    encryption_key = Fernet.generate_key()
    encryption_helper = EncryptionHelper(encryption_key)

    pb2_grpc.add_GeneticAnalysisServicer_to_server(
        GeneticAnalysisService(encryption_helper), server
    )

    print("Starting server on port 50051...")
    server.add_insecure_port("[::]:50051")
    server.start()
    server.wait_for_termination()

if __name__ == "__main__":
    serve()
