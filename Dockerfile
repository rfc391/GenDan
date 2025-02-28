
FROM python:3.14.0a1-slim

# Set the working directory
WORKDIR /app

# Copy project files into the container
COPY . /app

# Install required dependencies
RUN pip install -r requirements.txt

# Command to run the application
CMD ["python", "main.py"]
