#verification page
#home page
import streamlit as st
st.set_page_config(initial_sidebar_state="collapsed")

st.text("Cryptography Project")

st.markdown(""" 
<style>
 .css-1vencpc{
        display: none;
    }
* {
    margin:0;
    padding:0;
}
button {
background-color: rgb(19, 23, 32); 
  border: 1px solid rgba(250, 250, 250, 0.2);
  color: white;
  padding: 0.25rem 0.75rem;
  border-radius:0.25rem;
  text-align: center;
  text-decoration: none;
  display: inline-flex;
  line-height:1.6;
  width:auto;

    -webkit-box-align: center;
    align-items: center;
    -webkit-box-pack: center;
    justify-content: center;
    font-weight: 400;
    
}
a{
    text-decoration:none ;
}
a:hover{
    text-decoration:none;
}
button:hover{
  border: 1px solid rgb(255, 75, 75);
  color: rgb(255, 75, 75);
}
</style>
<a href="/"><button>Home</button></a>
<a href="generate_signature"><button>Generate Signature</button></a>
""",unsafe_allow_html=True)



