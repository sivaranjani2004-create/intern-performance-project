from flask import Flask, request, jsonify, render_template
import joblib
import numpy as np
import os
import sys

app = Flask(__name__)

# File path settings
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

def load_files():
    try:
        print("--- Starting File Load ---")
        
        model_path = os.path.join(BASE_DIR, "intern_model.pkl")
        scaler_path = os.path.join(BASE_DIR, "scaler.pkl")
        le_path = os.path.join(BASE_DIR, "label_encoder.pkl")

        print(f"Loading from: {BASE_DIR}")

        model = joblib.load(model_path)
        print("✅ Model loaded")
        
        scaler = joblib.load(scaler_path)
        print("✅ Scaler loaded")
        
        le = joblib.load(le_path)
        print("✅ Label encoder loaded")
        
        return model, scaler, le
    except Exception as e:
        print(f"❌ Error during loading: {e}")
        sys.exit(1)

# Global variables setup
model, scaler, le = load_files()

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/predict", methods=["POST"])
def predict():
    try:
        json_data = request.get_json()
        data = json_data["features"]
        
        input_data = np.array(data).reshape(1, -1)
        input_scaled = scaler.transform(input_data)

        prediction = model.predict(input_scaled)
        result = le.inverse_transform(prediction)

        return jsonify({"prediction": str(result[0])})
    except Exception as e:
        return jsonify({"error": str(e)}), 400

if __name__ == "__main__":
    print("--- Starting Flask Server ---")
    app.run(debug=True, port=5000)