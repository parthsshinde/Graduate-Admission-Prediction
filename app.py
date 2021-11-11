import numpy as np
from flask import Flask, request, render_template, jsonify
import pickle

app = Flask(__name__)
model = pickle.load(open('new_model.pkl', 'rb'))
    
@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict',methods=['POST'])
def predict():
    '''
    For rendering results on HTML GUI
    '''
    int_features = [int(x) for x in request.form.values()]
    final_features = [np.array(int_features)]
    prediction = model.predict(final_features)
    output = prediction[0]*100

    return render_template('index.html', prediction_text='Chance of Admition is {}%'.format(round(output[0],2)))



if __name__ == "__main__":
    app.run(debug=True)
