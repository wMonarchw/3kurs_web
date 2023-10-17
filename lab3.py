from flask import Blueprint, render_template, request
lab3 = Blueprint('lab3', __name__)


@lab3.route('/lab3/')
def lab():
    return render_template('lab3.html')

@lab3.route('/lab3/form1')
def form1():
    errors = {}
    user = request.args.get('user')
    age = request.args.get('age')
    if user == '':
        errors['user'] = 'Заполните поле!'
    if age == '':
        errors['age'] = 'Заполните поле!'
        user = ''
        errors['user'] = 'Заполните поле!'
    sex = request.args.get('sex')
    return render_template('form1.html', user=user, age=age, sex=sex, errors=errors)

@lab3.route('/lab3/order')
def order():
    return render_template('order.html')

@lab3.route('/lab3/pay')
def pay():
    price = 0
    drink = request.args.get('drink')
    if drink == 'cofee':
        price = 120
    elif drink == 'black-tea':
        price = 80
    else: 
        price = 70
     

    if request.args.get('milk') == 'on':
        price += 30
    if request.args.get('sugar') == 'on':
        price +=10

    return render_template('pay.html', price=price)


@lab3.route('/lab3/success')
def success():
    return render_template('success.html')


@lab3.route('/lab3/ticket')
def ticket():
    return render_template('ticket.html')


@lab3.route('/lab3/ticket_buyed')
def ticket_buyed():
    name = request.args.get('name')
    age = request.args.get('age')
    ticket_type = request.args.get('ticket_type')
    berth = request.args.get('berth')
    luggage = request.args.get('luggage')
    departure = request.args.get('departure')
    destination = request.args.get('destination')
    date = request.args.get('date')
    
    if not all([name, age, departure, destination, date]):
        return "<script>alert('Пожалуйста, заполните все поля'); window.location='/lab3/ticket'</script>"
    else:
        pass
    age = int(age)
    if age < 18 or age > 120:
            return "<script>alert('Возраст введен некоректно!'); window.location='/lab3/ticket'</script>"
    else: 
        pass
    return render_template('ticket_buyed.html', name=name, age=age, ticket_type=ticket_type, berth=berth, luggage=luggage, departure=departure, destination=destination, date=date)