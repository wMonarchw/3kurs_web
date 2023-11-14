from flask import Flask, redirect, url_for, render_template, Blueprint, request
from lab1 import lab1 
from lab2 import lab2
from lab3 import lab3
from lab4 import lab4
from lab5 import lab5

app = Flask(__name__)
app.register_blueprint(lab1)
app.register_blueprint(lab2)
app.register_blueprint(lab3)
app.register_blueprint(lab4)
app.register_blueprint(lab5)

