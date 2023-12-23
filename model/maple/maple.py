import os
from dotenv import load_dotenv

load_dotenv()

APIKEY = os.environ.get('APIKEY')
APIADDRESS = os.environ.get('API_ADDRESS')
API_HEADER = os.environ.get('API_HEADER')