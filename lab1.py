from flask import Blueprint, redirect, url_for, render_template, Blueprint, request

lab1 = Blueprint('lab1', __name__)

@lab1.route('/')
@lab1.route('/index')
def start():
    return redirect('/menu', code=302)

@lab1.route('/menu')
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
            <li><a href='/lab3/'>Лабораторная 3</a></li>
            <li><a href='/lab4/'>Лабораторная 4</a></li>
            <li><a href='/lab5/'>Лабораторная 5</a></li>
            <li><a href='/lab6/'>Лабораторная 6</a></li>
            <li><a href='/lab7/'>Лабораторная 7</a></li>
            <li><a href='/lab8/'>Лабораторная 8</a></li>
            <li><a href='/lab9/'>Лабораторная 9</a></li>
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

@lab1.route('/lab1')
def lab():
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

@lab1.route('/oak')
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

@lab1.route('/lab1/student')
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

@lab1.route('/lab1/python')
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

@lab1.route('/lab1/choice')
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