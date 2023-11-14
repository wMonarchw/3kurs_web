from flask import Blueprint, redirect, url_for, render_template, Blueprint, request, session
import psycopg2
lab5 = Blueprint('lab5', __name__)

def dbConnect():
    conn = psycopg2.connect(
        host = '127.0.0.1',
        database='knowledge_base_for_zavgorodniy',
        user = 'zavgorodniy_knowledge_base',
        password = '123')    
    return conn

def dbClose(cursor, connection):
    cursor.close()
    connection.close()


@lab5.route('/lab5/')
def lab():
    username = session.get('username')
    return render_template('lab5.html', username=username)


@lab5.route('/lab5/users')
def users():
    conn = psycopg2.connect(
        host = '127.0.0.1',
        database='knowledge_base_for_zavgorodniy',
        user = 'zavgorodniy_knowledge_base',
        password = '123')
    cur = conn.cursor()

    cur.execute('SELECT * FROM public.users;')

    users = cur.fetchall()

    cur.close()
    conn.close()
    user0 = users[0][1]
    user1 = users[1][1]
    user2 = users[2][1]
    user3 = users[3][1]
    return render_template("users.html", user0=user0, user1=user1, user2=user2, user3=user3)

@lab5.route('/lab5/register', methods = ['GET', 'POST'])
def registerPage():
    errors = []

    if request.method == "GET":
        return render_template('register.html', errors=errors)

    username = request.form.get("username")
    password = request.form.get("password")


    if not (username or password):
        errors.append("Пожалуйста заполните все поля")
        print(errors)
        return render_template('register.html', errors=errors)
    if username == '':
        errors.append("Пожалуйста заполните все поля")
        print(errors)
        return render_template('register.html', errors=errors)
    if password == '':
        errors.append("Пожалуйста заполните все поля")
        print(errors)
        return render_template('register.html', errors=errors)

    conn = dbConnect()
    cur = conn.cursor()

    cur.execute(f"SELECT username FROM users WHERE username = '{username}';")

    if cur.fetchone() is not None:
        errors.append("Пользователь с данным именем уже существует")

        dbClose(cur, conn)
        return render_template('register.html', errors=errors)

    cur.execute(f"INSERT INTO users (username, password) VALUES ('{username}', '{password}');")

    conn.commit()
    dbClose(cur, conn)
    return redirect("/lab5/users")