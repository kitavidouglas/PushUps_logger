from flask import Blueprint, render_template, url_for, request, redirect

auth = Blueprint('auth', __name__)

@auth.route('/signup', methods=['GET'])
def signup():
    return render_template('signup.html')

@auth.route('/signup', methods=['POST'], endpoint='signup_post')
def signup_post():
    email = request.form.get('email')
    name = request.form.get('name')
    password = request.form.get('password')

    print(email, name, password)
    
    return redirect(url_for('auth.login'))



@auth.route('/login')
def login():
    return render_template('login.html')

@auth.route('/login', methods=['POST'], endpoint='login_post')
def login_post():
    email = request.form.get('email')
    name = request.form.get('name')
    password = request.form.get('password')

    print(email, name, password)
    
    return redirect(url_for('auth.login'))