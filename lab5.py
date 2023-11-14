from flask import Blueprint, redirect, url_for, render_template, Blueprint, request
import psycopg2
lab5 = Blueprint('lab5', __name__)

@lab5.route('/lab5/')
def lab():
    conn = psycopg2.connect(
        host = '127.0.0.1',
        database='knowledge_base_for_zavgorodniy',
        user = 'zavgorodniy_knowledge_base',
        password = '123')
    cur = conn.cursor()

    cur.execute('SELECT * FROM public.users;')

    result = cur.fetchall()

    cur.close()
    conn.close()

    print(result)
    return ('go console')

@lab5.route('/lab5/users')
def users():
    conn = psycopg2.connect(
        host = '127.0.0.1',
        database='knowledge_base',
        user = 'admin_knowledge_base',
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