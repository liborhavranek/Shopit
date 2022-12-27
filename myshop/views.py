from flask import Flask, Blueprint, render_template

views = Blueprint('views', __name__, template_folder='templates')

@views.route('/views')
def view():
    return render_template('views.html')