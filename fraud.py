import streamlit as st
import pandas as pd
import joblib

model=joblib.load("fraud_detection_pipeline.pkl")
st.title("Fraud detection app")
st.markdown("please enter transaction detail use predict button")
st.divider()
transaction_type=st.selectbox("Transaction Type",["PAYMENT","TRANSFER","CASH_OUT","DEPOSIT"])
amount=st.number_input("Amount",min_value=0.0,value=1000.0)
oldbalanceOrg=st.number_input("Old Balance(Sender)",min_value=0.0,value=10000.0)
newbalanceOrig=st.number_input("New Balance (sender)",min_value=0.0,value=10000.0)
oldbalanceDest=st.number_input("Old Balance (reciever)",min_value=0.0,value=10000.0)
newbalanceDest=st.number_input("New Balance (reciever)",min_value=0.0,value=10000.0)
if st.button("predict"):
    input_data=pd.DataFrame([{
        "type":transaction_type,
        "amount": amount,
        "oldbalanceOrg": oldbalanceOrg,
        "newbalanceOrig":newbalanceOrig,
        "oldbalanceDest":oldbalanceDest,
        "newbalanceDest":newbalanceDest
    }])
    prediction=model.predict(input_data)[0]
    st.subheader(f"prediction:'{int(prediction)}'")
    if prediction==1:
        st.error("This transaction can be fraud")
    else:
        st.success("This transcation looks like not fraud")    
