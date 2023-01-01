from . import db 
from flask import flash
from datetime import datetime
from flask_login import UserMixin


class Costumer(db.Model, UserMixin):
    #  -------------------Uzivatel-------------------
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), unique=True)
    email = db.Column(db.String(50), unique=True)
    phone_code = db.Column(db.String(50), unique=False)
    phone = db.Column(db.String(50), unique=False)
    password = db.Column(db.String(200), unique=False)


# --------------- Fakturacni udaje ---------------------
    faktura_first_name = db.Column(db.String(50), unique=False, nullable=True)
    faktura_last_name = db.Column(db.String(50), unique=False, nullable=True)
    faktura_city = db.Column(db.String(50), unique=False, nullable=True)
    faktura_street = db.Column(db.String(50), unique=False, nullable=True)
    faktura_zipcode = db.Column(db.String(50), unique=False, nullable=True)
    
    
# ---------------Dodaci udaje ---------------------------------

    dodej_first_name = db.Column(db.String(50), unique=False, nullable=True)
    dodej_last_name = db.Column(db.String(50), unique=False, nullable=True)
    dodej_company = db.Column(db.String(50), unique=False, nullable=True)
    dodej_city = db.Column(db.String(50), unique=False, nullable=True)
    dodej_street = db.Column(db.String(50), unique=False, nullable=True)
    dodej_zipcode = db.Column(db.String(50), unique=False, nullable=True)
    dodej_info = db.Column(db.String(50), unique=False, nullable=True)
    dodej_phone_code = db.Column(db.String(50), unique=False, nullable=True)
    dodej_phone = db.Column(db.String(50), unique=False, nullable=True)
    
# -------------------Firemní údaje -------------------------------------

    firma_ico = db.Column(db.String(50), unique=False, nullable=True)
    firma_dic = db.Column(db.String(50), unique=False, nullable=True)
    firma_bank_acc = db.Column(db.String(50), unique=False, nullable=True)
    firma_bank_number = db.Column(db.String(50), unique=False, nullable=True)
    firma_spec_symbol = db.Column(db.String(50), unique=False, nullable=True)


#_____________________ ostatni ________________________________

    user_pic = db.Column(db.String(150), nullable=True)
    last_login = db.Column(db.DateTime, default=datetime.utcnow)
    date_created = db.Column(db.DateTime, nullable=False, default=datetime.utcnow())
    
    
    
    
# class Product(db.Model, UserMixin):
#     id = db.Column(db.Integer, primary_key=True)
#     name = db.Column(db.String(80), nullable=False)
#     price = db.Column(db.Numeric(10,2), nullable=False)
#     discount = db.Column(db.Integer, default=0)
#     stock = db.Column(db.Integer, nullable=False)
#     sold = db.Column(db.Integer)
#     size = db.Column(db.Text, nullable=False)
#     description = db.Column(db.Text, nullable=False)
#     pub_date = db.Column(db.DateTime, nullable=False,default=datetime.utcnow)
    
    
# pridat rating, recenze, categorie, brand, udelat color s id brand, kategorie



class Category(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    category = db.Column(db.String(30), nullable=False, unique=True)
    date_created = db.Column(db.DateTime, nullable=False, default=datetime.utcnow())

    
    
class Brand(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    brand = db.Column(db.String(30), nullable=False, unique=True)
    date_created = db.Column(db.DateTime, nullable=False, default=datetime.utcnow())


