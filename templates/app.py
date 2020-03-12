from flask import Flask, render_templates
from mongoengine import *
connect('web3')


app = Flask(__name__)

@app.route('/')
@app.route('/index')
@app.route('/home')
def index():
    index= "Index"
    return render_templates('index.html', title=index)


@app.route('/1.1')
def  1.1():
    return render_templates('1.1.html')    

@app.route('/1.2')
def 1.2():
    return render_templates('1.2.html')	
	
if __name__ == '__main__':
    app.run(debug=True)