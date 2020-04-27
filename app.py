from flask import Flask, render_template, url_for
from mongoengine import *

connect('web3')

class Country(Document):
    CountryID = StringField()
    Continent = StringField()
    CountryCode = StringField()

app = Flask(__name__)



@app.route('/')
@app.route('/index')
@app.route('/home')
def index():
    index= "Index"
    return render_template('index.html', title=index)

@app.route('/pageone')
def pageone():
    return render_template('pageone.html')    

@app.route('/pagetwo')
def pagetwo():
    return render_template('pagetwo.html')	


@app.route('/createdata')
def create():

	China = Country(CountryID='1',Continent='Asia', CountryCode='CN')
	China.save(force_insert=False)
	NewZealand = Country(CountryID='2',Continent='Oceania',CountryCode='NZ' )
	NewZealand.save(force_insert=True)

	return render_template('index.html')
@app.route('/deletedata')
def delete():

	db.country.drop()
	return render_template('index.html')

# API part
@app.route('/countries', methods=['GET','POST','PUT'])
@app.route('/countries/<CountryCode>', methods=['GET'])
def getCountry(CountryCode=None):
	countries=None
	if CountryCode is None:
		countries = Country.objects
	else:
		countries = Country.objects.get(CountryCode=CountryCode)
	return countries.to_json()

#	except Exception as e:
#		return render_template('pagetwo.html',error=error)

if __name__ == '__main__':
    app.run(host='0.0.0.0',debug=True, port=80)
