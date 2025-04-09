
#!/bin/bash

echo "Starting deployment process..."

# Check if Docker is installed
if ! command -v docker &> /dev/null
then
    echo "Docker not installed. Please install Docker to proceed."
    exit 1
fi

# Build the Docker image
docker build -t genetic-app .

# Run the Docker container
docker run -d -p 8080:8080 --name genetic-app-container genetic-app

echo "Deployment complete. The application is running on port 8080."
