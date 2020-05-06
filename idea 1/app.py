import streamlit as st
# To make things easier later, we're also importing numpy and pandas for
# working with sample data.
import numpy as np
import pandas as pd
from PIL import Image
import pickle


filename = 'diamondsmodel.sav'
loaded_model = pickle.load(open(filename, 'rb'))

st.title('Diamond price estimator')
carat = st.sidebar.slider("What is the size of the Diamond ?",0.1,5.0,2.4,0.1)

cut = st.sidebar.radio("What is the type of cut?",
('Ideal',"Premium","Good","Very Good", "Fair"))
if cut =='Ideal':cut1 = 1
if cut =='Premium':cut1 = 2
if cut =='Good':cut1 = 3
if cut =='Very Good':cut1 = 4
if cut =='Fair':cut1 = 5

colour = st.sidebar.radio("What is the colour?", ("J","I", "H", "G","F", "E","D"))
if colour =="J": colour1=1
if colour =="I": colour1=2
if colour =="H": colour1=3
if colour =="G": colour1=4
if colour =="F": colour1=5
if colour =="E": colour1=6
if colour =="D": colour1=7

clarity  = st.sidebar.radio("What is the type of cut?",
("I3","I2","I1","SI2", "SI1","VS2","VS1","VVS2", "VVS1","IF","FL"))
if clarity =="I3": clarity =1
if clarity =="I2": clarity =2
if clarity =="I1": clarity =3
if clarity =="SI2": clarity =4
if clarity =="SI1": clarity =5
if clarity =="VS2": clarity =6
if clarity =="VS1": clarity =7
if clarity =="VVS2": clarity =8
if clarity =="VVS1": clarity =9
if clarity =="IF": clarity =10
if clarity =="FL": clarity =11
depth = st.sidebar.slider("What is the depth?",43,80,60,1 )

table = st.sidebar.slider("What is the table size ?",43.0,95.0,70.0,0.1)

x = st.sidebar.slider("What is the X dimension?",0.1,11.0,5.0,0.1)
y= st.sidebar.slider("What is the Y dimension?",0.1,58.0,28.0,0.1)
z= st.sidebar.slider("What is the Z dimension?",0.1,31.0,15.0,0.1)
cal_img = Image.open('images/clarity.jpg')
size_img = Image.open('images/size.png')
st.image(cal_img,"Clarity chart",use_column_width=True)
st.image(size_img,"Diamond dimensions", use_column_width=True)

btn = st.sidebar.button("Get Price")
if btn:
    new_data = [carat, cut1, colour1,clarity,depth,table,x,y,z]
    #st.write("Cut type is: ", cut, "Value is: ", cut1)
    result = int(loaded_model.predict([new_data]))
    st.write("The price of the diamond is: ", result)
    #print(type(result))
    
