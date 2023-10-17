from flask import Flask, redirect, url_for, render_template, Blueprint, request
from lab1 import lab1 

app = Flask(__name__)
app.register_blueprint(lab1)
# Лаба 2

@app.route('/lab2/example')
def example():
    name = 'Завгородний Илья Артурович'
    number_labolatory = '2'
    number_course = '3 курс'
    group = 'ФБИ-14'
    fruits = [
        {'name': 'Яблоки', 'price': 100},
        {'name': 'Груши', 'price': 166},
        {'name': 'Апельсины', 'price': 320},
        {'name': 'Бананы', 'price': 1030},
        {'name': 'Манго', 'price': 1520}
        ]
    books = [
        {'name': 'Куджо', 'author': 'Стивен Кинг', 'size': '400 страниц'},
        {'name': 'Мастер и Маргарита', 'author': 'Михаил Булгаков', 'size': '350 страниц'},
        {'name': '1984', 'author': 'Джордж Оруэлл', 'size': '328 страниц'},
        {'name': 'Война и мир', 'author': 'Лев Толстой', 'size': '1225 страниц'},
        {'name': 'Анна Каренина', 'author': 'Лев Толстой', 'size': '864 страницы'},
        {'name': 'Гарри Поттер и философский камень', 'author': 'Джоан Роулинг', 'size': '223 страницы'},
        {'name': 'Маленький принц', 'author': 'Антуан де Сент-Экзюпери', 'size': '96 страниц'},
        {'name': 'Три товарища', 'author': 'Эрих Мария Ремарк', 'size': '480 страниц'},
        {'name': 'Алхимик', 'author': 'Пауло Коэльо', 'size': '208 страниц'},
        {'name': 'Метро 2033', 'author': 'Дмитрий Глуховский', 'size': '416 страниц'}
        ]
    return render_template('laba2.html', name=name, number_labolatory=number_labolatory,number_course=number_course,group=group, 
                           fruits=fruits, books=books)

@app.route('/lab2/')
def lab2():
    return render_template('lab2.html')

@app.route('/lab2/cars')
def lab2_cars():
    return render_template('cars.html')