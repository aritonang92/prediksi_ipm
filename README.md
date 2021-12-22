# Predicting HDI per Province in Indonesia

This project is intended to an end-to-end Machine Learning platform to predict HDI (or IPM in Bahasa) 
per Province in Indonesia using Multivariate Linear Regression.

![testt](https://user-images.githubusercontent.com/65146994/147039552-6fea203a-fec5-4dbf-8551-638f6c037187.JPG)

## Description

This data science project series walks through step by step process of how to build 
a Human Development Index per Province prediction website.In Data Science the task of predicting number
is a regression problem so we will first build a model 
using `sklearn's linear regression` using selected historical data from 2011 to 2021 of
[BPS (Badan Pusat Statistik)](https://www.bps.go.id/indicator/26/494/1/-metode-baru-indeks-pembangunan-manusia-menurut-provinsi.html) 
in this website you can also read the methodology to get that value and its related parameters. 
Second step would be to write a python flask server that uses the saved model to serve http requests. 
There are three components to built the website such as html, css and javascript that allows user to 
enter these variables such as name of province, life expectancy (in years), periods in schooling (in years), 
periods in schooling expectations (in years) and expenditure per capita per person per year (in thousands rupiah) 
and these will call python flask server to retrieve the predicted HDI value.

## Prerequisites
Before you build this project you must have these particular packages installed on your own PC:

* sklearn 
* pandas 
* Flask (for API) 

## Project's Architecture
This project has three major parts: 

1. model : in model's folder you'll find `hdi.py` file it is a foundation of this app, contains cleansing set and
   modelling part in linear regression and at the final step you saved the model in pickle's format.
2. server : this folder contains server.py and util.py these two files works to enable html calls, also one folder named artifacts that contains columns.json that consists of name of provinces in json format and hdi.pickle that the saved ML model at the last.
3. model : this contains hdi.py as a final file of ML model, hdi.pickle as a saved model in pickle's format and columns.json that consist of name of provinces in json format.
4. client : this folder contains : app.html (which forms the structure of the website in html format), app.js (which helps html files in shaping and receiving data from machine learning processing) and app.css (this file contains the website design (such as color, text size, text type, etc.)

## Running the project

1. First you should open the server folder and select the `server.py` file then run it, after that you will get a http call link.

```
Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
```

2. You can also test the Machine Learning model that gives you the results of selected province by running `util.py` file at this same folder `server`.

```
Prediksi nilai IPM Provinsi DI YOGYAKARTA adalah: ****
```

3. After you ensure that these two steps works well, open client folder and select `app.html` then run it by double clicks, it will directs you to your preference web browser and then you can fill in those fields then predicts the HDI. 


