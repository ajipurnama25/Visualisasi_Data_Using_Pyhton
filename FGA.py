import streamlit as st
from multipel import MultiApp
from apps import data,visualisasi,model

app = MultiApp()

st.markdown("""
# FINAL PROJECT FGA 2021

Bismillahirrahmanirrahim Semoga Berkah
""")

app.add_app("Data", data.app)
app.add_app("Visualisasi", visualisasi.app)
app.add_app("Model", model.app)
app.run()