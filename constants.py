# config/config.py

import os
from dotenv import load_dotenv

load_dotenv()


class BaseConfig:
    """Base configuration shared across environments"""

    # Core Flask
    SECRET_KEY = os.getenv("SECRET_KEY", "super_secret_flood_key")
    DEBUG = False
    TESTING = False

    # Database
    SQLALCHEMY_DATABASE_URI = os.getenv(
        "DATABASE_URL",
        "sqlite:///flood.db"
    )
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # AI Model Settings
    MODEL_INPUT_DIM = 10
    MODEL_BATCH_SIZE = 32
    MODEL_EPOCHS = 5

    # Federated Learning
    FEDERATED_ROUNDS = 5
    FEDERATED_CLIENTS = 3
    FEDERATED_AGGREGATION = "fedavg"

    # Prediction Thresholds
    FLOOD_HIGH_THRESHOLD = 0.75
    FLOOD_MEDIUM_THRESHOLD = 0.45

    # Alert Settings
    EMAIL_ENABLED = True
    SMS_ENABLED = True

    SMTP_SERVER = os.getenv("SMTP_SERVER", "smtp.gmail.com")
    SMTP_PORT = int(os.getenv("SMTP_PORT", 587))
    SMTP_USERNAME = os.getenv("SMTP_USERNAME", "arungudi48@gmail.com")
    SMTP_PASSWORD = os.getenv("SMTP_PASSWORD", "jzepzxtiviioabjj")

    TWILIO_ACCOUNT_SID = os.getenv("TWILIO_ACCOUNT_SID", "ACb217641a541ca13646f0dc920c17268f")
    TWILIO_AUTH_TOKEN = os.getenv("TWILIO_AUTH_TOKEN", "69eb5b26fdcf2be191fa9785919aa20a")
    TWILIO_PHONE_NUMBER = os.getenv("TWILIO_PHONE_NUMBER", "(775) 261-7785")

    # System Performance
    REALTIME_REFRESH_SECONDS = 3
    MAX_WORKERS = 4


class DevelopmentConfig(BaseConfig):
    DEBUG = True


class ProductionConfig(BaseConfig):
    DEBUG = False


config_by_name = {
    "development": DevelopmentConfig,
    "production": ProductionConfig
}