from flask import Flask, redirect, url_for, render_template

app = Flask(__name__)

@app.route('/')
@app.route('/index')
def start():
    return redirect('/menu', code=302)

@app.route('/menu')
def menu():
    return '''
<!DOCTYPE html>
<html lang="ru">
    <head>
        <title>НГТУ, ФБ, Лабораторные работы</title>
        <link rel="stylesheet" href="''' + url_for('static', filename='lab1.css') + '''">
    </head>
    <body>
        <header>
            НГТУ,ФБ, WEB-программирование, часть 2. Список лабораторных
        </header>
        <div id='labs'>
            <li><a href='/lab1'>Лабораторная 1</a></li>
            <li><a href='/lab2/'>Лабораторная 2</a></li>
        </div>
        <div id='rout'>
            <h1>Реализованные Роуты</h1>
            <ol>
                <li><a href='/oak'>Dub</a></li>
                <li><a href='/lab1/student'>Student</a></li>
                <li><a href='/lab1/python'>Python</a></li>
                <li><a href='/lab1/choice'>Choice</a></li>
            </ol>
        </div>
        <footer>
            &copy; Завгородний Илья Артурович, ФБИ-14, 3 курс, 2023
        </footer>
    </body>
</html>
'''

@app.route('/lab1')
def lab1():
    return '''
<!DOCTYPE html>
<html lang="ru">
    <head>
        <title>Завгородний Илья Артурович, Лабораторная 1</title>
        <link rel="stylesheet" href="''' + url_for('static', filename='lab1.css') + '''">
    </head>
    <body>
        <header>
            Нгту, ФБ, Лабораторная 1
        </header>
        <h1>WEB-сервер на flask</h1>
        <div>
            Flask — фреймворк для создания веб-приложений на языке
            программирования Python, использующий набор инструментов
            Werkzeug, а также шаблонизатор Jinja2. Относится к категории так
            называемых микрофреймворков — минималистичных каркасов

            веб-приложений, сознательно предоставляющих лишь самые ба-
            зовые возможности.
        </div>
        <div>
            <h1>Ссыллка на меню</h1>
            <li><a href='/menu'>Меню</a></li>
        </div>
        <footer>
            &copy; Завгородний Илья Артурович, ФБИ-14, 3 курс, 2023
        </footer>
    </body>
</html>
'''

@app.route('/oak')
def oak():
    return '''
<!DOCTYPE html>
<html lang="ru">
    <head>
        <title>Завгородний Илья Артурович, Лабораторная 1</title>
        <link rel="stylesheet" href="''' + url_for('static', filename='lab1.css') + '''">
    </head>
    <body>
        <h1>DUB</h1>
        <img src="''' + url_for('static', filename='oak.jpg') + '''">
    </body>
</html>
'''

@app.route('/lab1/student')
def student():
    return '''
<!DOCTYPE html>
<html lang="ru">
    <head>
        <title>Завгородний Илья Артурович, Лабораторная 1</title>
        <link rel="stylesheet" href="''' + url_for('static', filename='lab1.css') + '''">
    </head>
    <body>
        <h1>НГТУ</h1>
        <div>Завгородний Илья Артурович</div>
        <img id='ngtu' src="''' + url_for('static', filename='ngtu.png') + '''">
    </body>
</html>
'''

@app.route('/lab1/python')
def python():
    return '''
<!DOCTYPE html>
<html lang="ru">
    <head>
        <title>Завгородний Илья Артурович, Лабораторная 1</title>
        <link rel="stylesheet" href="''' + url_for('static', filename='lab1.css') + '''">
    </head>
    <body>
        <div id='python'>
            Python (МФА: [ˈpʌɪθ(ə)n]; в русском языке встречаются названия пито́н[23] или па́йтон[24]) — 
            высокоуровневый язык программирования общего назначения с динамической строгой типизацией и автоматическим управлением памятью[25][26], 
            ориентированный на повышение производительности разработчика, читаемости кода и его качества, а также на обеспечение переносимости написанных на нём 
            программ[27]. Язык является полностью объектно-ориентированным в том плане, что всё является объектами[25]. Необычной особенностью языка является выделение 
            блоков кода пробельными отступами[28]. Синтаксис ядра языка минималистичен, за счёт чего на практике редко возникает необходимость обращаться к документации[27]. 
            Сам же язык известен как интерпретируемый и используется в том числе для написания скриптов[25]. Недостатками языка являются зачастую более низкая скорость работы и 
            более высокое потребление памяти написанных на нём программ по сравнению с аналогичным кодом, написанным на компилируемых языках, таких как C или C++[25][27].
        </div>
    </body>
</html>
'''

@app.route('/lab1/choice')
def choice():
    return '''
<!DOCTYPE html>
<html lang="ru">
    <head>
        <title>Завгородний Илья Артурович, Лабораторная 1</title>
        <link rel="stylesheet" href="''' + url_for('static', filename='lab1.css') + '''">
    </head>
    <body>
        <div id='data'>
            Наука о данных (англ. data science; иногда даталогия — datalogy[1]) — 
            раздел информатики, изучающий проблемы анализа, обработки и представления данных в цифровой форме. 
            Объединяет методы по обработке данных в условиях больших объёмов и 
            высокого уровня параллелизма, статистические методы, методы интеллектуального анализа данных и приложения 
            искусственного интеллекта для работы с данными, а также методы проектирования и разработки баз данных.
            Рассматривается как академическая дисциплина[2], а с начала 2010-х годов, 
            во многом благодаря популяризации концепции «больших данных»[3], — и как практическая межотраслевая сфера деятельности,
            притом специализация исследователя данных (англ. data scientist — «учёного по данным») с начала 2010-х годов считается одной из самых 
            привлекательных, высокооплачиваемых и перспективных профессий[4][5].
        </div>
        <img src="''' + url_for('static', filename='oak.jpg') + '''">
    </body>
</html>
'''

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