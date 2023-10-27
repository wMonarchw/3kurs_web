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

@lab4.route('/lab4/zerno/', methods=['GET', 'POST'])
def zerno():
    if request.method == 'GET':
        return render_template("zerno.html")

    zerno = request.form.get('zerno')
    zerno_weight = request.form.get('zerno_weight')
    zerno_weight = float(zerno_weight)
    message = None
    price = 0

    if zerno == 'yachmen':
        price = 12000
    elif zerno == 'oves':
        price = 8500
    elif zerno == 'psheno':
        price = 8700
    elif zerno == 'rozj':
        price = 14000
    else:
        price = 0
    
    sum = price * zerno_weight
    discount = None
    if zerno_weight > 50:
        sum = (price * zerno_weight) * 0.9
        discount = (price * zerno_weight) * 0.1 
        message = f'За взятый объем свыше 50 тонн присовена скидка = {discount} руб. Финальная цена товара составит = {sum}руб.'
    elif zerno_weight <= 50:
        message = f'Цена товаров = {sum}руб.'
    elif zerno_weight >= 500:
        message = 'Такого обьема зерна нет в наличии'
    elif not zerno_weight:
        message = 'Невведен вес'
    elif zerno_weight == 0:
        message = 'Неккоректное значение веса'
    else:
        pass

    return render_template('zerno.html', zerno=zerno, zerno_weight=zerno_weight, message=message, price=price)