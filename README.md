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

## How to setup this project

1. First clone the repo locally.
    ```
    git clone <repo url>
    ```

2. Create a new virtual environment in the project directory.
    ```
    python3 -m venv ./venv
    ```

3. Activate the virtual environment.
    ```
    source venv/bin/activate
    ```

4. While in the virtual environment, install required dependencies from `requirements.txt`
    ```
    pip install -r ./requirements.txt
    ```
5. Ensure that you are in the project home directory, So now we can run the web application via
    ```
    python app.py
    ```
    and navigate to http://127.0.0.1:5000/ to see it live. On this page, a user can then interact with the application and receive predictions from the trained model.
