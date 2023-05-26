import streamlit as st
import pickle
import numpy as np

# import the model
pipe = pickle.load(open('pipe12.pkl','rb'))
df = pickle.load(open('df.pkl','rb'))

st.title("Laptop Price Predictor")

# brand
company = st.selectbox('Brand',df['Company'].unique())

# type of laptop
type = st.selectbox('Type',df['TypeName'].unique())

# Ram
ram = st.selectbox('RAM(in GB)',[2,4,6,8,12,16,24,32,64])

left_column, middle_column, right_column = st.columns(3)
with left_column:
    # Weight input
    weight = st.number_input("Weight of laptop in kg")

with middle_column:
    # Touchscreen
    touchscreen = st.selectbox("Touchscreen", ["No", "Yes"])

with right_column:
    # IPS display
    ips = st.selectbox("IPS Display", ["No", "Yes"])

# making 3 cols left_column, middle_column, right_column
left_column, middle_column, right_column = st.columns(3)
with left_column:
    # screen size
    Screen_size = st.number_input("Screen Size (in Inches)")

with middle_column:
    # resolution
  resolution = st.selectbox('Screen Resolution',['1920x1080', '1366x768', '1600x900', '3840x2160', '3200x1800', '2880x1800', '2560x1600','2560x1440', '2304x1440'])
with right_column:
    # cpu input
    cpu = st.selectbox("CPU Brand", df["Cpu_brand"].unique())

# making 3 cols left_column, middle_column, right_column
left_column,  right_column = st.columns(2)
with left_column:
    # hdd input
    hdd = st.selectbox("HDD(in GB)", [0, 128, 256, 512, 1024, 2048])


with right_column:
    # ssd input
    ssd = st.selectbox("SSD(in GB)", [0, 8, 128, 256, 512, 1024])

gpu = st.selectbox('GPU',df['Gpu_brand'].unique())

os = st.selectbox('OS',df['os'].unique())

if st.button('Predict Price'):
    # query
    ppi = None
    if touchscreen == 'Yes':
        touchscreen = 1
    else:
        touchscreen = 0

    if ips == 'Yes':
        ips = 1
    else:
        ips = 0

    X_res = int(resolution.split('x')[0])
    Y_res = int(resolution.split('x')[1])
    ppi = ((X_res**2) + (Y_res**2))**0.5/screen_size
    query = np.array([company,type,ram,weight,touchscreen,ips,ppi,cpu,hdd,ssd,gpu,os])

    query = query.reshape(1,12)
    st.title("The predicted price of this configuration is  : ₹ " + str(int(np.exp(pipe.predict(query)[0]))))
