from flask import Flask, render_template, url_for
from mongoengine import *

app.config.from_object('config')

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
    for file in op.listdir(app.config['FILES_FOLDER']):
        filename = op.fsdecode(file)
        path = os.path.join(app.config['FILES_FOLDER'],"data1.csv")
        f = open(path)
        r = csv.reader(f)
        d = list(r)
        for data in d
            print(data)
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

@app.route('/countries', methods=['GET','POST','PUT'])
@app.route('/countries/<CountryCode>', methods=['GET'])
def getCountry(CountryCode=None):
	countries=None
	if CountryCode is None:
		countries = Country.objects
	else:
		countries = Country.objects.get(CountryCode=CountryCode)
	return countries.to_json()

if __name__ == '__main__':
    app.run(host='0.0.0.0',debug=True, port=80)
