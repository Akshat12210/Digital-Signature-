
# Digital Signature and Verification

- A digital signature is a way to verify the authenticity and integrity of a digital document or message.
- It is a unique code that is generated using the private key of a cryptographic key pair, and it is attached to the document or message to verify that it has not been altered in any way.
- The recipient of the message or document can then use the sender's public key to verify the digital signature and ensure that the message or document is authentic and has not been tampered with.


## Steps to run code
1.  Clone the repository
2.  Install all the libraries mentioned in requirements.txt file
3.  Launch the streamlit application by running command
``` streamlit run app.py ```
       

## Workflow

***

### 1. [Go to app · Streamlit](http://localhost:8501/)


### 2. Click on Generate Signature
![Step 2 screenshot](https://images.tango.us/workflows/5a1c96b3-11ee-4c14-8e7c-efd7c5f712de/steps/aa2b971d-c56d-4cff-8dc3-7dbd37563308/9f61abba-f620-4b58-a8d8-92aec5d631cd.png?crop=focalpoint&fit=crop&fp-x=0.5000&fp-y=0.5000&fp-z=1.0000&w=1200&mark-w=0.2&mark-pad=0&mark64=aHR0cHM6Ly9pbWFnZXMudGFuZ28udXMvc3RhdGljL21hZGUtd2l0aC10YW5nby13YXRlcm1hcmsucG5n&ar=1558%3A743)


### 3. Select the file for which you want to generate signature
![Step 3 screenshot](https://images.tango.us/workflows/5a1c96b3-11ee-4c14-8e7c-efd7c5f712de/steps/9d8498a9-90de-47e1-bc14-ad2865f2ae23/7fb34f89-15ee-42c5-908b-4988be95d9c2.png?crop=focalpoint&fit=crop&w=1200&mark-w=0.2&mark-pad=0&mark64=aHR0cHM6Ly9pbWFnZXMudGFuZ28udXMvc3RhdGljL21hZGUtd2l0aC10YW5nby13YXRlcm1hcmsucG5n&ar=1920%3A892)


### 4. A zip file will be generated which contains digital signature, public key and the actual file
![Step 4 screenshot](https://images.tango.us/workflows/5a1c96b3-11ee-4c14-8e7c-efd7c5f712de/steps/91e946d9-b0de-459c-a76c-d611bb8e5f09/578a983f-9daa-49e5-bacf-70b636bcbb61.png?crop=focalpoint&fit=crop&fp-x=0.4975&fp-y=0.4152&fp-z=1.2039&w=1200&mark-w=0.2&mark-pad=0&mark64=aHR0cHM6Ly9pbWFnZXMudGFuZ28udXMvc3RhdGljL21hZGUtd2l0aC10YW5nby13YXRlcm1hcmsucG5n&ar=1920%3A892)


### 5. Click on Download Zip
![Step 5 screenshot](https://images.tango.us/workflows/5a1c96b3-11ee-4c14-8e7c-efd7c5f712de/steps/24da2118-baef-4c05-aba1-179d7b194433/6d4a9678-24b9-4f97-9944-72e71b4838c5.png?crop=focalpoint&fit=crop&fp-x=0.3096&fp-y=0.6418&fp-z=2.6483&w=1200&mark-w=0.2&mark-pad=0&mark64=aHR0cHM6Ly9pbWFnZXMudGFuZ28udXMvc3RhdGljL21hZGUtd2l0aC10YW5nby13YXRlcm1hcmsucG5n&ar=1920%3A892)


### 6. Click on Verify Signature to go to the verfication page
![Step 6 screenshot](https://images.tango.us/workflows/5a1c96b3-11ee-4c14-8e7c-efd7c5f712de/steps/81cec266-a761-408a-9998-f4e326b52267/2ee4751b-a901-4cd1-b395-91042b822fc0.png?crop=focalpoint&fit=crop&fp-x=0.4975&fp-y=0.4152&fp-z=1.2039&w=1200&mark-w=0.2&mark-pad=0&mark64=aHR0cHM6Ly9pbWFnZXMudGFuZ28udXMvc3RhdGljL21hZGUtd2l0aC10YW5nby13YXRlcm1hcmsucG5n&ar=1920%3A892)


### 7. This is verify signature page upload the zip containing digital signature, file and public key
![Step 7 screenshot](https://images.tango.us/workflows/5a1c96b3-11ee-4c14-8e7c-efd7c5f712de/steps/7ca3d270-2f3c-49fb-8a90-1ede18213161/5d988a93-5af4-4b23-b6f8-d9b47451191f.png?crop=focalpoint&fit=crop&fp-x=0.5000&fp-y=0.4707&fp-z=1.0000&w=1200&mark-w=0.2&mark-pad=0&mark64=aHR0cHM6Ly9pbWFnZXMudGFuZ28udXMvc3RhdGljL21hZGUtd2l0aC10YW5nby13YXRlcm1hcmsucG5n&ar=1920%3A820)


### 8. Upload zip file using browse file option
![Step 8 screenshot](https://images.tango.us/workflows/5a1c96b3-11ee-4c14-8e7c-efd7c5f712de/steps/ba85f3cd-c0f6-4032-a854-75d534d0455d/452334c2-4c8c-42a1-a27e-b3107723a6d2.png?crop=focalpoint&fit=crop&w=1200&mark-w=0.2&mark-pad=0&mark64=aHR0cHM6Ly9pbWFnZXMudGFuZ28udXMvc3RhdGljL21hZGUtd2l0aC10YW5nby13YXRlcm1hcmsucG5n&ar=1920%3A820)


### 9. If the file is not tampered you will get success message 
![Step 9 screenshot](https://images.tango.us/workflows/5a1c96b3-11ee-4c14-8e7c-efd7c5f712de/steps/f6c7614c-a3af-4042-a3ed-ec8c7e0bd714/b92beffe-1bff-493b-a814-648084b3a7f7.png?crop=focalpoint&fit=crop&fp-x=0.4984&fp-y=0.4262&fp-z=1.1714&w=1200&mark-w=0.2&mark-pad=0&mark64=aHR0cHM6Ly9pbWFnZXMudGFuZ28udXMvc3RhdGljL21hZGUtd2l0aC10YW5nby13YXRlcm1hcmsucG5n&ar=1920%3A820)


### 10. If the file is tampered you will get  
![Step 10 screenshot](https://images.tango.us/workflows/5a1c96b3-11ee-4c14-8e7c-efd7c5f712de/steps/cd16a457-23bb-4d29-9258-2528d33c3d22/cf75ab3b-c470-4fc0-bf05-160cf053f2cd.png?crop=focalpoint&fit=crop&fp-x=0.5000&fp-y=0.5000&fp-z=1.0000&w=1200&mark-w=0.2&mark-pad=0&mark64=aHR0cHM6Ly9pbWFnZXMudGFuZ28udXMvc3RhdGljL21hZGUtd2l0aC10YW5nby13YXRlcm1hcmsucG5n&ar=1648%3A792)


***
