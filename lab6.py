from flask import Blueprint, redirect, url_for, render_template, Blueprint, request, session
from Db import db

from Db.models import users, articles
from werkzeug.security import check_password_hash, generate_password_hash
from flask_login import login_user, login_required, current_user

lab6 = Blueprint('lab6', __name__)

@lab6.route('/lab6/check')
def main():
    my_users = users.query.all()
    print(my_users)
    return 'console'

@lab6.route('/lab6/checkarticles')
def checkarticles():
    my_articles = articles.query.all()
    print(my_articles)
    return 'console'


@lab6.route('/lab6/register', methods = ['GET', 'POST'])
def register():
    errors = []
    if request.method == 'GET':
        return render_template('register.html')
    
    username_form = request.form.get('username')
    password_form = request.form.get('password')

    isUserExist = users.query.filter_by(username=username_form).first()
    if isUserExist is not None:
        return render_template('register.html')
    
    if not (username_form or password_form):
        errors.append("Пожалуйста заполните все поля")
        print(errors)
        return render_template('register.html', errors=errors)
    if username_form == '':
        errors.append("Пожалуйста заполните все поля")
        print(errors)
        return render_template('register.html', errors=errors)
    if password_form == '':
        errors.append("Пожалуйста заполните все поля")
        print(errors)
        return render_template('register.html', errors=errors)
    

    hashPassword = generate_password_hash(password_form, method='pbkdf2')
    newUser = users(username=username_form, password=hashPassword)

    db.session.add(newUser)
    db.session.commit()

    return redirect('/lab6/login')





