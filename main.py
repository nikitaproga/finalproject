#Импорт
from flask import Flask, render_template, request

app = Flask(__name__)

#Первая страница
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/ecology_1')
def ecology_1():
    return render_template('ecology_1.html')

@app.route('/ecology_2')
def ecology_2():
    return render_template('ecology_2.html')

@app.route('/ecology_3')
def ecology_3():
    return render_template('ecology_3.html')

app.run(debug=True)