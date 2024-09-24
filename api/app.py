from flask import Flask, request
from pickle import load
from flask_cors import CORS
from models import Predict_Body
import os
import pandas as pd

app = Flask(__name__)
CORS(app)

pipeline_path = os.path.join('data', 'pipeline.pkl')

@app.post("/predict")
def predict():
    body_data = request.get_json()
    body = Predict_Body(**body_data)

    X_input = Predict_Body.transform_into_X_input(body)
    loaded_pipeline = load(open(pipeline_path, 'rb'))
    result = loaded_pipeline.predict(X_input)
    return {"outcome": result[0]}

if __name__ == "__main__":
    app.run(debug=True)