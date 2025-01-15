
# GenDan - Genetic Algorithm Backend

## Overview
GenDan is a backend application demonstrating encryption and decryption functionality using the Python `cryptography` library. This version has been simplified for core functionality testing.

## Features
- Symmetric encryption and decryption using `Fernet` keys.
- Simple and secure implementation with helper classes.
- Fully tested with `unittest` framework.

## Setup Instructions

### Prerequisites
- Python 3.8 or higher
- pip (Python package manager)

### Installation
1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd GenDan-main
   ```

2. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

### Running the Application
To run the main script and see encryption in action:
```bash
python main.py
```

### Testing
To run the test suite:
```bash
pytest
```

## Docker Support
A `Dockerfile` is included for containerization. Build and run the container as follows:
```bash
docker build -t gendan .
docker run gendan
```

## Future Enhancements
- Integration with `grpc` for remote procedure calls.
- Advanced genetic algorithms for problem-solving.

## License
This project is licensed under the MIT License.
