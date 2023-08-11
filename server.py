from flask import Flask, render_template,url_for,redirect,request
import csv
app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')
    
@app.route('/contact.html')
def contact():
    return render_template('contact.html')

@app.route('/works.html')
def works():
    return render_template('works.html')

@app.route('/about.html')
def about():
    return render_template('about.html')

@app.route('/blog.html')
def blog():
    return render_template('blog.html')
@app.route('/resume.html')

def resume():
    return render_template('resume.html')


app.run(debug=True)

