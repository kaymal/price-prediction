
# Import necessary modules
from flask import Flask, request, jsonify
import pickle
import pandas as pd

import traceback

# Create an instance of Flask class
app = Flask(__name__)

# Use pickle to load in the pre-trained model.
with open('model_rf.pkl', 'rb') as m:
    model_rf = pickle.load(m)

# Use pickle to load in the feature names.
with open('model_features.pkl', 'rb') as f:
    features = pickle.load(f)

@app.route('/')
def index():
    return 'Server is up and running!'

@app.route('/predict', methods=['GET', 'POST'])
def predict():
    if request.method == 'POST':
        try:
            # Get data for prediction (Parse data as JSON)
            json_data = request.get_json()
            
            # Raise an Error if there are values not entered
            if not all(k in json_data for k in ["hp", "age", "km", "model"]):
                raise ValueError("Not enough data to make a prediction!")
            
            # Create a DataFrame from JSON
            df = pd.DataFrame.from_dict([json_data], orient='columns')
            
            # Create dummy variables and persist features
            df = pd.get_dummies(df).reindex(columns=features, fill_value=0)
            # Note that if a column name (value) in JSON is wrong, 
            # The relevant column is filled with '0'
            
            # Predict the target
            prediction = list(model_rf.predict(df))
            
            # Return the result in JSON format
            return jsonify({"prediction": prediction})
        
        except:
            return jsonify({'trace': traceback.format_exc()})
    else:
        print("Nothing posted!")
        return "Nothing posted!"

if __name__ == '__main__':
    app.run(debug=True)
# Debugging mode is enabled to provide code reloading and better error messages.
