from flask import Blueprint, redirect, url_for, render_template, request, session


lab8 = Blueprint('lab8', __name__)


@lab8.route('/lab8/')
def lab():
    return render_template('lab8/index.html')