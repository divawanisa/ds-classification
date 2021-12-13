import numpy as np
import pickle
import pandas as pd
import streamlit as st
from PIL import Image

def welcome():
    return "welcome all"
def predict(umur, produk, nilai_produk, jumlah_review, tempat_beli, jenis, kategori, tipe_kulit,waktu_pemakaian, penggunaan, kepuasan, warna_kulit, tone_kulit, value):
    cols = [1,2,3,4,5,6,7,8,9,10,11,12,13,14]
    df_1 = pd.read_csv('data_bersih.csv',usecols=cols)
    df_1.TotalCharges = pd.to_numeric(df_1.TotalCharges, errors='coerce')
    model = pickle.load(open("model.pkl", "rb"))
    data = [[umur, produk, nilai_produk, jumlah_review, tempat_beli, jenis, kategori, tipe_kulit,waktu_pemakaian, penggunaan, kepuasan, warna_kulit, tone_kulit, value]]
    new_df = pd.DataFrame(data, columns = ['umur', 'produk', 'nilai_produk', 'jumlah_review', 'tempat_beli', 'jenis', 'kategori', 'tipe_kulit','waktu_pemakaian', 'penggunaan', 'kepuasan', 'warna_kulit', 'tone_kulit', 'value'])
    

    df_2 = pd.concat([df_1, new_df], ignore_index = True) 
    df_2.dropna(how = 'any', inplace=True)
    labels = ["{0} - {1}".format(i, i + 11) for i in range(1, 72, 12)]
    df_2['tenure_group'] = pd.cut(df_2.tenure.astype(int), range(1, 80, 12), right=False, labels=labels)
    df_2.drop(columns= ['tenure'], axis=1, inplace=True) 
    
    new_df__dummies = pd.get_dummies(data)
    probablity = model.predict_proba(new_df__dummies.tail(1))[:,1]
    
    return probablity


def main():
    st.title("Variabel penentu")
    html_temp = """
    <div style="background-color:tomato;padding:10px">
    <h2 style="color:white;text-align:center;">Telco_Churn</h2>
    </div>
    """ 
    # Text Input as string
    st.markdown(html_temp,unsafe_allow_html=True)
    umur = st.text_input("umur","Type Here")
    produk = st.text_input("produk","Type Here")
    nilai_produk = st.text_input("nilai_produk","Type Here")
    jumlah_review = st.text_input("jumlah_review","Type Here")
    tempat_beli = st.text_input("tempat_beli","Type Here")
    jenis = st.text_input("jenis","Type Here")
    kategori = st.text_input("kategori","Type Here")
    tipe_kulit = st.text_input("tipe_kulit","Type Here")
    waktu_pemakaian = st.text_input("waktu_pemakaian","Type Here")
    penggunaan = st.text_input("penggunaan","Type Here")
    kepuasan = st.text_input("kepuasan","Type Here")
    warna_kulit=st.text_input("warna_kulit","Type Here")
    tone_kulit=st.text_input("tone_kulit","Type Here")

    result = ""
    if st.button("predict"):
        result = predict(gender,SeniorCitizen,Partner,Dependents,tenure,PhoneService,MultipleLines,InternetService,OnlineSecurity,OnlineBackup,DeviceProtection,TechSupport,StreamingTV,StreamingMovies,Contract,PaperlessBilling,PaymentMethod,MonthlyCharges,TotalCharges)
    st.success('output is {}'.format(result))    
    
if __name__=='__main__':
    main()
