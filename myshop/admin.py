from flask import Flask, Blueprint, render_template

admin = Blueprint('admin', __name__, template_folder='templates')

@admin.route('/admin')
def admin_page():
    return render_template('admin.html')