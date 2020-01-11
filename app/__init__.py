from flask import Flask, jsonify, request
from .config import Config
from .models import db, Issue
from .cli import create_db
from flask_migrate import Migrate
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
import stripe
import uuid
from dotenv import load_dotenv
load_dotenv()


app = Flask(__name__)
CORS(app) 
app.config.from_object(Config)
app.cli.add_command(create_db)
db.init_app(app)
migrate = Migrate(app, db) 



@app.route("/getinfo", methods=["POST","GET"])
def getinfo():
    return jsonify(
        {"success":True}
        )
