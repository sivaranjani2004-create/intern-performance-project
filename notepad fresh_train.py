# print("STARTING FULL SCRIPT")

# import pandas as pd
# from sklearn.model_selection import train_test_split
# from sklearn.ensemble import RandomForestClassifier
# from sklearn.preprocessing import StandardScaler, LabelEncoder
# import joblib




# print("Loading dataset...")

# print("Trying to load dataset...")

# data = pd.read_csv("intern_performance_dataset.csv", encoding="latin1", engine="python")

# print("Dataset loaded successfully!")
# print(data.head())

# print(data["Performance_Label"].value_counts())





# print(data["Performance_Label"].value_counts())

# X = data.drop(["Intern_ID", "Performance_Label"], axis=1)
# y = data["Performance_Label"]

# le = LabelEncoder()
# y = le.fit_transform(y)

# scaler = StandardScaler()
# X_scaled = scaler.fit_transform(X)

# X_train, X_test, y_train, y_test = train_test_split(
#     X_scaled, y, test_size=0.2, random_state=42
# )

# print("Training model...")

# model = RandomForestClassifier(class_weight="balanced")
# model.fit(X_train, y_train)

# print("Saving model...")

# joblib.dump(model, "intern_model.pkl")
# joblib.dump(scaler, "scaler.pkl")
# joblib.dump(le, "label_encoder.pkl")

# print("DONE SUCCESSFULLY")





print("STEP 1")

import pandas as pd
print("STEP 2")

from sklearn.model_selection import train_test_split
print("STEP 3")

from sklearn.ensemble import RandomForestClassifier
print("STEP 4")

from sklearn.preprocessing import StandardScaler, LabelEncoder
print("STEP 5")

import joblib
print("STEP 6")

print("Before reading CSV")

print("Reading CSV now...")

data = pd.read_csv("intern_performance_dataset.csv", encoding="latin1", engine="python")

print("CSV successfully loaded")
print("CSV LOADED")