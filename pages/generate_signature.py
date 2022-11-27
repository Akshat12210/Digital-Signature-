#genearte signature page
import streamlit as st
import Crypto
from Crypto import Random
from Crypto.PublicKey import RSA
from Crypto.Hash import SHA256
from Crypto.Signature import PKCS1_v1_5
from zipfile import ZipFile
import os

def rsakeys():  
     length=1024  
     privatekey = RSA.generate(length, Random.new().read)  
     publickey = privatekey.publickey()  
     return privatekey, publickey

def generate_signature(key, data):
    print("Generating Signature")
    h = SHA256.new(data)
    rsa = RSA.importKey(key)
    signer = PKCS1_v1_5.new(rsa)
    signature = signer.sign(h)
    f = open("D:/Digital-Signature-and-Verification/files/signature.txt", "wb")
    f.write(signature)
    f.close()
    return f


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
<a href="/"><button>Home</button></a><br>
<a href="verify"><button>Verify Signature</button></a>""",unsafe_allow_html=True)

zip=ZipFile("D:/Digital-Signature-and-Verification/files/files.zip",'w')

val=st.file_uploader("Upload data file")
if(val):
    f = open("D:/Digital-Signature-and-Verification/files/data.txt", "wb")
    for i in val:
        f.write(i)
    print(val)
    f.close()

    privatekey,publickey=rsakeys() #generating keys

    privatekey=privatekey.exportKey().decode()
    publickey=publickey.exportKey().decode()

    print(privatekey)
    print(publickey)

    f = open('D:/Digital-Signature-and-Verification/files/data.txt', 'rb') # opening a binary file
    content = f.read()
    print(content)
    sign=generate_signature(privatekey,content);


    f1 = open("D:/Digital-Signature-and-Verification/files/pub_key.txt", "w")
    f1.write(publickey)
    f1.close()
    f.close()

    os.chdir("D:/Digital-Signature-and-Verification/files/")
    zip.write("signature.txt")
    zip.write("pub_key.txt")
    zip.write("data.txt")
    zip.close()

    st.text("Please download the zip file containing signature, data file and your public key")
    with open('D:/Digital-Signature-and-Verification/files/files.zip', 'rb') as f:
            st.download_button('Download Zip', f, file_name='files.zip')  # Defaults to 'application/octet-stream'





