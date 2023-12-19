from flask import Blueprint, redirect, url_for, render_template, request, session


lab8 = Blueprint('lab8', __name__)


@lab8.route('/lab8/')
def lab():
    return render_template('lab8/index.html')

courses = [
    {"name": "C++", "videos": 3, "price": 3000},
    {"name": "basic", "videos": 30, "price": 0},
    {"name": "C#", "videos": 8}

]

@lab8.route('/lab8/api/courses', methods=['GET'])
def get_courses():
    return courses

@lab8.route('/lab8/api/courses/<int:course_num>', methods=['GET'])
def get_course(course_num):
    return courses[course_num]

@lab8.route('/lab8/api/courses/<int:course_num>', methods=['DELETE'])
def del_course(course_num):
    del courses[course_num]
    return '', 204