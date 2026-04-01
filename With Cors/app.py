from flask import Flask, render_template
from flask_cors import CORS
import os

app = Flask(__name__, template_folder='Simple/templates')
CORS(app)


@app.route('/')
def home():
    return 'Welcome'

@app.route('/page1')
def f1():
    return render_template('1.html')


@app.route('/page2')
def f2():
    return render_template('2.html')


@app.route('/data')
def data():
    return 'hii'


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 10000)))