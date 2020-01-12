from flask import Flask, jsonify, request
from .config import Config
from .models import db, Issue
from .cli import create_db
from flask_migrate import Migrate
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
import datetime
import uuid
from twilio.rest import Client

from dotenv import load_dotenv
load_dotenv()

app = Flask(__name__)
CORS(app) 
app.config.from_object(Config)
app.cli.add_command(create_db)
db.init_app(app)
migrate = Migrate(app, db) 

account_sid = 'ACa169c83ab4e4f2c73f23799b68c61d5d'
auth_token = 'f802b852e11f57f36b316891fd2574fe'
client = Client(account_sid, auth_token)
 


# message = client.messages.create(
#                               from_='whatsapp:+14155238886',
#                               body='Hello, Scott! How are you?',
#                               to='whatsapp:+84902555174'
#                           )
 
# message = client.messages.create(
#                               from_='whatsapp:+14155238886',
#                               body='Hello, Cliff! How are you?',
#                               to='whatsapp:+84937574917'
#                           )
 
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
            issue_type = data['type'],
            detail1 = data1['title'],
            detail2 = data2['title'],
            remark = data['remark'],
            submit_date = datetime.datetime.now(),
        )
        db.session.add(new_issue)
        db.session.commit()
        issues = Issue.query.filter(Issue.status!="done").all()
        
        message = client.messages.create(
                              from_='whatsapp:+14155238886',
                              body='Hello, Bocard! How are you?',
                              to='whatsapp:+84353585386'
                          )
        print(message.sid)                 
        res = {
            "success": True,
            "issues": [issue.render() for issue in issues]
        }
       
    return jsonify(res) 
