from flask import Flask, request, jsonify
import joblib
import numpy as np

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

    input_data = np.array(data).reshape(1, -1)
    input_scaled = scaler.transform(input_data)

    prediction = model.predict(input_scaled)
    result = le.inverse_transform(prediction)

    return jsonify({"prediction": result[0]})

if __name__ == "__main__":
    app.run(debug=True)