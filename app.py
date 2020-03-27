from flask import Flask, render_template, url_for
from mongoengine import *

connect('web3')


class Country(Document):
    Continent = StringField()
    CountryCode = StringField()



app = Flask(__name__,
        static_url_path='',
        template_folder='../Web3-Homepage/templates')


China = Country(Continent='Asia', CountryCode='CN')
China.save()
NewZealand = Country(Continent='Oceania',CountryCode='NZ' )
NewZealand.save()


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
