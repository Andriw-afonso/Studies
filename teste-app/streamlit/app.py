import streamlit as st 

@st.cache()
  
# defining the function which will make the prediction using the data which the user inputs 
def prediction(Cholesterol,ApLo,ApHi,Smoke_yes,Age):
  
    return print('Hello')
      
  
# this is the main function in which we define our webpage  
def main():       
    # front end elements of the web page 
    html_temp = """ 
    <div style ="background-color:yellow;padding:13px"> 
    <h1 style ="color:black;text-align:center;">Streamlit Loan Prediction ML App</h1> 
    </div> 
    """
      
    # display the front end aspect
    st.markdown(html_temp, unsafe_allow_html = True) 
      
    # following lines create boxes in which user can enter data required to make prediction 
    Cholesterol = st.selectbox('Cholesterol',('1','2','3'))
    ApLo =        st.selectbox('Pressão diastólica',('0','200'))
    ApHi =        st.selectbox('Pressão sistólica',('80','300')) 
    Smoke_yes =   st.selectbox('Fumante',('sim','nao')) 
    Age =         st.selectbox('Idade',('0','130')) 

    ApplicantIncome = st.number_input("Applicants monthly income") 
    LoanAmount = st.number_input("Total loan amount")
    Credit_History = st.selectbox('Credit_History',("Unclear Debts","No Unclear Debts"))
    result =""
      
    # when 'Predict' is clicked, make the prediction and store it 
    if st.button("Predict"): 
        result = prediction(Gender, Married, ApplicantIncome, LoanAmount, Credit_History) 
        st.success('Your loan is {}'.format(result))
        print(LoanAmount)
     
if __name__=='__main__': 
    main()