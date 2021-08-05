# The ML-DL App

A python based web application featuring a collection of end-to-end implemented machine learning and deep learning models solving various problem statements. Made using Flask web framework, this application predicts new output for a given user input using pre-trained models. Currently it consists of 5 different problem statements (applications) from machine learning and computer vision domains.

The application is live [here](https://the-ml-dl-app.herokuapp.com/).

## Applications
1. House Price Prediction - [Dataset](https://www.kaggle.com/c/house-prices-advanced-regression-techniques)
2. Digit Recognition - [Dataset](https://www.kaggle.com/scolianni/mnistasjpg)
3. Rock Paper Scissors - [Dataset](https://laurencemoroney.com/datasets.html)
4. Bank Note Authentication - [Dataset](https://www.kaggle.com/ritesaluja/bank-note-authentication-uci-data)
5. Car Resale Value - [Dataset](https://www.kaggle.com/nehalbirla/vehicle-dataset-from-cardekho)

## Technologies Used
![Python](https://img.shields.io/badge/-Python-FFFFFF?style=flat&logo=python&logoColor=3776AB)&nbsp;&nbsp;&nbsp;
![Flask](https://img.shields.io/badge/-Flask-FFFFFF?style=flat&logo=flask&logoColor=000000)&nbsp;&nbsp;&nbsp;
![TensorFlow](https://img.shields.io/badge/-TensorFlow-FFFFFF?style=flat&logo=tensorflow&logoColor=FF6F00)  

![HTML](https://img.shields.io/badge/-HTML-FFFFFF?style=flat&logo=HTML5)&nbsp;&nbsp;&nbsp;
![CSS](https://img.shields.io/badge/-CSS-FFFFFF?style=flat&logo=CSS3&logoColor=1572B6) 

![Heroku](https://img.shields.io/badge/-Heroku-FFFFFF?style=flat&logo=heroku&logoColor=430098)&nbsp;&nbsp;&nbsp;
![Git](https://img.shields.io/badge/-Git-FFFFFF?style=flat&logo=git&logoColor=F05032)

## Installations Required
For running the source code on your local machine, the following dependencies are required.
- Python
- Flask
- Numpy
- OpenCV
- Pillow
- Scikit-Learn
- TensorFlow

These dependencies can be installed using `pip` using the following commands
```
pip install flask==2.0.0 numpy==1.19.5 opencv-python==4.5.2.52 Pillow==8.2.0 scikit-learn==0.24.2 tensorflow-cpu==2.5.0
```

## Launch
The web application is hosted on Heroku [here](https://the-ml-dl-app.herokuapp.com/).

For local installation, follow these steps:
1. Download source code from this repository or click [here](https://github.com/rishabh1323/The-ML-DL-App/archive/refs/heads/main.zip).
2. Extract files to desired directory.
3. [Download](https://www.python.org/downloads/) and install Python3 if not done already.
4. Create a new python virtual environment.
```
python3 -m venv tutorial-env
```
5. Once you’ve created a virtual environment, you may activate it.  

`On Windows, run:`
```
tutorial-env\Scripts\activate.bat
```
`On Unix or MacOS, run:`
```
source tutorial-env/bin/activate
```
> Refer to [python documentation](https://docs.python.org/3/tutorial/venv.html) for more information on virtual environments.  
6. Install required dependecies (as mentioned above).
```
pip install flask==2.0.0 numpy==1.19.5 opencv-python==4.5.2.52 Pillow==8.2.0 scikit-learn==0.24.2 tensorflow-cpu==2.5.0
```
7. Start a local server on default port number.
```
python app.py
```
8. Go to `localhost:5000` from your browser to launch the application.