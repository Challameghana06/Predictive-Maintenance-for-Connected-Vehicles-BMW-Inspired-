import streamlit as st
import numpy as np
try:
    import joblib
except ImportError:
    import os
    os.system("pip install joblib")
    import joblib
model = joblib.load("rf_model.joblib")

import joblib
import os

st.title("🚗 BMW Predictive Maintenance AI App")

st.write("Files in directory:", os.listdir("."))

try:
    model = joblib.load("rf_model.joblib")
    st.success("✅ Model loaded successfully.")
except Exception as e:
    st.error(f"Model failed to load: {e}")
    st.stop()

# ---- prediction UI ----
air_temp = st.slider("Air Temperature [K]", 290, 320, 300)
process_temp = st.slider("Process Temperature [K]", 300, 350, 320)
torque = st.slider("Torque [Nm]", 0, 80, 40)
rot_speed = st.slider("Rotational Speed [rpm]", 1000, 3000, 1500)
tool_wear = st.slider("Tool Wear [min]", 0, 250, 50)

features = np.array([[air_temp, process_temp, torque, rot_speed, tool_wear]])

if st.button("🔍 Predict Maintenance Status"):
    pred = model.predict(features)[0]
    if pred == 1:
        st.error("⚠️ Maintenance Needed Soon!")
    else:
        st.success("✅ Vehicle Operating Normally")

