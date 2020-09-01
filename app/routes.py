from flask import Flask, render_template, redirect, flash, url_for

from app import app
from .forms import LoginForm


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


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash(f'Login requested for user {form.username.data}, remember_me={form.remember_me.data}')
        return redirect(url_for('index'))
    return render_template('login.html', title='Sign In', form=form)