from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/board')
def board():
    return 'board'


if __name__ == '__main__':
    app.run(debug=True)