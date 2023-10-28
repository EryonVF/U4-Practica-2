from flask import Flask

app = Flask(__name__)

@app.route('/welcome/<name>/<ncontrol>')
def hello(name,ncontrol):
    return f'Bienvenido ' + name + ncontrol
