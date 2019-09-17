from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


def configure(app):
    db.init_app(app)
    app.db = db


class Data(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    event = db.Column(db.String(255))
    timestamp = db.Column(db.String(255))
