from datetime import datetime

from flask_sqlalchemy import SQLAlchemy
from application import db


class Users(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password_hash = db.Column(db.String(120), nullable=False)
    cash = db.Column(db.Integer, default=10000)
    transactions = db.relationship("Transaction", backref="user", lazy=True)

    def __repr__(self):
        return f"<User {self.username}>"


class Transaction(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False)
    symbol = db.Column(db.String(10), nullable=False)
    name = db.Column(db.String(80))
    price = db.Column(db.Integer, nullable=False)
    count = db.Column(db.Integer, nullable=False)
    sold = db.Column(db.Boolean, default=False)
    date_time = db.Column(db.DateTime, default=datetime.utcnow())

    def __repr__(self):
        return f"<Transaction {self.symbol}"
