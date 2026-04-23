import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import LabelEncoder
import joblib
import os

os.makedirs("model", exist_ok=True)

data = pd.read_csv("intern_performance_dataset.csv")

# 🔥 Smart Score
data['Performance_Score'] = (
    data['Tasks_Completed'] * 2 +
    data['Attendance_Percentage'] * 0.5 +
    data['Engagement_Score'] * 3 +
    data['Consistency_Score'] * 2 -
    data['Deadline_Misses'] * 5
)

# 🔥 Rule-based label
def label_rule(score):
    if score > 120:
        return "High"
    elif score > 70:
        return "Medium"
    else:
        return "Low"

data['Performance_Label'] = data['Performance_Score'].apply(label_rule)

X = data[[
    'Tasks_Assigned','Tasks_Completed','Avg_Task_Time_Hours',
    'Attendance_Percentage','Consistency_Score','Engagement_Score',
    'Feedback_Score','Learning_Progress','Deadline_Misses'
]]

le = LabelEncoder()
y = le.fit_transform(data['Performance_Label'])

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

model = RandomForestClassifier(n_estimators=200)
model.fit(X_train, y_train)

accuracy = model.score(X_test, y_test)

joblib.dump(model, "model/intern_model.pkl")
joblib.dump(le, "model/label_encoder.pkl")
joblib.dump(accuracy, "model/accuracy.pkl")

print("✅ Accuracy:", accuracy)
print("✅ Model Ready")