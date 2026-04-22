print("File is running...")

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.preprocessing import StandardScaler, LabelEncoder
from sklearn.metrics import accuracy_score, classification_report
import joblib

print("Loading dataset...")
data = pd.read_csv("intern_performance_dataset.csv", encoding="utf-8")
print("Dataset loaded successfully!")

X = data.drop(["Intern_ID", "Performance_Label"], axis=1)
y = data["Performance_Label"]

le = LabelEncoder()
y = le.fit_transform(y)

scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

X_train, X_test, y_train, y_test = train_test_split(
    X_scaled, y, test_size=0.2, random_state=42
)

# ✅ Algorithm 1: Decision Tree
print("\n--- Algorithm 1: Decision Tree ---")
dt_model = DecisionTreeClassifier(class_weight="balanced")
dt_model.fit(X_train, y_train)
dt_pred = dt_model.predict(X_test)
dt_accuracy = accuracy_score(y_test, dt_pred)
print(f"Decision Tree Accuracy: {dt_accuracy:.2f}")
print(classification_report(y_test, dt_pred, target_names=le.classes_))

# ✅ Algorithm 2: Random Forest
print("\n--- Algorithm 2: Random Forest ---")
rf_model = RandomForestClassifier(class_weight="balanced")
rf_model.fit(X_train, y_train)
rf_pred = rf_model.predict(X_test)
rf_accuracy = accuracy_score(y_test, rf_pred)
print(f"Random Forest Accuracy: {rf_accuracy:.2f}")
print(classification_report(y_test, rf_pred, target_names=le.classes_))

# ✅ Best Model Save
print("\n--- Comparing Models ---")
if rf_accuracy >= dt_accuracy:
    print(f"✅ Random Forest wins! ({rf_accuracy:.2f} vs {dt_accuracy:.2f})")
    best_model = rf_model
else:
    print(f"✅ Decision Tree wins! ({dt_accuracy:.2f} vs {rf_accuracy:.2f})")
    best_model = dt_model

print("Saving best model...")
joblib.dump(best_model, "intern_model.pkl")
joblib.dump(scaler, "scaler.pkl")
joblib.dump(le, "label_encoder.pkl")
print("Model trained and saved successfully!")