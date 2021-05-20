# Importing Required Libraries and Modules
import pickle
import sklearn
import datetime
import warnings
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
    data_dict = {
        "source_code_link" : "https://github.com/rishabh1323/House-Price-Prediction",
        "dataset_link" : "https://www.kaggle.com/c/house-prices-advanced-regression-techniques",
        "stats_images_list" : {
            "Bar Plots" : [
                "/static/statistics_images/1_bar_1.png", "/static/statistics_images/1_bar_2.png",
                "/static/statistics_images/1_bar_3.png", "/static/statistics_images/1_bar_4.png"
            ],
            "Scatter Plots" : [
                "/static/statistics_images/1_scatter_1.png"
            ],
            "Distibution Plots" : [
                "/static/statistics_images/1_dist_1.png", "/static/statistics_images/1_dist_2.png"
            ]
        }
    }    
    return render_template("predict/house_price_prediction.html", data_dict=data_dict)

# Bank Note Authentication Page
@app.route("/bank-note-authentication", methods=['GET', 'POST'])
def bank_note_authentication():
    data_dict = {
        "source_code_link" : "https://github.com/rishabh1323/Bank-Note-Authentication",
        "dataset_link" : "https://www.kaggle.com/ritesaluja/bank-note-authentication-uci-data",
        "stats_images_list" : {
            "Box Plots" : [
                "/static/statistics_images/4_box_1.png", "/static/statistics_images/4_box_2.png",
                "/static/statistics_images/4_box_3.png", "/static/statistics_images/4_box_4.png"
            ],
            "Count Plots" : [
                "/static/statistics_images/4_count_1.png"
            ],
            "Distibution Plots" : [
                "/static/statistics_images/4_dist_1.png", "/static/statistics_images/4_dist_2.png",
                "/static/statistics_images/4_dist_3.png", "/static/statistics_images/4_dist_4.png"
            ]
        }
    }   
    return render_template("predict/bank_note_authentication.html", data_dict=data_dict)

# Car Resale Value Page
@app.route("/car-resale-value", methods=['GET', 'POST'])
def car_resale_value():
    data_dict = {
        "source_code_link" : "https://github.com/rishabh1323/Car-Resale-Value-Prediction",
        "dataset_link" : "https://www.kaggle.com/nehalbirla/vehicle-dataset-from-cardekho",
        "stats_images_list" : {
            "Bar Plots" : [
                "/static/statistics_images/5_bar_1.png", "/static/statistics_images/5_bar_2.png",
                "/static/statistics_images/5_bar_3.png", "/static/statistics_images/5_bar_4.png"
            ],
            "Box Plots" : [
                "/static/statistics_images/5_box_1.png", "/static/statistics_images/5_box_2.png",
                "/static/statistics_images/5_box_3.png", "/static/statistics_images/5_box_4.png"
            ],
            "Scatter Plots" : [
                "/static/statistics_images/5_scatter_1.png", "/static/statistics_images/5_scatter_2.png"
            ],
            "Distibution Plots" : [
                "/static/statistics_images/5_dist_1.png", "/static/statistics_images/5_dist_2.png",
                "/static/statistics_images/5_dist_3.png", "/static/statistics_images/5_dist_4.png"
            ]
        }
    }
    return render_template("predict/car_resale_value.html", data_dict=data_dict)

# Digit Recognition Page
@app.route("/digit-recognition", methods=['GET', 'POST'])
def digit_recognition():
    data_dict = {
        "source_code_link" : "https://github.com/rishabh1323/Deep-Learning-Basic-Projects/blob/main/mnist_digit_recognizer.ipynb",
        "dataset_link" : "https://www.kaggle.com/scolianni/mnistasjpg"
    }
    return render_template("predict/digit_recognition.html", data_dict=data_dict)

# Rock Paper Scissors Page
@app.route("/rock-paper-scissors", methods=['GET', 'POST'])
def rock_paper_scissors():
    data_dict = {
        "source_code_link" : "https://github.com/rishabh1323/Deep-Learning-Basic-Projects/blob/main/rock_paper_scissors.ipynb"
    }
    return render_template("predict/rock_paper_scissors.html", data_dict=data_dict)

#################################
##### Routes for Prediction #####
#################################

# House Price Prediction
@app.route("/house-price-prediction/predict", methods=['GET', 'POST'])
def house_price_prediction_predict():
    if request.method == 'POST':
        prediction_text = ""
        return render_template("predict/house_price_prediction.html", prediction_text=prediction_text, scroll='OutputPredictionText')
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

        return render_template("predict/bank_note_authentication.html", prediction_text=prediction_text, scroll='OutputPredictionText')
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

        X_test = [[Present_Price, Kms_Driven, Num_Years, Fuel_Type_Diesel, Fuel_Type_Petrol, Seller_Type_Individual, Transmission_Manual]]

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

        return render_template("predict/car_resale_value.html", prediction_text=prediction_text, scroll='OutputPredictionText')
    return redirect(url_for('car_resale_value'))

# Initializing the Flask App
if __name__ == '__main__':
    # app.run(host='0.0.0.0', debug=True)
    app.run(debug=True)