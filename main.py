from flask import Flask,render_template,request
import plotly
import plotly.graph_objs as go
import plotly.express as px

import pandas as pd
import numpy as np
import json
import joblib

app = Flask(__name__)


# default page (distribution plot page)
@app.route('/')
def index():
    return render_template('insights.html')


# insights function
@app.route('/insights')
def insights_fn():
    return render_template('insights.html')


# data display function
@app.route('/see_the_data', methods=['POST','GET'])
def data_fn():
    # generate dataframe
    df = pd.read_csv("./static/data.csv")
    if request.method == 'GET':
        return render_template('data.html')
    elif request.method == 'POST':
        disp = []
        num = int(request.form.get('num_disp'))
        source = df.sample(num).to_dict('records')
        for i in source:
            disp.append(i)
        return render_template('data.html',
                                num=num,
                                disp=disp,
                                title='Data')


# prediction input function
@app.route('/predict_result', methods=['POST', 'GET'])
def predict_fn():
    return render_template('predict.html', title='Prediction Input')


# prediction result function
@app.route('/result', methods=['POST', 'GET'])
def result():
    country = ""

    if request.method == 'POST':
        # extracting input
        country = request.form.get('country')

        # processing vaccination data
        df = pd.read_csv("./static/data.csv")  
        df.set_index('date', inplace=True) 
        data = df[df['country']==country]

        # extraxting data of country population
        population = pd.read_csv('./static/population.csv')
        citizenNum = population[population['Country (or dependency)']==country].iloc[0][1]

        # providing variables
        history = list(data['Daily Vaccinations'])
        vaccinated = data['Daily Vaccinations'].sum()
        day = 0

        # looping to find number of vaccinated citizen
        from statsmodels.tsa.arima_model import ARIMA, ARIMAResults
        while vaccinated < 80/100*citizenNum:
            model = ARIMA(history, order=(0,1,0))
            model = model.fit()
            start = len(history)
            pred = model.predict(start=start, end=start, typ='levels')
            vaccinated += int(pred[0])
            history.append(int(pred[0]))
            day += 1
        mean = int(sum(history)/len(history))
    return render_template('result.html',                            
                            country=country,
                            day=day,
                            mean=mean,
                            population=citizenNum,
                            title='Prediction Result')

if __name__ == '__main__':
    app.run(debug=True)
