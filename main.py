from flask import Flask, render_template, request
import jsonify
import requests
import pickle
import numpy as np
import sklearn
from sklearn.preprocessing import StandardScaler
app = Flask(__name__)
model = pickle.load(open('qda_model.pkl', 'rb'))
@app.route('/',methods=['GET'])
def Home():
    return render_template('index.html')


standard_to = StandardScaler()
@app.route("/predict", methods=['POST'])
def predict():
    # Fuel_Type_Diesel=0
    if request.method == 'POST':
        Fever = request.form['Fever']
        if(Fever == 'Yes'):
            Fever = 1
        else:
            Fever = 0

        Tiredness = request.form['Tiredness']
        if(Tiredness == 'Yes'):
            Tiredness = 1
        else:
            Tiredness = 0

        Cough = request.form['Cough']
        if(Cough == 'Yes'):
            Cough = 1
        else:
            Cough = 0

        Breathing = request.form['Breathing']
        if(Breathing == 'Yes'):
            Breathing = 1
        else:
            Breathing = 0

        SoreThroat = request.form['SoreThroat']
        if(SoreThroat == 'Yes'):
            SoreThroat = 1
        else:
            SoreThroat = 0

        NoSymp = request.form['NoSymp']
        if(NoSymp == 'Yes'):
            NoSymp = 1
        else:
            NoSymp = 0

        Pain = request.form['Pain']
        if(Pain == 'Yes'):
            Pain = 1
        else:
            Pain = 0

        Nasal = request.form['Nasal']
        if(Nasal == 'Yes'):
            Nasal = 1
        else:
            Nasal = 0

        Runny = request.form['Runny']
        if(Runny == 'Yes'):
            Runny = 1
        else:
            Runny = 0

        Diarrhea = request.form['Diarrhea']
        if(Diarrhea == 'Yes'):
            Diarrhea = 1
        else:
            Diarrhea = 0

        NoneExp = request.form['NoneExp']
        if(NoneExp == 'Yes'):
            NoneExp = 0
        else:
            NoneExp = 1

        Age = request.form['Age']
        if(Age == '0-9'):
            Age_0 = 1
            Age_10 = 0
            Age_20 = 0
            Age_25 = 0
            Age_60 = 0
        elif(Age == '10-19'):
            Age_0 = 0
            Age_10 = 1
            Age_20 = 0
            Age_25 = 0
            Age_60 = 0
        elif(Age == '20-24'):
            Age_0 = 0
            Age_10 = 0
            Age_20 = 1
            Age_25 = 0
            Age_60 = 0
        elif(Age == '25-59'):
            Age_0 = 0
            Age_10 = 0
            Age_20 = 0
            Age_25 = 1
            Age_60 = 0
        else:
            Age_0 = 0
            Age_10 = 0
            Age_20 = 0
            Age_25 = 0
            Age_60 = 1

        Gender = request.form['Gender']
        if(Gender == 'Male'):
            Gender_Male = 1
            Gender_Female = 0
            Gender_TransGender = 0
        elif(Gender == 'Female'):
            Gender_Male = 0
            Gender_Female = 1
            Gender_TransGender = 0
        else:
            Gender_Male = 0
            Gender_Female = 0
            Gender_TransGender = 1

        Contact = request.form['Contact']
        if(Contact == 'Yes'):
            Contact_Yes = 1
            Contact_No = 0
            Contact_DontKnow = 0
        elif(Contact == 'No'):
            Contact_Yes = 0
            Contact_No = 1
            Contact_DontKnow = 0
        else:
            Contact_Yes = 0
            Contact_No = 0
            Contact_DontKnow = 1



        prediction = model.predict([[Fever, Tiredness, Cough, Breathing, SoreThroat, NoSymp, Pain, Nasal, Runny, Diarrhea, NoneExp, Age_0, Age_10, Age_20, Age_25, Age_60, Gender_Female, Gender_Male, Gender_TransGender, Contact_DontKnow, Contact_No, Contact_Yes]])
        output = round(prediction[0],2)
        if output < 0:
            return render_template('index.html',prediction_text = "Sorry you cannot sell this car")
        else:
            return render_template('index.html',prediction_text = "You Can Sell The Car at {}".format(output))
    else:
        return render_template('index.html')

if __name__=="__main__":
    app.run(debug=True)
