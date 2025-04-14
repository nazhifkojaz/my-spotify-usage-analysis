from dotenv import load_dotenv
import os

# Add your secret keys to a .env file
# load environment variables from .env file
load_dotenv(override=True)

# Get the environment variables
SPOTIFY_CLIENT_ID = os.getenv("SPOTIFY_CLIENT_ID")
SPOTIFY_CLIENT_SECRET = os.getenv("SPOTIFY_CLIENT_SECRET")