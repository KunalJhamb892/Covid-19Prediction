from flask import Flask, request, render_template
import jsonify
import requests
import pickle
import numpy as np
import sklearn
from sklearn.preprocessing import StandardScaler

app = Flask(__name__)
model = pickle.load(open('rf_model.pkl', 'rb'))
@app.route('/', methods=['GET'])
def Home():
    return render_template('index.html')


standard_to = StandardScaler()
@app.route('/prediction', methods=['GET', 'POST'])
def predict():
    if request.method == 'POST':
        Cough = request.form['cough']
        if(Cough == "Yes"):
            Cough = 1
        else:
            Cough = 0

        Fever = request.form['Fever']
        if(Fever == 'Yes'):
            Fever = 1
        else:
            Fever = 0
        
        SoreThroat = request.form['SoreThroat']
        if(SoreThroat == 'Yes'):
            SoreThroat = 1
        else:
            SoreThroat = 0

        Breathing = request.form['Breathing']
        if(Breathing == 'Yes'):
            Breathing = 1
        else:
            Breathing = 0

        HeadAche = request.form['headache']
        if(HeadAche == 'Yes'):
            HeadAche = 1
        else:
            HeadAche = 0

        Age = request.form['Age']
        if(Age == 'No record'):
            Age = 1
        elif(Age == 'Yes'):
            Age = 2
        else:
            Age = 0

        Gender = request.form['Gender']
        if(Gender == 'Male'):
            Gender = 2
        elif(Gender == 'Female'):
            Gender = 1
        else:
            Gender = 0

        Contact = request.form['Contact']
        if(Contact == 'Contact with confirmed'):
            Contact = 1
        elif(Contact == 'Abroad'):
            Contact = 0
        else:
            Contact = 2



        prediction = model.predict([[Cough, Fever, SoreThroat, Breathing, HeadAche, Age, Gender, Contact]])
        output = prediction[0]
        if(output == 0):
           return render_template('index.html',prediction_text = "Negative")
        elif(output == 1):
           return render_template('index.html', prediction_text = "Could not determine")
        else:
            return render_template('index.html', prediction_text = "Positive")

if __name__=="__main__":
    app.run(debug=True)
