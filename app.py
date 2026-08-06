from flask import Flask, render_template, request
import joblib

app = Flask(__name__)

# Load trained model
model = joblib.load("ransomware_model.pkl")

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/predict", methods=["POST"])
def predict():

    cpu = float(request.form["cpu"])
    files = float(request.form["files"])
    encryption = float(request.form["encryption"])
    network = float(request.form["network"])

    prediction = model.predict([[cpu, files, encryption, network]])

    if prediction[0] == 1:
        result = "⚠️ Ransomware Detected"
    else:
        result = "✅ Benign Activity"

    return render_template("result.html", result=result)

if __name__ == "__main__":
    app.run(debug=True)