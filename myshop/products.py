from flask import Flask, Blueprint, render_template, request, flash, jsonify, redirect, url_for, get_flashed_messages
from flask_login import login_user, logout_user, login_required, current_user
from datetime import datetime
from .models import Category,Brand,Color,Product
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
        category = request.form.get("category").title()
        if len(category) < 3:
            flash("Kategorie musí mít minimálně 3 znaky", category="danger")
            return handle_response()
        existing_category = Category.query.filter_by(category=category).first()
        if existing_category:
            flash("Kategorie už existuje !", category="danger")
            return handle_response()
        else:
            new_category = Category(category=category, date_created=datetime.now())
            db.session.add(new_category)
            db.session.commit()
            flash("Kategorie byla přidána", category="success")
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
        new_category = request.form.get("edit_category").title()
        if len(new_category) < 3:
            flash("Kategorie musí mít minimálně 3 znaky!", category="danger")
            return handle_response()
        existing_category = Category.query.filter_by(category=new_category).first()
        if existing_category:
            flash("Kategorie už existuje!", category="danger")
            return handle_response()
        else:
            category.category = new_category
            db.session.commit()
            flash('Kategorie byla editována.', category='success')
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
    return jsonify({'message': 'Kategorie byla smazána'})






@products.route('/addbrand', methods=['GET', 'POST'])
@login_required
def addbrand():
    brands = Brand.query.all() 
    if request.method == 'POST':
        brand = request.form.get("brand").title()
        if len(brand) < 3:
            flash("Značka musí mít alespoň tři znaky!", category="danger")
            return handle_response()
        existing_brand = Brand.query.filter_by(brand=brand).first()
        if existing_brand:
            flash("Značka už existuje !", category="danger")
            return handle_response()
        else:
            new_brand = Brand(brand=brand, date_created=datetime.now())
            db.session.add(new_brand)
            db.session.commit()
            flash("Značka byla přidána", category="success")
            return handle_response(data={
                'flash_message': get_flashed_messages(with_categories=True),
                'brand': new_brand.brand,
                'id': new_brand.id,
                'date_created': new_brand.date_created
            })
    return render_template('addbrand.html', brands=brands)
  
  
  
@products.route('/editbrand/<int:id>', methods=['GET','POST'])
@login_required
def editbrand(id):
    brand = Brand.query.filter_by(id=id).first()
    if request.method == 'POST':
        new_brand = request.form.get("edit_brand").title()
        if len(new_brand) < 3:
            flash("Značka musí mít minimálně 3 znaky!", category="danger")
            return handle_response()
        existing_brand = Brand.query.filter_by(brand=new_brand).first()
        if existing_brand:
            flash("Značka už existuje!", category="danger")
            return handle_response()
        else:
            brand.brand = new_brand
            db.session.commit()
            flash('Značka byla upravena.', category='success')
            return handle_response(data={
            'flash_message': get_flashed_messages(with_categories=True),
            'brand': brand.brand,
            })
    return render_template('editbrand.html', brand=brand)
  
  
  
@products.route('/deletebrand/<int:id>', methods=['DELETE'])
@login_required
def deletebrand(id):
    brand = Brand.query.filter_by(id=id).first()
    db.session.delete(brand)
    db.session.commit()
    return jsonify({'message': 'Značka byla smazána'})



@products.route('/addcolor', methods=['GET', 'POST'])
@login_required
def addcolor():
    colors = Color.query.all() 
    if request.method == 'POST':
        color = request.form.get("color").title()
        if len(color) < 3:
            flash("Barva musí mít minimálně 3 znaky", category="danger")
            return handle_response()
        existing_color = Color.query.filter_by(color=color).first()
        if existing_color:
            flash("Barva už existuje !", category="danger")
            return handle_response()
        else:
            new_color = Color(color=color, date_created=datetime.now())
            db.session.add(new_color)
            db.session.commit()
            flash("Barva byla přidána", category="success")
            return handle_response(data={
                'flash_message': get_flashed_messages(with_categories=True),
                'color': new_color.color,
                'id': new_color.id,
                'date_created': new_color.date_created
            })
    return render_template('addcolor.html', colors=colors)
  
  
  
@products.route('/editcolor/<int:id>', methods=['GET','POST'])
@login_required
def editcolor(id):
    color = Color.query.filter_by(id=id).first()
    if request.method == 'POST':
        new_color = request.form.get("edit_color").title()
        if len(new_color) < 3:
            flash("Barva musí mít minimálně 3 znaky!", category="danger")
            return handle_response()
        existing_color = Color.query.filter_by(color=new_color).first()
        if existing_color:
            flash("Barva už existuje!", category="danger")
            return handle_response()
        else:
            color.color = new_color
            db.session.commit()
            flash('Barva byla editována.', category='success')
            return handle_response(data={
            'flash_message': get_flashed_messages(with_categories=True),
            'color': color.color,
            })
    return render_template('editcolor.html', color=color)
  
  
  
@products.route('/deletecolor/<int:id>', methods=['DELETE'])
@login_required
def deletecolor(id):
    color = Color.query.filter_by(id=id).first()
    db.session.delete(color)
    db.session.commit()
    return jsonify({'message': 'Barva byla smazána'})
  
  
  
  
@products.route('/addproduct/', methods=['GET', 'POST'])
@login_required
def addproduct():
    brands = Brand.query.all()
    products = Product.query.all() 
    if request.method == 'POST':
      product = request.form.get("product").title()
      price = request.form.get('price')
      brand_id = request.form.get('brand')
      if len(product) < 3:
          flash("Produkt musí mít minimálně 3 znaky", category="danger")
      existing_product = Product.query.filter_by(product=product).first()
      if existing_product:
          flash("Produkt už existuje !", category="danger")
      else:
          brand = Brand.query.get(brand_id)
          new_product= Product(product=product, price=price, brand=brand)
          db.session.add(new_product)
          db.session.commit()
    return render_template('addproduct.html', products=products, brands=brands)