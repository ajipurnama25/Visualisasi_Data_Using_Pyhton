import streamlit as st

class MultiApp:

    def _init_(self): #konfigurasi object yang telah di-construct.
        self.apps = []

    def add_app(self, title, func):
        self.apps.append({"title": title,"function": func})

    def run(self):
        app = st.selectbox('Navigation',self.apps,format_func=lambda app: app['title'])
        app['function']()