import joblib

# Load trained model
model = joblib.load("ransomware_model.pkl")

# Test values
sample = [[75, 85, 95, 90]]

prediction = model.predict(sample)

if prediction[0] == 1:
    print("Ransomware Detected")
else:
    print("Benign Activity")