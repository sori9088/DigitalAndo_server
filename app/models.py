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
    datail2 = db.Column(db.String(256))
    remark = db.Column(db.Text)
    status = db.Column(db.String(256))
    submit_date = db.Column(db.DateTime(timezone=True), server_default=func.now())
    start_date =  db.Column(db.DateTime(timezone=True), server_default=func.now())
    finish_date =  db.Column(db.DateTime(timezone=True), server_default=func.now())
    duration = db.Column(db.Integer)

