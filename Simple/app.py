from flask import Flask, render_template
from flask_cors import CORS

app = Flask(__name__, template_folder='Simple/templates')
# CORS(app)


@app.route('/')
def home():
    return 'Welcome'

@app.route('/1')
def f1():
    return render_template('1.html')


@app.route('/2')
def f2():
    return render_template('2.html')


@app.route('/data')
def data():
    return 'hii'


if __name__ == '__main__':
    app.run()
