from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
import datetime
from sqlalchemy.sql import func


db = SQLAlchemy()


class Issue(db.Model):
    __tablename__='issues'
    id = db.Column(db.Integer, primary_key=True)
    line_id = db.Column(db.String(256))
    issue_type = db.Column(db.String(256))
    detail1 = db.Column(db.String(256))
    detail2 = db.Column(db.String(256))
    remark = db.Column(db.Text)
    status = db.Column(db.String(256), default="null")
    submit_date = db.Column(db.DateTime(timezone=True), server_default=func.now())
    start_date =  db.Column(db.DateTime(timezone=True), server_default=func.now())
    finish_date =  db.Column(db.DateTime(timezone=True), server_default=func.now())
    duration = db.Column(db.Integer)

    def render(self):
        return {
                "line_id" : self.line_id,
                "issue_type" :self.issue_type,
                "detail1" : self.detail1,
                "detail2" : self.detail2,
                "remark" : self.remark,
                "status" : self.status,
                "submit_date" : self.submit_date,
                "start_date" : self.start_date,
                "finish_date" :  self.finish_date,
                "duration" : self.duration
            }