from dotenv import load_dotenv 
import os

load_dotenv() 
AUTH0_DOMAIN_VAR = os.environ.get("AUTH0_DOMAIN") 
API_AUDIENCE_VAR = os.environ.get("API_AUDIENCE") 
