from flask import Flask
from flask_bootstrap import Bootstrap
from flask_script import Manager
from flask_moment import Moment


app = Flask(__name__)
manager = Manager(app)
bootstrap = Bootstrap(app)
moment = Moment(app)


@app.route('/')
def index():
    return '<h1>Hello world!</h1>'


@app.route('/user/<name>')
def user(name):
    return '<h1>Hello, {}</h1>'.format(name)


if __name__ == '__main__':
    manager.run()
