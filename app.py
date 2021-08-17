# Import libraries
import numpy as np
from flask import Flask, request, jsonify, render_template
import pickle

app = Flask(__name__)

# Load the model
model = pickle.load(open('movies_model_overall.pkl','rb'))

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/api',methods=['POST'])
def predict():
    # Get the data from the POST request.
    data = request.get_json(force=True)
    print(data)
    # Make prediction using model loaded from disk as per the data.
    prediction = model.predict([[(data['values'])]])
    print(prediction)
    # Take the first value of prediction
    output = prediction[0][0]
    return jsonify({"result" : output})

if __name__ == '__main__':
    app.run(port=5000, debug=True)
