from flask import Blueprint, redirect, url_for, render_template, request, session


lab7 = Blueprint('lab7', __name__)


@lab7.route('/lab7/')
def lab():
    return render_template('lab7/index.html')

@lab7.route('/lab7/drink')
def drink():
    return render_template('lab7/drink.html')

@lab7.route("/lab7/api", methods=['POST'])
def api():
    data = request.json

    if data['method'] == 'get-price':
        return get_price(data['params'])

    if data['method'] == 'pay':
        return pay(data['params'])
    
    if data['method'] == 'refund':
        return cancel_pay(data['params'])
    
    abort(400)

def get_price(params):
    return{"result": calcullate_price(params), "error": None}

def calcullate_price(params):
    drink = params['drink']
    milk = params['milk']
    sugar = params['sugar']

    if drink == 'coffee':
        price = 12
    elif drink =='black-tea':
        price = 80
    else:
        price = 70

    if milk:
        price += 30
    if sugar:
        price += 10

    return price

def pay(params):
    card_num = params['card_num']
    if len(card_num) != 16 or not card_num.isdigit():
        return {"result": None, "error": "Неверный номер карты"}

    cvv = params['cvv']
    if len(cvv) != 3 or not cvv.isdigit():
        return {"result": None, "error": "Неверный номер CVV"}

    price = calcullate_price(params)
    return {"result": f'С карты {card_num} списано {price} руб.', "error": None}

def cancel_pay(params):
    card_num = params['card_num']
    if len(card_num) != 16 or not card_num.isdigit():
        return {"result": None, "error": "Неверный номер карты"}

    cvv = params['cvv']
    if len(cvv) != 3 or not cvv.isdigit():
        return {"result": None, "error": "Неверный номер CVV"}

    price = calcullate_price(params)
    return {"result": f'На карту {card_num} возвращено {price} руб.', "error": None}