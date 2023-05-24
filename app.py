import streamlit as st
import pickle
#import the model

pipe = pickle.load(open('pipe.pkl','rb'))
df = pickle.load(open('df.pkl','rb'))


st.title("Laptop Predictor")

#brand
company = st.selectbox('Brand',df['Company'].unique())

#Type
type = st.selectbox('Type',df['TypeName'].unique())

#Ram

type = st.selectbox('Ram(in GB)',[2,4,6,8,12,16,24,32,64])

#weight

weight = st.number_input('Weight of the Laptop')

# TouchScreen

Touchscreen = st.selectbox('Tounchscreen',['No','Yes'])

#IPS
IPS = st.selectbox('IPS',['No','Yes'])

#Screen Size

Screen_size = st.number_input('Screen size')

#resolution

resolution = st.selectbox('Screen Resolution',['1920x1080','1366x768','1600x900','3840x2160','2880x1800','2560x1440','2304x1440'])

#cpu
cpu = st.selectbox('Brand',df['Cpu Brand'].unique())

#HDD

hdd = st.selectbox('HDD(in GB)',df['0,128,256,512,1024,2048'].unique())

ssd = st.selectbox('SSD(in GB)',df['0,128,256,512,1024'].unique())

gpu = st.selectbox('Gpu',df['Gpu brand'].unique())

os = st.selectbox('OS',df['os'].unique())

if st.button('Predict Price'):
    pass
