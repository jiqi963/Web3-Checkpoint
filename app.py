from flask import Flask, render_template
from mongoengine import *
connect('web3')


app = Flask(__name__)

@app.route('/')
@app.route('/index')
@app.route('/home')
def index():
    index= "Index"
    return render_template('index.html', title=index)


@app.route('/pageone')
def  pageone():
    return render_template('pageone.html')    

@app.route('/pagetwo')
def pagetwo():
    return render_template('pagetwo.html')	
	
if __name__ == '__main__':
    app.run(debug=True)
