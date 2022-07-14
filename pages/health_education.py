import streamlit as st
import os
from PIL import Image
st.title('About Depression Mood Disorders')
st.write('''You many find some useful infomation about depression in this page. Please visit a doctor if any concerns. Thanks!''')

st.sidebar.info(
    '''
    Reference: \n
    National Institutes of Health (NIH) NIH Publication No. 21-MH-8079
    '''
)

depression_ss = Image.open(os.path.dirname(__file__)+'/health_education_images/depression_ss.JPG')
st.image(depression_ss, caption='')

depression_care_self = Image.open(os.path.dirname(__file__)+'/health_education_images/depression_care_self.JPG')
st.image(depression_care_self, caption='')

depression_care_other = Image.open(os.path.dirname(__file__)+'/health_education_images/depression_care_other.JPG')
st.image(depression_care_other, caption='')