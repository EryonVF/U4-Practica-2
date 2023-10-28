from flask import Flask

app = Flask(__name__)

@app.route('/welcome/<name>')
def hello(name):
    return 'Bienvenido ' + name
