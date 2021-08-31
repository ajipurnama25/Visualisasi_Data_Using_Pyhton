import streamlit as st
import pandas as pd
import mysql.connector

def app():
    conn = mysql.connector.connect( host="localhost",
                                    port="3306",
                                    user="root",
                                    passwd="",
                                    db="tugbes"
                                  )
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM heart_failure_clinical_records_dataset LIMIT 1,300")
    data = cursor.fetchall()
    df = pd.DataFrame(data, columns=['age',
                                     'anaemia',
                                     'creatinine_phosphokinase',
                                     'diabetes',
                                     'ejection_fraction',
                                     'high_blood_pressure',
                                     'platelets',
                                     'serum_creatinine',
                                     'serum_sodium',
                                     'sex',
                                     'smoking',
                                     'time',
                                     'DEATH_EVENT']
                      )
    df.to_csv("jantungg.csv")
    df = pd.read_csv('jantungg.csv')
    st.subheader("Data diambil dari kaggle :")#menampilkan teks yang dibuat
    st.markdown("[DOWNLOAD](https://www.kaggle.com/andrewmvd/heart-failure-clinical-data)") #markdown digunakan untuk menuliskan dokumentasi.
    df.drop('Unnamed: 0',axis='columns', inplace=True)#menghapus yang tidak penting
    st.dataframe(df) # agar terlihat rapi pada data yang akan disajikan

    shwdata = st.multiselect('Pilih Kolom yang mau ditampilkan:', df.columns, default=[])#membuat banyak pilihan
    st.write(df[shwdata])
