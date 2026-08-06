Streamlit Cloud deployment

This repository contains a Streamlit app (app.py) that predicts T20 scores.

Quick deploy steps (Streamlit Community Cloud):
1. Push this branch to GitHub (branch: tanudip572-deploy-t20-score-prediction).
2. Visit https://share.streamlit.io and sign in with GitHub.
3. Click "New app" → select this repository and choose branch `tanudip572-deploy-t20-score-prediction`.
4. Set the main file to `app.py` and deploy.

Notes
- Dependencies are listed in requirements.txt (includes streamlit and xgboost).
- The app supports uploading `pipe.pkl` via the UI; to make predictions without manual upload, add `pipe.pkl` to the repo (consider Git LFS for large files).
- To update the app, push commits to the chosen branch; Streamlit Cloud redeploys automatically.

If you want, I can push this branch and create this file for you now.