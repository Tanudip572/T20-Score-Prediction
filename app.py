import streamlit as st
import pickle
import pandas as pd
import numpy as np
# Delay importing xgboost until it's needed to avoid import errors during startup
# (xgboost is required only for unpickling or training the model).
import importlib

def module_available(name):
    try:
        importlib.import_module(name)
        return True
    except Exception:
        return False

have_xgboost = module_available('xgboost')
have_sklearn = module_available('sklearn')

pipe = None
if have_xgboost and have_sklearn:
    try:
        with open('pipe.pkl','rb') as f:
            pipe = pickle.load(f)
    except Exception:
        pipe = None
        st.warning("Model file 'pipe.pkl' not found or could not be loaded. Upload it below or add it to the repo.")
else:
    st.info("Model predictions are temporarily disabled while server dependencies (xgboost/scikit-learn) install. You can still upload a model file to enable predictions.")

uploaded_file = st.file_uploader('Upload pipe.pkl', type=['pkl'])
if uploaded_file is not None:
    try:
        data = uploaded_file.read()
        pipe = pickle.loads(data)
        st.success("Model uploaded and loaded successfully.")
    except Exception as e:
        pipe = None
        st.error(f"Uploaded file could not be loaded as a pickle: {e}")


teams = ['Australia',
 'India',
 'Bangladesh',
 'New Zealand',
 'South Africa',
 'England',
 'West Indies',
 'Afghanistan',
 'Pakistan',
 'Sri Lanka']

cities = ['Colombo',
 'Mirpur',
 'Johannesburg',
 'Dubai',
 'Auckland',
 'Cape Town',
 'London',
 'Pallekele',
 'Barbados',
 'Sydney',
 'Melbourne',
 'Durban',
 'St Lucia',
 'Wellington',
 'Lauderhill',
 'Hamilton',
 'Centurion',
 'Manchester',
 'Abu Dhabi',
 'Mumbai',
 'Nottingham',
 'Southampton',
 'Mount Maunganui',
 'Chittagong',
 'Kolkata',
 'Lahore',
 'Delhi',
 'Nagpur',
 'Chandigarh',
 'Adelaide',
 'Bangalore',
 'St Kitts',
 'Cardiff',
 'Christchurch',
 'Trinidad']

st.title('Cricket Score Predictor')

col1, col2 = st.columns(2)

with col1:
    batting_team = st.selectbox('Select batting team',sorted(teams))
with col2:
    bowling_team = st.selectbox('Select bowling team', sorted(teams))

city = st.selectbox('Select city',sorted(cities))

col3,col4,col5 = st.columns(3)

with col3:
    current_score = st.number_input('Current Score')
with col4:
    overs = st.number_input('Overs done(works for over>5)')
with col5:
    wickets = st.number_input('Wickets out')

last_five = st.number_input('Runs scored in last 5 overs')

if st.button('Predict Score'):
    balls_left = 120 - (overs*6)
    wickets_left = 10 -wickets
    crr = current_score/overs if overs>0 else 0

    if pipe is None:
        st.error("No model available to make predictions. Upload pipe.pkl or add it to the repository.")
    else:
        input_df = pd.DataFrame({
            'batting_team': [batting_team],
            'bowling_team': [bowling_team],
            'city': [city],
            'current_score': [current_score],
            'balls_left': [balls_left],
            'wickets_left': [wickets_left],
            'crr': [crr],
            'last_five': [last_five]
        })
        result = pipe.predict(input_df)
        st.header("Predicted Score - " + str(int(result[0])))


