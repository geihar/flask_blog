from flask import Flask, render_template

app = Flask(__name__)
app.config['SECRET_KEY'] = 'you-will-never-guess'


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


if __name__ == '__main__':
    app.run(debug=True)
