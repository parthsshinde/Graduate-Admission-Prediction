# Graduate-Admission-Prediction

## Content
The dataset contains several parameters which are considered important during the application for Masters Programs.
The parameters included are :

- GRE Scores ( out of 340 )
- TOEFL Scores ( out of 120 )
- University Rating ( out of 5 )
- Statement of Purpose and Letter of Recommendation Strength ( out of 5 )
- Undergraduate GPA ( out of 10 )
- Research Experience ( either 0 or 1 )
- Chance of Admit ( ranging from 0 to 1 )

## Inspiration
This dataset was built with the purpose of helping students in shortlisting universities with their profiles. The predicted output gives them a fair idea about their chances for a particular university.

In this project we use machine learning techniques to predict whether an applicant will get accepetd for the graduate program or not.


The dataset contains several parameters which are considered important during the application for Masters Programs.


## ML Model Flask-Deployment

Here we will deploy Machine Learning Models production using Flask API!

### Tools and Tech used ~
- Bootstrap studio
- Heroku    
- Flask
- Scikit Learn
- Pandas
- Numpy

## Project Structure

`Dataset` - This directory consist on required data for training and testing the machine learning model, after the model is trained we dump the pickel file here.

`app.py` - This file contains Flask APIs that receives employee details through GUI or API calls, computes the precited value based on our model and returns it.

`templates` - This folder contains the HTML template to allow user to enter applicant details and displays the predicted result.

