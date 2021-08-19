
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
    
       return render_template('index.html', prediction = prediction[0][0])

if __name__ == "__main__":
    app.run(debug=True)