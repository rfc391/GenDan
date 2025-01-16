
import logging

# Configure logging
logging.basicConfig(
    filename='app.log',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

class Logger:
    """A class to handle logging for traceability and compliance."""

    @staticmethod
    def log_info(message):
        """Log an informational message."""
        logging.info(message)

    @staticmethod
    def log_error(message):
        """Log an error message."""
        logging.error(message)

# Example usage:
# Logger.log_info("Fetching data from Ensembl API")
# Logger.log_error("Failed to fetch data from NCBI GenBank")
