# 🛡️ Ransomware Detection Using Machine Learning

## Overview
A Machine Learning-based web application that detects ransomware activity using system behavior metrics such as CPU usage, file changes, encryption rate, and network activity.

## Technologies Used
- Python
- Flask
- Scikit-Learn
- Pandas
- HTML/CSS
- Bootstrap

## Features
- Ransomware Detection
- Machine Learning Prediction
- Flask Web Interface
- Real-time Results

## Project Structure

```text
Ransomware-Detection-ML
│
├── app.py
├── train_model.py
├── test_model.py
├── ransomware_dataset.csv
├── ransomware_model.pkl
└── templates
    ├── index.html
    └── result.html
```

## How to Run

```bash
python app.py
```

Open:

```text
http://127.0.0.1:5000
```

## Sample Results

**Input:** 25, 12, 8, 20  
**Output:** ✅ Benign Activity

**Input:** 75, 85, 95, 90  
**Output:** ⚠️ Ransomware Detected

## Author

**Nayana Kannan**  
B.Tech Computer Science and Engineering
