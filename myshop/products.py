from flask import Flask, Blueprint, render_template, request, flash, jsonify, redirect, url_for, get_flashed_messages
from flask_login import login_user, logout_user, login_required, current_user
from datetime import datetime
from .models import Category,Brand
from . import db
from random import randint
products = Blueprint('products', __name__, template_folder='templates/products')



# Pokud přidám kategorii nebo budu psát kód s podmínkami např jako mám tady musí být delší 
# než dva znaky tak můžu každou podmínku vypsat a pod ní vrátit jsonify, kód tak bude 
# velmi dlouhý u více podmínek proto jsem si vytvořil funkci handle_response a proto můžu 
# pod podmínkou flashnout zprávu a přivolat funkci handle_responze, kód tak bude kratší při více
# podmínkách

def handle_response(data={}):
    return jsonify({
        'flash_message': get_flashed_messages(with_categories=True)
    } if not data else data)



@products.route('/addcategory', methods=['GET', 'POST'])
@login_required
def addcategory():
    categories = Category.query.all() 
    if request.method == 'POST':
        category = request.form.get("category")
        if len(category) < 3:
            flash("Category have to minimal 3 char!", category="danger")
            return handle_response()
        existing_category = Category.query.filter_by(category=category).first()
        if existing_category:
            flash("Categorie už existuje !", category="danger")
            return handle_response()
        else:
            new_category = Category(category=category, date_created=datetime.now())
            db.session.add(new_category)
            db.session.commit()
            flash("Categorie byla přidána", category="success")
            return handle_response(data={
                'flash_message': get_flashed_messages(with_categories=True),
                'category': new_category.category,
                'id': new_category.id,
                'date_created': new_category.date_created
            })
    return render_template('addcategory.html', categories=categories)





@products.route('/editcategory/<int:id>', methods=['GET','POST'])
@login_required
def editcategory(id):
    category = Category.query.filter_by(id=id).first()
    if request.method == 'POST':
        new_category = request.form.get("edit_category")
        if len(new_category) < 3:
            flash("Categorie musí mít minimálně 3 znaky!", category="danger")
            return handle_response()
        existing_category = Category.query.filter_by(category=new_category).first()
        if existing_category:
            flash("Categorie už existuje!", category="danger")
            return handle_response()
        else:
            category.category = new_category
            db.session.commit()
            flash('Category byla editována.', category='success')
            return handle_response(data={
            'flash_message': get_flashed_messages(with_categories=True),
            'category': category.category,
            })
    return render_template('editcategory.html', category=category)



@products.route('/deletecategory/<int:id>', methods=['DELETE'])
@login_required
def deletecategory(id):
    category = Category.query.filter_by(id=id).first()
    db.session.delete(category)
    db.session.commit()
    return jsonify({'message': 'Category deleted successfully'})






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

