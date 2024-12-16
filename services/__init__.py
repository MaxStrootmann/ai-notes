import os
from dotenv import load_dotenv

# Load .env file when the 'services' package is imported
load_dotenv()

# Optional: Print or debug to ensure it's loaded
# print(f"ENV LOADED - APP_ENV: {os.getenv('APP_ENV')}")

