import streamlit as st
import pickle
import pandas as pd
import numpy as np
import importlib

# Delay importing xgboost until it's available to avoid startup failures
try:
    import xgboost
    from xgboost import XGBRegressor
    have_xgboost = True
except Exception:
    have_xgboost = False

pipe = None

def try_load_repo_model():
    """Attempt to load pipe.pkl from the repository and show helpful messages on failure."""
    global pipe
    try:
        with open('pipe.pkl','rb') as f:
            pipe = pickle.load(f)
            return True
    except FileNotFoundError:
        pipe = None
        st.warning("Model file 'pipe.pkl' not found in repository. You can upload it below or add it to the repo.")
    except (ImportError, ModuleNotFoundError) as e:
        pipe = None
        st.error(f"Found 'pipe.pkl' but loading failed due to a missing package: {e}. Redeploy so requirements.txt installs scikit-learn/xgboost matching the model, or recreate the pickle with the target environment versions.")
    except Exception as e:
        pipe = None
        st.error(f"Could not load 'pipe.pkl' from repo: {e}")
    return False

if have_xgboost:
    try_load_repo_model()
else:
    st.info("Server dependencies are still installing or unavailable. Predictions disabled until install completes. If 'pipe.pkl' is present in the repo, trigger a redeploy so requirements install and the model can be loaded automatically; otherwise upload via the UI.")

uploaded_file = st.file_uploader('Upload pipe.pkl', type=['pkl'])
if uploaded_file is not None:
    try:
        data = uploaded_file.read()
        pipe = pickle.loads(data)
        st.success("Model uploaded and loaded successfully.")
    except (ImportError, ModuleNotFoundError) as e:
        pipe = None
        st.error(f"Uploaded pickle requires a missing package: {e}. Redeploy the app so requirements.txt installs required packages (scikit-learn, xgboost) or recreate the pickle compatible with the runtime.")
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
        if st.button("Retry loading 'pipe.pkl' from repository"):
            if have_xgboost:
                if try_load_repo_model():
                    st.success("Loaded 'pipe.pkl' from repository.")
                else:
                    st.error("Failed to load 'pipe.pkl' from repository. See messages above.")
            else:
                st.info("Server dependencies are not yet available. Redeploy or wait for requirements to install before retrying.")
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