from flask import request, redirect, render_template, session, flash
from app import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True)
    password = db.Column(db.String(120))
    movies = db.relationship("Movie", backref="viewer")
    
    def __init__(self, email, password):
        self.email = email
        self.password = password

    def __repr__(self):
        return '<User %r>' % self.email

class Movie(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120))
    watched = db.Column(db.Boolean)
    rating = db.Column(db.String(20))
    viewer_id = db.Column(db.Integer, db.ForeignKey("user.id"))

    def __init__(self, name, viewer):
        self.name = name
        self.watched = False
        self.viewer = viewer

    def __repr__(self):
        return '<Movie %r>' % self.name