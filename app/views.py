from app import app
from flask import render_template, flash, redirect
from flask import render_template

from .forms import LoginForm



@app.route('/')
def index():
    user = { 'nickname': 'Miguel' } 
    posts = [
        { 
            'author': { 'nickname': 'John' }, 
            'body': 'Beautiful day in Portland!' 
        },
        { 
            'author': { 'nickname': 'Susan' }, 
            'body': 'The Avengers movie was so cool!' 
        }
    ]
    context = {
        'title':'Home',
        'user':user,
        'posts':posts
    }
    return render_template('index.html', **context)

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        username = form.username.data
        password = form.password.data
        # здесь можно выполнить каку    ю-то проверку имени пользователя и пароля
        return f'Hello, {username}!'
    context={
        'form':form,
        'title':'Login'
    }
    return render_template('login.html', **context)


# with app.test_request_context():
#     print(url_for('index'))
#     print(url_for('about'))
#     print(url_for('post', id=3))