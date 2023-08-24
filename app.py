#Importing the libraries
import pickle
from flask import Flask, render_template, request
#Global variables
app = Flask(__name__)
loadedModel = pickle.load(open('agriculture.pkl', 'rb')) 

    
#www.google.co.in/prediction

#Routes
@app.route('/')
def home():
    return render_template('index.html')


@app.route('/prediction', methods=['POST'])
def prediction():
    N = int(request.form['Nitrogen'])
    P = int(request.form['Phosphorous'])
    K = int(request.form['Pottasium'])
    temperature = int(request.form['Temperature'])
    humidity = int(request.form['Humidity'])
    ph = int(request.form['PH'])
    rainfall = int(request.form['Rainfall'])
    
    Suitable_Crop = loadedModel.predict([[N,P,K,temperature,humidity,ph,rainfall]])[0]

    return render_template('result.html', output=Suitable_Crop)

#Main function
if __name__ == '__main__':
    app.run(debug=True)