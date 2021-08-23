
import numpy as np
from flask import Flask, request, jsonify, render_template
import joblib

app = Flask(__name__)
# model = pickle.load(open('movies_model_overall.pkl', 'rb'))

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/prediction',methods=['GET','POST'])
def predict():

   if request.method == "POST" : 
       data = request.form.get('input1')
       data = np.array(data)
       data = data.reshape(1,-1)
        #open file
       file = open("movies_model_overall.pkl","rb")
    
        #load trained model
       trained_model = joblib.load(file)
    
        #predict
       prediction = trained_model.predict(data)

       output = round(prediction[0][0], 2)
    
       return render_template('index.html', prediction = 'Based on our prediction model, Revenue will be ${}'.format(output))

if __name__ == "__main__":
    app.run(debug=True)