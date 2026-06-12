# app/extensions.py

from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager

# Database
db = SQLAlchemy()

# Database migration
migrate = Migrate()

# Authentication
login_manager = LoginManager()
login_manager.login_view = "admin.login"
login_manager.login_message = "Please log in to access this page."
login_manager.login_message_category = "warning"