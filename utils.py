import sqlitecloud
import hashlib
import os
from dotenv import load_dotenv

# Load environment variables from the .env file
load_dotenv()

# Retrieve cloud DB URL and Admin API key from .env
CLOUD_DB_URL = os.getenv('CLOUD_DB_URL')
ADMIN_API_KEY = os.getenv('ADMIN_API_KEY')