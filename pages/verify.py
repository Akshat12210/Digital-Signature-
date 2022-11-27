#verification page
import streamlit as st
import Crypto
from Crypto import Random
from Crypto.PublicKey import RSA
from Crypto.Hash import SHA256
from Crypto.Signature import PKCS1_v1_5
from zipfile import ZipFile


def verify_signature(key, data, sig_f):
    print("Verifying Signature")
    h = SHA256.new(data)
    rsa = RSA.importKey(key)
    signer = PKCS1_v1_5.new(rsa)
    # with open(sig_f, 'rb') as f: signature = f.read()
    rsp = "Success" if (signer.verify(h, sig_f)) else " Verification Failure"
    if(rsp=="Success"):
        st.success("Success, File is not tampered")
    else:
        st.error("Verifcation Failure, File is tampered")

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

st.write("Verify Signature")
uploaded_zip = st.file_uploader('XML File', type="zip")
if(uploaded_zip):
    with ZipFile(uploaded_zip, 'r') as zip_ref:
        zip_ref.extractall("D:/Digital-Signature-and-Verification/files/uploads")
    f = open('D:/Digital-Signature-and-Verification/files/uploads/data.txt', 'rb') # opening a binary file
    content = f.read()
    print(content)
    f1 = open('D:/Digital-Signature-and-Verification/files/uploads/signature.txt', 'rb') # opening a binary file
    sign = f1.read()
    print(sign)

    f2 = open("D:/Digital-Signature-and-Verification/files/uploads/pub_key.txt", "r")
    publicKey=f2.read()
    check=verify_signature(publicKey,content,sign)
    f1.close()
    f.close()
    f2.close()

