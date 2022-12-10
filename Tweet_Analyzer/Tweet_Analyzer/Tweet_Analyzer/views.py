"""
Routes and views for the flask application.
"""

from datetime import datetime
from flask import render_template
from Tweet_Analyzer import app

@app.route('/')
@app.route('/login')
def login():
    """Renders the login page."""
    return render_template(
        'login.html',
        title='login Page',
        year=datetime.now().year,
    )

@app.route('/register')
def register():
    """Renders the register page."""
    return render_template(
        'register.html',
        title='register',
        year=datetime.now().year,
    )

@app.route('/home')
def home():
    """Renders the home page."""
    return render_template(
        'dashboard.html',
        title='Home Page',
        year=datetime.now().year,
    )

@app.route('/account')
def account():
    """Renders the account page."""
    return render_template(
        'account.html',
        title='account',
        year=datetime.now().year,
    )

@app.route('/profile')
def profile():
    """Renders the profile page."""
    return render_template(
        'profile.html',
        title='profile',
        year=datetime.now().year,
    )

@app.route('/record')
def record():
    """Renders the record page."""
    return render_template(
        'record.html',
        title='record',
        year=datetime.now().year,
    )

