import argparse
import platform
import logging
from backend.genetic_app_backend import run_backend
from secure_storage import SecureStore

logging.basicConfig(level=logging.INFO)

def main():
    parser = argparse.ArgumentParser(description="GenDan Genetic Intelligence CLI")
    parser.add_argument('--run', action='store_true', help="Run GenDan backend service")
    parser.add_argument('--secure', action='store_true', help="Launch secure storage interface")
    parser.add_argument('--info', action='store_true', help="Show system platform info")
    
    args = parser.parse_args()

    if args.info:
        logging.info(f"Detected platform: {platform.system()} {platform.release()}")
    
    if args.secure:
        logging.info("Launching Secure Storage...")
        store = SecureStore()
        store.initialize()

    if args.run:
        logging.info("Starting GenDan backend service...")
        run_backend()

if __name__ == '__main__':
    main()
