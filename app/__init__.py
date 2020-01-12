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



@app.route("/")
def root():
    return jsonify({"success": True})


@app.route("/getinfo", methods=["POST","GET"])
def getinfo():

    issues = Issue.query.filter(Issue.status!="done").all()
    res = {
        "success" : True,
        "issues" : [ {
            "id" : issue.id,
            "line_id" : issue.line_id,
            "issue_type" :issue.issue_type,
            "detail1" : issue.detail1,
            "detail2" : issue.detail2,
            "remark" : issue.remark,
            "status" : issue.status,
            "submit_date" : issue.submit_date,
            "start_date" : issue.start_date,
            } for issue in issues] 
        }
    return jsonify(res)



@app.route("/doing", methods=["POST", "GET"])
def doing():
    if request.method =="POST" :
        data = request.get_json()
        issue = Issue.query.filter_by(id=data['id']).first()
        issue.status = "doing"

        db.session.commit()
            
        issues = Issue.query.filter(Issue.status!="done").all()
        res = {
            "success" : True,
            "issues" : [ {
                "id" : issue.id,
                "line_id" : issue.line_id,
                "issue_type" :issue.issue_type,
                "detail1" : issue.detail1,
                "detail2" : issue.detail2,
                "remark" : issue.remark,
                "status" : issue.status,
                "submit_date" : issue.submit_date,
                "start_date" : issue.start_date,
                } for issue in issues] 
            }
        return jsonify(res)


@app.route("/done", methods=["POST", "GET"])
def done():
    if request.method =="POST" :
        data = request.get_json()
        issue = Issue.query.filter_by(id=data['id']).first()
        issue.status = "done"

        db.session.commit()
            
        issues = Issue.query.filter(Issue.status!="done").all()
        res = {
            "success" : True,
            "issues" : [ {
                "id" : issue.id,
                "line_id" : issue.line_id,
                "issue_type" :issue.issue_type,
                "detail1" : issue.detail1,
                "detail2" : issue.detail2,
                "remark" : issue.remark,
                "status" : issue.status,
                "submit_date" : issue.submit_date,
                "start_date" : issue.start_date,
                } for issue in issues] 
            }
        return jsonify(res)


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
        issues = Issue.query.filter(Issue.status!="done").all()
        
        res = {
            "success": True,
            "issues": [issue.render() for issue in issues]
        }
       
    return jsonify(res) 
