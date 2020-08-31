from flask import Flask, render_template

from config import Config
from app.forms import LoginForm

app = Flask(__name__)
app.config.from_object(Config)


@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'Dima'}
    posts = [
        {
            'author': {'username': 'Alex'},
            'body': 'Beautiful day in Portland!'
        },
        {
            'author': {'username': 'Sam'},
            'body': 'The Avengers movie was so cool!'
        },
        {
            'author': {'username': 'Tom'},
            'body': 'Lorem ipsum dolor sit amet, consectetur adipisicing elit. Esse, tempore!'
        }
    ]
    return render_template('index.html', title='Home', user=user, posts=posts)


@app.route('/login')
def login():
    form = LoginForm()
    return render_template('login.html', title='Sign In', form=form)


if __name__ == '__main__':
    app.run(debug=True)
