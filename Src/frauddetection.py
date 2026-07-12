import streamlit as st
import pandas as pd
import numpy as np
import joblib



model=joblib.load('/Users/joestar/Fraud detection project/Model/fraud_detection_model.pkl')
st.title("Fraud Detection App")

st.markdown("This app predicts whether a transaction is fraudulent or not based on the input features.")
st.markdown("Please enter the following details to make a prediction:")
st.divider()
transaction_type = st.selectbox("Transaction Type", ["PAYMENT", "TRANSFER", "CASH_OUT", "DEPOSIT", "CASH_IN"])
amount=st.number_input("Amount", min_value=0.0, step=0.01)
oldbalanceOrg=st.number_input("Old Balance of Origin Account", min_value=0.0, step=0.01)
newbalanceOrig=st.number_input("New Balance of Origin Account", min_value=0.0, step=0.01)
oldbalanceDest=st.number_input("Old Balance of Destination Account", min_value=0.0, step=0.01)
newbalanceDest=st.number_input("New Balance of Destination Account", min_value=0.0, step=0.01)  

if(st.button("Predict")):
    input_data=pd.DataFrame([[transaction_type,amount,oldbalanceOrg,newbalanceOrig,oldbalanceDest,newbalanceDest]],columns=['type','amount','oldbalanceOrg','newbalanceOrig','oldbalanceDest','newbalanceDest'])
    prediction=model.predict(input_data)
    if(prediction[0]==1):
        st.error("The transaction is fraudulent.")
    else:
        st.success("The transaction is not fraudulent.")
