from flask import Flask
from flask import url_for
from flask import render_template


app=Flask(__name__)

@app.route('/')
def index():
    # template_name = 
    return render_template('index.html')

@app.route('/about/us')
def about():
    return '<h1>О нас</h1>'

@app.route('/post/<int:id>')
def post(id):
    return f'<h1>Пост {id} </h1>'



with app.test_request_context():
    print(url_for('index'))
    print(url_for('about'))
    print(url_for('post', id=3))