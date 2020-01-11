from flask import Flask, jsonify, request
from .config import Config
from .models import db, Issue
from .cli import create_db
from flask_migrate import Migrate
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
import datetime
import uuid
from dotenv import load_dotenv
load_dotenv()

app = Flask(__name__)
CORS(app) 
app.config.from_object(Config)
app.cli.add_command(create_db)
db.init_app(app)
migrate = Migrate(app, db) 

@app.route("/", methods=["POST","GET"])
def root():
    return jsonify(
        {"success": True}
    )

@app.route("/getinfo", methods=["POST","GET"])
def getinfo():
    return jsonify(
        {"success":True}
        )

@app.route("/send_issue", methods=["POST", "GET"])
def send_issue():
    if request.method == "POST":
        data = request.get_json()
        data1 = request.get_json()['detail1']
        data2 = request.get_json()['detail2']
        
        new_issue = Issue(
            line_id = data['line_id'],
            issue_type = datetime.datetime.now(),
            detail1 = data1['title'],
            detail2 = data2['title'],
            remark = data['remark'],
            submit_date = datetime.datetime.now(),
        )
        db.session.add(new_issue)
        db.session.commit()
        issues = Issue.query.all()
        
        res = {
            "success": True,
            "issues": [issue.render() for issue in issues]
        }
       
    return jsonify(res) 
