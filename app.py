from flask import Flask, render_template, request, redirect, send_file
import pandas as pd
import os

app = Flask(__name__)


# =========================
# 🔹 HOME
# =========================
@app.route('/')
def home():
    return redirect('/dashboard')


# =========================
# 🔹 DASHBOARD PAGE
# =========================
@app.route('/dashboard')
def dashboard():
    return render_template('dashboard.html')


# =========================
# 🔹 FORM PREDICTION
# =========================
@app.route('/predict', methods=['POST'])
def predict():
    f = request.form

    Tasks_Assigned = float(f['Tasks_Assigned'])
    Tasks_Completed = float(f['Tasks_Completed'])
    Avg_Task_Time_Hours = float(f['Avg_Task_Time_Hours'])
    Attendance_Percentage = float(f['Attendance_Percentage'])
    Consistency_Score = float(f['Consistency_Score'])
    Engagement_Score = float(f['Engagement_Score'])
    Feedback_Score = float(f['Feedback_Score'])
    Learning_Progress = float(f['Learning_Progress'])
    Deadline_Misses = float(f['Deadline_Misses'])

    # 🔥 SCORE CALCULATION
    score = (
        Tasks_Completed * 2 +
        Attendance_Percentage * 0.5 +
        Engagement_Score * 3 +
        Consistency_Score * 2 -
        Deadline_Misses * 5
    )

    # 🔥 FINAL THRESHOLD FIX
    if score >= 100:
        result = "High"
    elif score >= 60:
        result = "Medium"
    else:
        result = "Low"

    return render_template(
        'dashboard.html',
        prediction_text=f"Performance: {result}",
        score=round(score, 2),
        form=f
    )


# =========================
# 🔹 CSV UPLOAD
# =========================
@app.route('/upload', methods=['GET', 'POST'])
def upload():
    if request.method == 'POST':
        file = request.files['file']
        df = pd.read_csv(file)

        predictions = []

        for _, row in df.iterrows():
            score = (
                row['Tasks_Completed'] * 2 +
                row['Attendance_Percentage'] * 0.5 +
                row['Engagement_Score'] * 3 +
                row['Consistency_Score'] * 2 -
                row['Deadline_Misses'] * 5
            )

            if score >= 100:
                predictions.append("High")
            elif score >= 60:
                predictions.append("Medium")
            else:
                predictions.append("Low")

        df['Prediction'] = predictions

        # Save CSV
        os.makedirs("static", exist_ok=True)
        df.to_csv("static/predictions.csv", index=False)

        # GRAPH DATA
        counts = df['Prediction'].value_counts()
        labels = ["Low", "Medium", "High"]
        values = [int(counts.get(i, 0)) for i in labels]

        return render_template(
            'upload.html',
            table=df.to_html(index=False),
            show=True,
            labels=labels,
            values=values
        )

    return render_template('upload.html')


# =========================
# 🔹 DOWNLOAD
# =========================
@app.route('/download')
def download():
    return send_file("static/predictions.csv", as_attachment=True)


# =========================
# 🔥 IMPORTANT FOR DEPLOYMENT
# =========================
if __name__ == "__main__":
    app.run()