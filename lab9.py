from flask import Blueprint, redirect, url_for, render_template, request, session, abort
from datetime import datetime

lab9 = Blueprint('lab9', __name__)


@lab9.route('/lab9/')
def lab():
    return render_template('lab9/index.html')

@lab9.app_errorhandler(404)
def not_found(e):
    return 'Нет такой страницы', 404

@lab9.app_errorhandler(500)
def internal_error(e):
    return 'Ошибка', 500

@lab9.route('/lab9/500')
def error_500():
    abort(500)

@lab9.route('/lab9/greeting_card', methods=['GET', 'POST'])
def greeting_card():
    if request.method == 'POST':
        recipient_name = request.form.get('recipient_name')
        recipient_gender = request.form.get('recipient_gender')
        sender_name = request.form.get('sender_name')
        return render_template('lab9/greeting_card.html', recipient_name=recipient_name, recipient_gender=recipient_gender, sender_name=sender_name)
    else:
        recipient_name = request.args.get('recipient_name')
        recipient_gender = request.args.get('recipient_gender')
        sender_name = request.args.get('sender_name')
        return render_template('lab9/greeting_card.html', recipient_name=recipient_name, recipient_gender=recipient_gender, sender_name=sender_name)
