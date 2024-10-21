from flask import app, jsonify, request
from joblib import load
import pandas as pd
import io

model = load('./models/random_forest_model.joblib')

def predict():
    try:
        data = request.data.decode('utf-8')  # Get raw data from the request

        if not data:
            return jsonify({"error": "No data received or invalid format"}), 400
        
        # Read CSV data into a DataFrame
        df = pd.read_csv(io.StringIO(data))
        
        # Make predictions
        predictions = model.predict(df)

        # Return predictions
        return jsonify({"predictions": predictions.tolist()})
    
    except Exception as e:
        return jsonify({"error": str(e)})
