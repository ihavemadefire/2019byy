from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/home')
def index():
    return render_template('home.html')

@app.route('/blog')
def index():
    return render_template('blog.html')

@app.route('/goals')
def index():
    return render_template('goals.html')

@app.route('/about')
    def index():
        return render_template('about.html')
