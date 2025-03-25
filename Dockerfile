
FROM python:3.11-slim

# Set the working directory
WORKDIR /app

# Copy project files into the container
COPY requirements.txt /app/
RUN pip install --no-cache-dir -r /app/requirements.txt
COPY . /app

# Install required dependencies
RUN pip install -r requirements.txt

# Command to run the application
EXPOSE 5000
CMD ["python", "main.py"]
