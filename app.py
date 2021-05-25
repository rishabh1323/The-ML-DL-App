# Importing Required Libraries and Modules
import os
import base64
import pickle
import shutil
import requests
import datetime
import warnings
import numpy as np
import tensorflow as tf
from url_dict import url_dict
from tensorflow.keras.preprocessing import image
from flask import Flask, render_template, redirect, url_for, request

warnings.filterwarnings('ignore')

# Instantiating the Flask App
app = Flask(__name__)

#################################
##### Routes for Root Pages #####
#################################

# Home Page
@app.route("/", methods=['GET'])
@app.route("/home", methods=['GET'])
def home():
    return render_template("home.html")

# About Page
@app.route("/about", methods=['GET'])
def about():
    return render_template("about.html")

# Machine Learning Page
@app.route("/machine-learning", methods=['GET'])
def machine_learning():
    return render_template("machine_learning.html")

# Deep Learning Page
@app.route("/deep-learning", methods=['GET'])
def deep_learning():
    return render_template("deep_learning.html")

# House Price Prediction Page
@app.route("/house-price-prediction", methods=['GET', 'POST'])
def house_price_prediction():    
    return render_template("predict/house_price_prediction.html", data_dict=url_dict['1'])

# Bank Note Authentication Page
@app.route("/bank-note-authentication", methods=['GET', 'POST'])
def bank_note_authentication():
    return render_template("predict/bank_note_authentication.html", data_dict=url_dict['4'])

# Car Resale Value Page
@app.route("/car-resale-value", methods=['GET', 'POST'])
def car_resale_value():
    return render_template("predict/car_resale_value.html", data_dict=url_dict['5'])

# Digit Recognition Page
@app.route("/digit-recognition", methods=['GET', 'POST'])
def digit_recognition():
    return render_template("predict/digit_recognition.html", data_dict=url_dict['2'])

# Rock Paper Scissors Page
@app.route("/rock-paper-scissors", methods=['GET', 'POST'])
def rock_paper_scissors():
    return render_template("predict/rock_paper_scissors.html", data_dict=url_dict['3'])

#################################
##### Routes for Prediction #####
#################################

# House Price Prediction
@app.route("/house-price-prediction/predict", methods=['GET', 'POST'])
def house_price_prediction_predict():
    if request.method == 'POST':
        models = pickle.load(open('saved_models/house_price_prediction/models.pkl', 'rb'))
        minmax_scaler = pickle.load(open('saved_models/house_price_prediction/minmax_scaler.pkl', 'rb'))
        label_encoder_dict = pickle.load(open('saved_models/house_price_prediction/label_encoders.pkl', 'rb'))

        GrLivArea = np.log(float(request.form['GrLivArea']))
        stFlrSF = np.log(float(request.form['1stFlrSF']))
        YearRemodAdd = int(request.form['YrSold']) - int(request.form['YearRemodAdd'])
        MSZoning = request.form['MSZoning']
        PavedDrive = request.form['PavedDrive']
        BldgType = request.form['BldgType']
        Fireplaces = int(request.form['Fireplaces'])
        KitchenQual = request.form['KitchenQual']
        GarageType = request.form['GarageType']
        GarageFinish = request.form['GarageFinish']
        GarageCars = int(request.form['GarageCars'])
        CentralAir = request.form['CentralAir']
        BsmtFullBath = int(request.form['BsmtFullBath'])
        BsmtExposure = request.form['BsmtExposure']
        BsmtFinType1 = request.form['BsmtFinType1']
        BsmtQual = request.form['BsmtQual']
        HeatingQC = request.form['HeatingQC']
        ExterQual = request.form['ExterQual']
        LotShape = request.form['LotShape']
        OverallQual = int(request.form['OverallQual'])
        Algorithm = request.form['Algorithm']

        if MSZoning == 'C (all)':
            MSZoning = 'Rare_Var'
        if LotShape == 'IR3':
            LotShape = 'Rare_Var'
        if ExterQual == 'Fa':
            ExterQual = 'Rare_Var'
        if HeatingQC == 'Po':
            HeatingQC = 'Rare_Var'
        if GarageType == 'CarPort' or GarageType == '2Types':
            GarageType = 'Rare_Var'
        
        MSZoning = label_encoder_dict['MSZoning'].transform([MSZoning])[0]
        LotShape = label_encoder_dict['LotShape'].transform([LotShape])[0]
        BldgType = label_encoder_dict['BldgType'].transform([BldgType])[0]
        ExterQual = label_encoder_dict['ExterQual'].transform([ExterQual])[0]
        BsmtQual = label_encoder_dict['BsmtQual'].transform([BsmtQual])[0]
        BsmtExposure = label_encoder_dict['BsmtExposure'].transform([BsmtExposure])[0]
        BsmtFinType1 = label_encoder_dict['BsmtFinType1'].transform([BsmtFinType1])[0]
        HeatingQC = label_encoder_dict['HeatingQC'].transform([HeatingQC])[0]
        CentralAir = label_encoder_dict['CentralAir'].transform([CentralAir])[0]
        KitchenQual = label_encoder_dict['KitchenQual'].transform([KitchenQual])[0]
        GarageType = label_encoder_dict['GarageType'].transform([GarageType])[0]
        GarageFinish = label_encoder_dict['GarageFinish'].transform([GarageFinish])[0]
        PavedDrive = label_encoder_dict['PavedDrive'].transform([PavedDrive])[0]
        
        X_test = [[MSZoning, LotShape, BldgType, OverallQual, YearRemodAdd, ExterQual, BsmtQual, BsmtExposure, 
                   BsmtFinType1, HeatingQC, CentralAir , stFlrSF, GrLivArea, BsmtFullBath, KitchenQual, Fireplaces, 
                   GarageType, GarageFinish, GarageCars, PavedDrive]]

        X_test = minmax_scaler.transform(X_test)  

        if Algorithm == 'linear_regressor':
            prediction = models[0].predict(X_test)[0]
        elif Algorithm == 'support_vector_regressor':
            prediction = models[1].predict(X_test)[0]
        elif Algorithm == 'random_forest_regressor':
            prediction = models[2].predict(X_test)[0]
        else:
            prediction = models[3].predict(X_test)[0]
        
        prediction_text = "The estimated price of the house is ${}".format(int(np.exp(prediction)))
        return render_template("predict/house_price_prediction.html", data_dict=url_dict['1'],
                                prediction_text=prediction_text, scroll='OutputPredictionText')
    return redirect(url_for('house_price_prediction'))

# Bank Note Authentication 
@app.route("/bank-note-authentication/predict", methods=['GET', 'POST'])
def bank_note_authentication_predict():
    if request.method == 'POST':
        models = pickle.load(open('saved_models/bank_note_authentication/models.pkl', 'rb'))
        standard_scaler = pickle.load(open('saved_models/bank_note_authentication/standard_scaler.pkl', 'rb'))

        Variance = request.form['Variance']
        Skewness = request.form['Skewness']
        Curtosis = request.form['Curtosis']
        Entropy = request.form['Entropy']
        Algorithm = request.form['Algorithm']

        X_test = [[Variance, Skewness, Curtosis, Entropy]]
        X_test = standard_scaler.transform(X_test)

        if Algorithm == 'logistic_classifier':
            prediction = models[0].predict(X_test)[0]
        elif Algorithm == 'support_vector_classifier':
            prediction = models[1].predict(X_test)[0]
        else:
            prediction = models[2].predict(X_test)[0]

        if prediction == 0:
            prediction_text = 'The bank note is a fake!'
        else:
            prediction_text = 'The bank note is authentic!'

        return render_template('predict/bank_note_authentication.html', data_dict=url_dict['4'],
                                prediction_text=prediction_text, scroll='OutputPredictionText')
    return redirect(url_for('bank_note_authentication'))

# Car Resale Value Prediction
@app.route("/car-resale-value/predict", methods=['GET', 'POST'])
def car_resale_value_predict():
    if request.method == 'POST':
        models = pickle.load(open('saved_models/car_resale_value/models.pkl', 'rb'))

        Year = int(request.form['Year'])
        Present_Price = request.form['Present_Price']
        Kms_Driven = int(request.form['Kms_Driven'])
        Fuel_Type = request.form['Fuel_Type']
        Seller_Type = request.form['Seller_Type']
        Transmission_Type = request.form['Transmission_Type']
        Algorithm = request.form['Algorithm']

        Num_Years = datetime.datetime.now().year - Year

        if Fuel_Type == 'Diesel':
            Fuel_Type_Diesel = 1
            Fuel_Type_Petrol = 0
        elif Fuel_Type == 'Petrol':
            Fuel_Type_Diesel = 0
            Fuel_Type_Petrol = 1
        else:
            Fuel_Type_Diesel = 0
            Fuel_Type_Petrol = 0

        if Seller_Type == 'Individual':
            Seller_Type_Individual = 1
        else:
            Seller_Type_Individual = 0
        
        if Transmission_Type == 'Manual':
            Transmission_Manual = 1
        else:
            Transmission_Manual = 0

        X_test = [[Present_Price, Kms_Driven, Num_Years, Fuel_Type_Diesel, Fuel_Type_Petrol, 
                   Seller_Type_Individual, Transmission_Manual]]

        if Algorithm == 'linear_regressor':
            prediction = models[0].predict(X_test)[0]
        elif Algorithm == 'support_vector_regressor':
            prediction = models[1].predict(X_test)[0]
        else:
            prediction = models[2].predict(X_test)[0]

        if prediction < 0:
            prediction_text = 'Sorry, this car can\'t be sold under these conditions'
        else:
            prediction_text = 'Your car can be sold for Rs {} Lakhs'.format(round(prediction, 2))

        return render_template('predict/car_resale_value.html', data_dict=url_dict['5'],
                                prediction_text=prediction_text, scroll='OutputPredictionText')
    return redirect(url_for('car_resale_value'))

# Digit Recognition
@app.route("/digit-recognition/predict", methods=['GET', 'POST'])
def digit_recognition_predict():
    if request.method == 'POST':
        model = tf.keras.models.load_model('saved_models/digit_recognition/saved_model/my_model')
        
        image_url = request.form['ImageUploadURL']

        r = requests.get(image_url, stream=True, headers={'User-agent': 'Mozilla/5.0'})
        if r.status_code == 200:
            with open("image.png", 'wb') as f:
                r.raw.decode_content = True
                shutil.copyfileobj(r.raw, f)

        img = image.load_img("image.png", target_size=(28, 28))
        os.remove("image.png")
        x = image.img_to_array(img)
        x = np.expand_dims(x/255.0, axis=0)

        classes = model.predict(x, batch_size=1)
        prediction_text = "The predicted digit is {}".format(np.argmax(classes))
        return render_template('predict/digit_recognition.html', data_dict=url_dict['2'],
                                prediction_text=prediction_text, scroll='OutputPredictionText')
    return redirect(url_for('digit_recognition'))

# Rock Paper Scissors
@app.route("/rock-paper-scissors/predict", methods=['GET', 'POST'])
def rock_paper_scissors_predict():
    if request.method == 'POST':
        model = tf.keras.models.load_model('saved_models/rock_paper_scissors/saved_model/my_model')
        
        image_url = request.form['ImageUploadURL']
        r = requests.get(image_url, stream=True, headers={'User-agent': 'Mozilla/5.0'})
        if r.status_code == 200:
            with open("image.png", 'wb') as f:
                r.raw.decode_content = True
                shutil.copyfileobj(r.raw, f)

        img = image.load_img("image.png", target_size=(150, 150))
        os.remove("image.png")
        x = image.img_to_array(img)
        x = np.expand_dims(x/255.0, axis=0)

        classes = model.predict(x, batch_size=1)[0]
        if classes[0] == 1.:
            predicted_class = "Paper"
        elif classes[1] == 1.:
            predicted_class = "Rock"
        else:
            predicted_class = "Scissor"

        prediction_text = "The predicted action is {}!".format(predicted_class)
        del predicted_class
        del classes
        return render_template('predict/rock_paper_scissors.html', data_dict=url_dict['3'],
                                prediction_text=prediction_text, scroll='OutputPredictionText')
    return redirect(url_for('rock_paper_scissors'))


# Initializing the Flask App
if __name__ == '__main__':
    # app.run(host='0.0.0.0', debug=True)
    app.run(debug=True)