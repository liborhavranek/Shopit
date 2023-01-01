from flask import Flask, Blueprint, render_template, request, flash, jsonify, redirect, url_for, get_flashed_messages
from flask_login import login_user, logout_user, login_required, current_user
from datetime import datetime
from .models import Category,Brand
from . import db
from random import randint
products = Blueprint('products', __name__, template_folder='templates/products')



@products.route('/addcategory', methods=['GET', 'POST'])
@login_required
def addcategory():
    categories = Category.query.all() 
    if request.method == 'POST':
        category = request.form.get("category")
        new_category = Category(category=category, date_created=datetime.now())
        db.session.add(new_category)
        db.session.commit()
        flash("Category added successfully!", "success")
        return jsonify({
            'flash_message': get_flashed_messages(with_categories=True),
            'category': new_category.category,
            'id': new_category.id,
            'date_created': new_category.date_created
        })
    return render_template('addcategory.html', categories=categories)

























# @products.route('/editcategory/<int:id>', methods=['POST', 'GET'])
# @login_required
# def editcategory(id):
#     categories = Category.query.all() 
#     if request.method == 'POST':
#         category = Category.query.filter_by(id=id).first()
#         edit_category = request.form.get("edit_category")
#         if not edit_category:
#             flash('Název kategorie nesmí být prázdný', category='error')
#         else:
#             category_exist = Category.query.filter_by(category=edit_category).first()
#             if category_exist:
#                 flash('Tato kategorie již existuje', category='error')
#             elif len(edit_category) < 3:
#                 flash('Název kategorie musí mít alespoň 3 znaky', category='error')
#             else:
#                 category.category = edit_category
#                 db.session.commit()
#                 flash('Kategorie byla upravena.', category='success')
#                 return render_template('editcategory.html', categories=categories)
#     return render_template('editcategory.html', categories=categories)




# @products.route('/addbrand', methods=['GET', 'POST'])
# @login_required
# def addbrand():
#     brands = Brand.query.all() 
#     if request.method == 'POST':
#         brand = request.form.get("brand")
#         brand_exist = Brand.query.filter_by(brand=brand).first()
#         if brand_exist:
#             flash('Tato značka již existuje', category='error')
#         else:
#             new_brand = Brand(brand=brand)
#             db.session.add(new_brand)
#             db.session.commit()
#             flash('Značka byla přidána.', category='success')
#             return render_template('addbrand.html')
#     return render_template('addbrand.html', brands=brands)

