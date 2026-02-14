import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
from datetime import datetime
import time

st.set_page_config(page_title="Water Safety Lab", page_icon="💧", layout="wide")

st.markdown("""
    <style>
    .safety-safe { background-color: #2ecc71; color: white; padding: 20px; border-radius: 10px; text-align: center; }
    .safety-warning { background-color: #f1c40f; color: black; padding: 20px; border-radius: 10px; text-align: center; }
    .safety-danger { background-color: #e74c3c; color: white; padding: 20px; border-radius: 10px; text-align: center; }
    </style>
    """, unsafe_allow_html=True)

st.title("💧 Real-Time Water Quality Analysis")

if 'water_log' not in st.session_state:
    st.session_state.water_log = pd.DataFrame(columns=['Time', 'pH', 'TDS'])

placeholder = st.empty()

for _ in range(100):
    ph = round(np.random.uniform(6.5, 8.5), 2)
    tds = round(np.random.uniform(100, 600), 0)
    
    new_entry = pd.DataFrame([[datetime.now().strftime('%H:%M:%S'), ph, tds]], 
                             columns=st.session_state.water_log.columns)
    st.session_state.water_log = pd.concat([st.session_state.water_log, new_entry]).tail(15)

    with placeholder.container():
        c1, c2, c3 = st.columns(3)
        c1.metric("pH Level", f"{ph} pH", delta="Neutral" if 6.5 <= ph <= 8.5 else "Imbalance")
        c2.metric("TDS Purity", f"{tds} PPM")
        
        # Safety Logic
        if 6.5 <= ph <= 8.5 and tds < 300:
            status, css = "SAFE DRINKING WATER", "safety-safe"
        elif tds < 500:
            status, css = "MODERATE QUALITY (General Use)", "safety-warning"
        else:
            status, css = "CONTAMINATED - DO NOT DRINK", "safety-danger"
            
        st.markdown(f'<div class="{css}"><b>CURRENT STATUS: {status}</b></div>', unsafe_allow_html=True)

        fig = px.area(st.session_state.water_log, x='Time', y='TDS', title="TDS Concentration Trend (PPM)")
        st.plotly_chart(fig, use_container_width=True)
    time.sleep(2)
