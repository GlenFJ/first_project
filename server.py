from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Glen is expert in Python development! amd awesome person amd the list goes on...'

@app.route('/blog')
def blog():
    return render_template('about.html')

@app.route('/blog/2020/dogs')
def blog2():
    return 'this is my dog...'