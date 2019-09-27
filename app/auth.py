# auth.py

from flask import Blueprint
from flask import render_template, request, redirect
from app import app, db
from app.models import Entry

auth = Blueprint('auth', __name__)

@app.route('/login')
def login():
    return redirect('/')

@app.route('/signup')
def signup():
    return 'Signup'

@app.route('/logout')
def logout():
    return 'Logout'