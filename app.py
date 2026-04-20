from flask import Flask, request, jsonify
import joblib
import numpy as np
import os

print("Starting Flask app...")

app = Flask(__name__)

# Load model files
model = joblib.load("intern_model.pkl")
scaler = joblib.load("scaler.pkl")
le = joblib.load("label_encoder.pkl")


@app.route("/")
def home():
    return "Intern Performance Prediction API is Running"


@app.route("/predict", methods=["POST"])
def predict():
    data = request.json["features"]

    # Convert input
    input_data = np.array(data).reshape(1, -1)

    # Scale input
    input_scaled = scaler.transform(input_data)

    # Predict
    prediction = model.predict(input_scaled)

    # Convert label back
    result = le.inverse_transform(prediction)

    return jsonify({"prediction": result[0]})


# IMPORTANT: Render requires this format
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
