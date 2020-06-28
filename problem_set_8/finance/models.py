from flask_sqlalchemy import SQLAlchemy
from application import db


class Users(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password_hash = db.Column(db.String(120), nullable=False)
    cash = db.Column(db.Integer, default=10000)

    def __repr__(self):
        return f'<User {self.username}>'