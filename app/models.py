from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
import datetime
from sqlalchemy.sql import func




db = SQLAlchemy()
