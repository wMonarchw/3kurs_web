from flask import Blueprint, redirect, url_for, render_template, Blueprint, request

lab4 = Blueprint('lab4', __name__)


@lab4.route('/lab4/')
def lab():
    return render_template('lab4.html')

@lab4.route('/lab4/login/', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        return render_template("login.html")

    username = request.form.get('username')
    password = request.form.get('password')
    error = None 
    if not username and not password:
        error = 'Нет логина и пароля'
    elif not username:
        error = 'Нет логина'
    elif not password:
        error = 'Нет пароля'
    elif username == 'alex' and password == '123':
        return render_template("success1.html", username=username)
    else:
        error = 'Неверный логин или пароль!'

    return render_template("login.html", error=error, username=username, password=password)

@lab4.route('/lab4/freeze/', methods=['GET', 'POST'])
def freeze():
    if request.method == 'GET':
        return render_template("freeze.html")
    
    temperature = request.form.get('temperature')
    message = None
    if not temperature:
        message = 'Не задана температура'
    elif int(temperature) < -12:
        message = 'Не удалось установить температуру слишком низкое значение'
    elif int(temperature) > -1: 
        message = 'Не удалось установить температуру слишком высокое значение'
    elif int(temperature) >=-12 and int(temperature) <=-9:
        message = f"Установлена температура {temperature} ***"
    elif int(temperature) >=-8 and int(temperature) <=-5:
        message = f"Установлена температура {temperature} **"
    elif int(temperature) >=-4 and int(temperature) <=-1:
        message = f"Установлена температура {temperature} *"     
    
    return render_template('freeze.html', temperature=temperature, message=message)