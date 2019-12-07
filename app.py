from flask import Flask

app = Flask(__name__)
app.debug = True

@app.route('/')
def index():
    return 'Hello, World!'

@app.route('/about')
def about():
    return 'This is the worst!'