import streamlit as st
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt 

# set_page_config adalah metode yang digunakan untuk mengubah setup halaman
st.set_page_config(
    page_title="Exploratory Data Analysis App",
    layout="wide"
)

# persiapkan parameter konfigurasi
path_dataset = "assets/"
filename = "titanic.csv"

# baca data
df = pd.read_csv(f"{path_dataset}{filename}")
df1 = df.copy()
df1.dropna()

# container Title
with st.container(border=True):
    st.title("Analisis Survivor Pada Peristiwa Titanic")
    st.text("Oleh Stephen Hendry")
    
# tampilkan data
st.dataframe(
    df.sample(10),
    use_container_width=True,
    hide_index=True
    )


with st.container():
    con2_col_1,con2_col_2 = st.columns([2,1])
    with con2_col_1:
        fig, ax = plt.subplots()
        sns.histplot(data=df1, x="Age")
        st.write(fig)
    with con2_col_2:
        st.markdown('''
                <style>
                    .analisis_1{
                        font-size: 30px;
                    }
                </style>
                    ''',
                    unsafe_allow_html=True
                    )
        
        st.markdown('''
                    <p class = "analisis_1">Berdasarkan grafik disamping, mayoritas penumpang Titanic adalah di usia 10 - 50 tahun</p>''',
                    unsafe_allow_html=True
                    )
