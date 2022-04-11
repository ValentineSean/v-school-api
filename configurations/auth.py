import os

from flask_jwt_extended import JWTManager
from dotenv import load_dotenv

jwt = JWTManager()

# Environment Variables
load_dotenv()

jwt_secret_key = os.getenv("JWT_SECRET_KEY")

auth_credentials = {
    "jwt_secret_key": jwt_secret_key,
}