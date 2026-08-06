import pandas as pd
from sklearn.ensemble import RandomForestClassifier
import joblib

# Read dataset
data = pd.read_csv("ransomware_dataset.csv")

# Inputs (features)
X = data.drop("label", axis=1)

# Output (answer)
y = data["label"]

# Create ML model
model = RandomForestClassifier()

# Train model
model.fit(X, y)

# Save trained model
joblib.dump(model, "ransomware_model.pkl")

print("Model Trained Successfully!")