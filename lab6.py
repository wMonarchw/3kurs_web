from flask import Blueprint, redirect, url_for, render_template, request, session
from Db import db

from Db.models import users, articles
from werkzeug.security import check_password_hash, generate_password_hash
from flask_login import login_user, login_required, current_user, logout_user

lab6 = Blueprint('lab6', __name__)


@lab6.route('/lab6/')
def lab():
    username_form = request.form.get('username')
    return render_template('lab6.html', username_form=username_form)

@lab6.route('/lab6/check')
def main():
    my_users = users.query.all()
    print(my_users)
    return 'console'

@lab6.route('/lab6/checkarticles')
def checkarticles():
    my_articles = articles.query.all()
    print(my_articles)
    return 'console'


@lab6.route('/lab6/register', methods = ['GET', 'POST'])
def register():
    errors = []
    if request.method == 'GET':
        return render_template('register6.html')
    
    username_form = request.form.get('username')
    password_form = request.form.get('password')

    isUserExist = users.query.filter_by(username=username_form).first()
    if isUserExist is not None:
        errors.append("Пользователь уже существует")
        return render_template('register6.html', errors=errors)   

    if not (username_form or password_form):
        errors.append("Пожалуйста заполните все поля")
        print(errors)
        return render_template('register6.html', errors=errors)
    if username_form == '':
        errors.append("Пожалуйста заполните все поля")
        print(errors)
        return render_template('register6.html', errors=errors)
    if password_form == '':
        errors.append("Пожалуйста заполните все поля")
        print(errors)
        return render_template('register6.html', errors=errors)
        
       
    

    hashPassword = generate_password_hash(password_form, method='pbkdf2')
    newUser = users(username=username_form, password=hashPassword)

    db.session.add(newUser)
    db.session.commit()

    return redirect('/lab6/login')


@lab6.route('/lab6/login', methods = ['GET', 'POST'])
def login():
    errors = []
    if request.method == 'GET':
        return render_template('login6.html')

    username_form = request.form.get('username')
    password_form = request.form.get('password')

    my_user = users.query.filter_by(username=username_form).first()

    if my_user is not None:
        if check_password_hash(my_user.password, password_form):
            login_user(my_user, remember = False)
            return redirect('/lab6/articles')
        else: 
            errors.append("Неправильный пароль")
            return render_template('login6.html', errors=errors)
        
    if not (username_form or password_form):
        errors.append("Пожалуйста заполните все поля")
        return render_template("login6.html", errors=errors)
    if username_form == '':
        errors.append("Пожалуйста заполните все поля")
        print(errors)
        return render_template('login6.html', errors=errors)
    if password_form == '':
        errors.append("Пожалуйста заполните все поля")
        print(errors)
        return render_template('login6.html', errors=errors)
    
    else: 
        errors.append('Пользователя не существует')
        return render_template('login6.html', errors=errors)

    return render_template('login6.html')


@lab6.route('/lab6/articles', methods = ['GET', 'POST'])
@login_required
def view_articles():
    username_form = request.form.get('username')
    my_articles = articles.query.filter((articles.user_id == current_user.id) | (articles.is_public == True)).order_by(articles.is_favorite.desc()).all()
    print(my_articles)
    return render_template('articles6.html', articles=my_articles, username_form = username_form)


@lab6.route("/lab6/newtitle", methods=["GET", "POST"])
@login_required
def createArticle():
    if request.method == "GET":
        return render_template("newtitle.html")

    article_text = request.form.get("article_text")
    title = request.form.get("article_title")
    option = request.form.get("usl")

    if len(article_text) == 0:
        errors = ["Заполните текст"]
        return render_template("new_article.html", errors=errors)

    new_article = articles(user_id=current_user.id, title=title, article_text=article_text)
    
    if option == 'yes':
        new_article.is_public = True
    else:
        new_article.is_public = False

    db.session.add(new_article)
    db.session.commit()

    return redirect("/lab6/articles")


@lab6.route("/lab6/articles/<int:article_id>", methods=['GET', 'POST'])
def getArticle(article_id):
    if current_user.is_authenticated:
        if request.method == 'POST':
            favorite = request.form.get('favorite')
            likes = request.form.get('likes')

            article = articles.query.filter_by(id=article_id).first()


            if likes == 'Лайк':
                if article.likes is None:
                    article.likes = 0
                else:
                    article.likes += 1

            if favorite == 'yes':
                article.is_favorite = True
            else:
                article.is_favorite = False

            db.session.commit()

        article = articles.query.filter_by(id=article_id).first()

        if article:
            if article.user_id == current_user.id or article.is_public:
                text = article.article_text.splitlines()
                likes_count = article.likes
                return render_template("6articleN.html", article_text=text, article_title=article.title, username=current_user.username, favorite=article.is_favorite, likes_count=likes_count)
            else:
                return "У вас нет доступа к этой статье"
        else:
            return "Статья не найдена"
    else:
        return "Пожалуйста, войдите, чтобы увидеть эту статью"

@lab6.route('/lab6/logout')
@login_required
def logout():
    logout_user()
    return redirect('/lab6')
