from flask import Flask, Blueprint, render_template

products = Blueprint('products', __name__, template_folder='templates')

@products.route('/products')
def product():
    return render_template('products.html')