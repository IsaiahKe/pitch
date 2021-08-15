from flask import render_template
from . import main

@main.errorhandler(404)
def notFoundError(error):
    
    return render_template('notfound.html'),404