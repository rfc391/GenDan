
# GenDan

## Overview
This application provides precision medicine services using encrypted genetic data. It leverages gRPC for communication, Protobuf for data serialization, and advanced encryption for security.

"R.I.P Darren"

## Features
- Fully encrypted payload communication.
- Secure handling of genetic data.
- Automated update-ready structure.

## Setup
1. Install dependencies:
   ```bash
   pip install grpcio grpcio-tools cryptography
   ```
2. Generate Protobuf files:
   ```bash
   python -m grpc_tools.protoc -I=proto --python_out=backend --grpc_python_out=backend proto/genetic_data.proto
   ```
3. Run the server:
   ```bash
   python backend/genetic_app_backend.py
   ```

## Testing
Run tests using:
```bash
python -m unittest discover -s tests
```

## CI/CD
Automated workflows are included for continuous integration and testing.
