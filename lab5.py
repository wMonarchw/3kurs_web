from flask import Blueprint, redirect, url_for, render_template, Blueprint, request, session
import psycopg2
from werkzeug.security import check_password_hash, generate_password_hash


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
    user_list = [user[1] for user in users]
    return render_template("users.html", user_list=user_list)

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
    
    hashPassword = generate_password_hash(password)

    conn = dbConnect()
    cur = conn.cursor()

    cur.execute("SELECT username FROM users WHERE username = %s;", (username,))

    if cur.fetchone() is not None:
        errors.append("Пользователь с данным именем уже существует")

        conn.close()
        cur.close()
        return render_template('register.html', errors=errors)
    
    cur.execute("INSERT INTO users (username, password) VALUES (%s, %s);", (username, hashPassword))
    
    conn.commit()
    conn.close()
    cur.close()
    return redirect("/lab5/login5")

@lab5.route('/lab5/login5', methods=["GET", "POST"])
def login5():
    errors = []

    if request.method == "GET":
        return render_template("login5.html", errors=errors)
    
    username = request.form.get("username")
    password = request.form.get("password")

    if not (username or password):
        errors.append("Пожалуйста заполните все поля")
        return render_template("login5.html", errors=errors)
    if username == '':
        errors.append("Пожалуйста заполните все поля")
        print(errors)
        return render_template('login5.html', errors=errors)
    if password == '':
        errors.append("Пожалуйста заполните все поля")
        print(errors)
        return render_template('login5.html', errors=errors)
    
    conn = dbConnect()
    cur = conn.cursor()

    cur.execute("SELECT id, password FROM users WHERE username = %s;", (username,))

    result = cur.fetchone()

    if result is None:
        errors.append("Неправильный логин или пароль")
        dbClose(cur, conn)
        return render_template("login5.html", errors=errors)
    
    userID, hashPassword = result

    if check_password_hash(hashPassword, password):
        session['id'] = userID
        session['username'] = username
        dbClose(cur, conn)
        return redirect("/lab5/")
    
    else:
        errors.append('Неправильный логин пароль')
        return render_template('login5.html', errors=errors)
    



@lab5.route("/lab5/newtitle", methods = ["GET", "POST"])
def createArticle():
    errors = []

    userID = session.get('id')
    username = session.get('username')
    option = request.form.get('usl')

    if userID is not None:
        if request.method =="GET":
            return render_template("newtitle.html", username=username, option=option)
        
        if request.method == "POST":
            article_text = request.form.get("article_text")
            title = request.form.get("article_title")

            if len(article_text)==0:
                errors.append("Заполните текст")
                return render_template("new_article", errors = errors, username=username, option=option)
            
            conn = dbConnect()
            cur = conn.cursor()

            if option == 'yes':
                cur.execute("INSERT INTO articles (user_id, title, article_text, is_public) VALUES (%s, %s, %s, TRUE) RETURNING id;", (userID, title, article_text))
            else:
                cur.execute("INSERT INTO articles (user_id, title, article_text) VALUES (%s, %s, %s) RETURNING id;", (userID, title, article_text))

            new_articl_id = cur.fetchone()[0]
            conn.commit()

            dbClose(cur, conn)

            return redirect(f"/lab5/articles/{new_articl_id}")

    return redirect("/lab5/login5")


@lab5.route("/lab5/articles/<int:article_id>", methods=['GET', 'POST'])
def getArticle(article_id):
    userID = session.get('id')

    favorite = request.form.get('favorite')
    likes = request.form.get('likes')
    if userID is not None:
        likes = request.form.get('likes')
        if request.method == 'POST':
            favorite = request.form.get('favorite')
            conn = dbConnect()
            cur = conn.cursor()

            if likes == 'Лайк':
                cur.execute("UPDATE articles SET likes = COALESCE(likes, 0) + 1 WHERE id = %s AND user_id = %s", (article_id, userID))

            if favorite == 'yes':
                cur.execute("UPDATE articles SET is_favorite = %s WHERE id = %s AND user_id = %s", ('True', article_id, userID))
            else:
                cur.execute("UPDATE articles SET is_favorite = %s WHERE id = %s AND user_id = %s", ('False', article_id, userID))

            
            conn.commit()
            dbClose(cur, conn)
        


        conn = dbConnect()
        cur = conn.cursor()
        cur.execute("SELECT title, article_text, likes FROM articles WHERE id = %s AND user_id = %s", (article_id, userID))
        articleBody = cur.fetchone()

        dbClose(cur, conn)

        if articleBody is None:
            return "Not found!"
            
        text = articleBody[1].splitlines()
        likes_count = articleBody[2]
    
        return render_template("articleN.html", article_text=text, article_title=articleBody[0], username=session.get("username"), favorite=favorite, likes=likes, likes_count=likes_count)




@lab5.route('/lab5/articles')
def list_articles():
    userID = session.get('id')
    username = session.get("username")
    
    if userID is not None:
        conn = dbConnect()
        cur = conn.cursor()
        
        cur.execute("SELECT id, title, is_favorite, is_public FROM articles WHERE user_id = %s OR is_public = True ORDER BY is_favorite DESC;", (userID,))
        articles_data = cur.fetchall()
        
        articles = [{'id': row[0], 'title': row[1], 'is_favorite': row[2]} for row in articles_data]

        dbClose(cur, conn)  

        return render_template('articles.html', articles=articles, username=username)

    return redirect("/lab5/login5")


@lab5.route('/lab5/logout')
def logout():
    session.clear()
    return render_template('lab5.html')

