# 🏏 T20 Cricket Score Prediction

A Machine Learning-based web application that predicts the final score of a T20 cricket innings using real-time match information such as batting team, bowling team, current score, wickets lost, current run rate, and runs scored in the last five overs.

## 📌 Project Overview

This project leverages historical T20 cricket data and machine learning techniques to estimate the final innings score during a live match. The model is trained on ball-by-ball cricket data and deployed using Streamlit for an interactive user experience.

## 🚀 Features

* Predicts the final T20 innings score in real time.
* Interactive Streamlit web application.
* Uses historical international T20 cricket data.
* Feature engineering based on match situation.
* XGBoost Regressor for high prediction accuracy.
* User-friendly interface for match inputs.

## 📊 Dataset

The dataset used in this project was obtained from:

* [Cricsheet T20 Dataset](https://www.kaggle.com/veeralakrishna/cricsheet-a-retrosheet-for-cricket?select=t20)

The dataset contains ball-by-ball information from international T20 matches, including:

* Batting Team
* Bowling Team
* City
* Runs Scored
* Wickets Lost
* Overs Completed
* Match Information

## 🔧 Feature Engineering

The following features were created to improve model performance:

* Batting Team
* Bowling Team
* City
* Current Score
* Balls Left
* Wickets Left
* Current Run Rate (CRR)
* Runs Scored in Last 5 Overs

Additional preprocessing steps include:

* Handling missing values
* Team filtering
* One-Hot Encoding of categorical variables
* Match-wise cumulative calculations

## 🤖 Machine Learning Model

Algorithm Used:

* XGBoost Regressor

Model Pipeline:

1. Data Extraction and Cleaning
2. Feature Engineering
3. One-Hot Encoding
4. Model Training
5. Hyperparameter Tuning
6. Model Serialization using Pickle
7. Streamlit Deployment

## 📈 Model Performance

| Metric                    | Score     |
| ------------------------- | --------- |
| R² Score                  | 0.947     |
| Mean Absolute Error (MAE) | 3.16 Runs |

The model predicts the final innings score with high accuracy and a low prediction error.

## 🛠️ Technologies Used

* Python
* Pandas
* NumPy
* Scikit-Learn
* XGBoost
* Streamlit
* Pickle

## 📂 Project Structure

```text
T20-Score-Prediction/
│
├── data_extraction.ipynb
├── Feature_Ext_&_Modeling.ipynb
├── app.py
├── pipe.pkl
├── README.md
│
└── Dataset/
```

## ▶️ Running the Project

### Clone Repository

```bash
git clone https://github.com/Tanudip572/T20-Score-Prediction.git
cd T20-Score-Prediction
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Run Streamlit App

```bash
streamlit run app.py
```

## 📷 Application Workflow

1. Select Batting Team
2. Select Bowling Team
3. Select Match City
4. Enter Current Score
5. Enter Overs Completed
6. Enter Wickets Lost
7. Enter Runs Scored in Last 5 Overs
8. Click Predict Score

The application returns the predicted final innings score.

## 🎯 Future Improvements

* IPL-specific score prediction
* Win probability prediction
* Live match API integration
* Deep Learning-based prediction models
* Advanced feature engineering

## 👨‍💻 Author

Tanudip Ghosh

If you found this project useful, consider giving it a ⭐ on GitHub.
