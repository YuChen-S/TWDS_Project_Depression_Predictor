import streamlit as st
import os
from PIL import Image
st.title('USER GUIDE')
st.write('''This brief user guide will help you go thorugh all the steps you need to get prediction for risk of depressive mood disorder.  
Please check this page carefully if you meet any trouble when using the application. Thanks!''')
st.sidebar.info(
    '''
    User requirement: \n
    For adult who needs a quick screening for risk of individual depressive mood disorders. 

    '''
)
st.sidebar.warning(
    '''
    Caution:\n
    Visit medical departments if any concerns, thanks.
    '''
    )

st.markdown("### --- Step 1: User basic info ---")
st.write('Enter your gender, age, height and weight. All these values would be used for prediction.')
user_info = Image.open(os.path.dirname(__file__)+'/user_guide_images/user_info.JPG')
st.image(user_info, caption='')

st.markdown("### --- Step 2: Questionnaire (Choice question) ---")
st.write('For this part, you will answer the questions with pre-defined options. Just select the one option which best matching your condition.')
question_part_1 = Image.open(os.path.dirname(__file__)+'/user_guide_images/question_part_1.JPG')
st.image(question_part_1, caption='')

st.markdown("### --- Step 3: Questionnaire (Filling question) ---")
st.write('''For this part, you will answer the questions by entering a number with limited range. 
You could use keyboard to enter the value or click the "+" or "-" buttons. 
''')
question_part_2 = Image.open(os.path.dirname(__file__)+'/user_guide_images/question_part_2.JPG')
st.image(question_part_2, caption='')

st.markdown("### --- Step 4: Start prediction ---")
st.write('''After finishing all the question, including user info, choice question and filling question, you could get your risk prediction by press
the "Start Prediction" button just below the questionnaire block.
''')
st.write('''You may wait for a few seconds before the result block shows up. There would be a blue progress bar indicating our apllication is alive.''')
prediction = Image.open(os.path.dirname(__file__)+'/user_guide_images/prediction.JPG')
st.image(prediction, caption='')


st.markdown("### --- Step 5: Check your result ---")
st.write('''Now your result is avaliable. You will see a score indicating the risk and a color spectrum showing your risk stratification. 
Please consult medical professionals if any problem. Never mistake this application as a precise diagnostic tool.
Thanks you very much!''')
result = Image.open(os.path.dirname(__file__)+'/user_guide_images/result.JPG')
st.image(result, caption='')
