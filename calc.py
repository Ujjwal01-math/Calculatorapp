import streamlit as st
import random
name=st.sidebar.text_input("Enter your name")
if name: 
    cc=st.sidebar.selectbox("Select the Operation",["None","Calculator","Currency converter"])
    if(cc=="Calculator"):
       st.title(f"Hello {name}")
       st.markdown("### Welcome to the Calculator 🙏") 
       a=st.number_input("Enter first number",min_value=0,step=1)
       sc = st.radio("Select operator", ['+', '-', '*', '%'],width=150, horizontal=True)
       #sc=st.selectbox("Select operation",["None","+","-","*","%"])
       b=st.number_input("Enter second number",min_value=1,step=1)
       if(sc=="+"):
          c=a+b
       elif(sc=="-"):
          c=a-b
       elif(sc=="*"):
          c=a*b 
       elif(sc=="%"):
          if(a==0 or b==0):
             c="Udefined"
          else :
             c=a/b
       elif(sc=="None"):
          c="Please select the Operation" 
    
       st.success(f"output = {c}")   
    elif(cc=="Currency converter")  :
       st.title(f"Hello {name}")
       st.markdown("### Welcome to Currency Converter 🙏") 
       a=st.radio("Select Currency",["Dollor","Euro","Yen","Ruble"])
       #a=st.selectbox("Select Currency",["Dollor","Euro","Yen","Ruble"])   
       b=st.number_input("Enter Amount",min_value=0,step=1)
       if(a=="Dollor"):
          st.write("Current rate is 93")
          c=b*93
       elif(a=="Euro"):
          st.write("Current rate is 108")
          c=b*108
       elif(a=="Yen"):
           st.write("Current rate is 0.59")
           c=b*0.59
       elif(a=="Ruble"):
          st.write("Current rate is 0.9")
          c=b*0.9
       st.success(f"Converted Value = ₹ {c}")  
   
               
  
               




   
   
