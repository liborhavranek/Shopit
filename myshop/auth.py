from flask import Flask, Blueprint, render_template

auth = Blueprint('auth', __name__, template_folder='templates')

@auth.route('/auth')
def authh():
    return render_template('auth.html')