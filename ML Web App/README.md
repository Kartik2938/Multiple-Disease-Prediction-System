# Multiple Disease Prediction System

## Overview

The Multiple Disease Prediction System is a Machine Learning web application built using Streamlit. It predicts the likelihood of three diseases:

* Diabetes Prediction
* Heart Disease Prediction
* Parkinson's Disease Prediction

Users can enter the required medical parameters through a simple web interface and receive instant prediction results.

## Technologies Used

* Python
* Streamlit
* Scikit-learn
* NumPy
* Pandas
* Pickle

## Features

* Diabetes Prediction using Machine Learning
* Heart Disease Prediction using Machine Learning
* Parkinson's Disease Prediction using Machine Learning
* User-friendly interface
* Fast and accurate predictions

## Project Structure

```
Multiple Disease Prediction System/
│
├── Multiple Disease Pred.py
├── requirements.txt
├── README.md
└── saved models/
    ├── diabetes_model.sav
    ├── scaler.sav
    ├── heart_disease_model.sav
    ├── parkinsons_model.sav
    └── parkinsons_scaler.sav
```

## Installation

1. Clone the repository.
2. Install the required packages:

```
pip install -r requirements.txt
```

3. Run the application:

```
streamlit run "Multiple Disease Pred.py"
```

## Author

Kartik
