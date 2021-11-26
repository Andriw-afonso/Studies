import streamlit as st 

@st.cache()
  
# function input
def prediction(Cholesterol,ApLo,ApHi,Smoke_yes,Age):
    a='Hello'
    return a
      
  
# webapp  
def main():       
    # Config web
    html_temp = """ 
    <div style ="background-color:yellow;padding:13px"> 
    <h1 style ="color:black;text-align:center;">Diagnóstico precoce cardiovascular</h1> 
    </div> 
    """
      
    # display 
    st.markdown(html_temp, unsafe_allow_html = True) 
      
    # Imput
    Cholesterol = st.selectbox('Nível de colesterol',('1','2','3'))
    ApLo =        st.number_input('Pressão diastólica')
    ApHi =        st.number_input('Pressão sistólica') 
    Smoke_yes =   st.selectbox('Fumante',('sim','nao')) 
    Age =         st.number_input('Idade') 

    result =""
      
    # Predict 
    if st.button("Predict"): 
        result = prediction(Cholesterol,ApLo,ApHi,Smoke_yes,Age) 
        st.success('Estado de saúde: {}'.format(result))
        
     
if __name__=='__main__': 
    main()