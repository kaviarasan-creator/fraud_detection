import streamlit as st
import joblib
import numpy as np
st.title("house pricing prediction")
st.divider()
st.write("this app is used to predict the house pricing")
st.divider()
bedrooms=st.number_input("Number of bedrooms",min_value=0,value=0)
bathrooms=st.number_input("Number of bathrooms",max_value=0,value=0)
livingarea=st.number_input("Living area",min_value=0,value=2000)
condition=st.number_input("Condition",min_value=0,value=0)
numberofschools=st.number_input("Number of school",min_value=0,values=0)
st.divider
model=joblib.load("model.pkg")
x=[[bedrooms,bathrooms,livingarea,condition,numberofschools]]
predictbutton=st.button("predict")
if predictbutton:
    st.balloons()
    x_array=np.array(x)
    prediction=model.predict(x_array)
    st.write(f"price prediction is {prediction}")

else:
    st.write("please use the predict button")
             


