from flask import render_template
from . import main

@main.route('/')
def index():
    
    title="Welcome home"
    return render_template('index.html',title=title)

@main.route('/home')
def homepage():
    
    title="welcome homepage"
    return render_template('home.html',title=title)