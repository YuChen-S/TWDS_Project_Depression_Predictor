import time
import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib as mpl
import joblib
import tqdm
import lightgbm as lgb
import sklearn
from flare.preprocessing import VaniilaLGBMPreprocessor
from flare.inference import ProbabilisticBinaryClassifier
from user_answer_preprocess import *
from utils import *

###### webpage settings ######
st_website_setting()

###### sidebar info ######
st_sidebar_info()

###### Main page title and user guide
st_title_info()

###### user info block ######
df_user_answer = generate_user_input_df()
with st.container():
    st.subheader('User basic info')
    # first row
    user_col_1_1, user_col_1_2 = st.columns(2)
    with user_col_1_1:
        user_sex = st.selectbox('What is your biological gender?', ('Male', 'Female',), )# Male: 1, Female: 2
    with user_col_1_2:
        user_age = st.number_input('How old are you?', min_value=18, max_value=120, value=30, )
    df_user_answer.loc[0,'SEXVAR'] = 1 if user_sex=='Male' else 2
    df_user_answer.loc[0,'_AGEG5YR'] = user_AGEG5YR(user_age)
    df_user_answer.loc[0,'_AGE80'] = user_age
    # second row
    user_col_2_1, user_col_2_2 = st.columns(2)
    with user_col_2_1:
        user_height = st.number_input('Your height in centimeter', min_value=0.0, max_value=250.0, value=160.0, step=1.0,)
    with user_col_2_2:
        user_weight = st.number_input('Your weight in kilogram', min_value=0.0, max_value=250.0, value=60.0, step=1.0,)
    df_user_answer.loc[0,'HTM4_C'] = 1
    df_user_answer.loc[0,'HTM4_N'] = user_height
    df_user_answer.loc[0,'WTKG3_C'] = 1
    df_user_answer.loc[0,'WTKG3_N'] = user_weight
    df_user_answer.loc[0,'_BMI5_C'] = 1
    df_user_answer.loc[0,'_BMI5_N'] = user_weight/((user_height/100)**2)
st.write('---')

###### question block ######
with st.container():
    st.markdown('### Please answer the following questions and then click the *"Start prediction"* button.')
    st.subheader('Part 1: Multiple choice questions')
    # first row
    select_col_1_1, select_col_1_2 = st.columns(2)
    with select_col_1_1:
        var_MENT14D = st.selectbox(
             'Frequency of not good mental health status during last month:',
             ('0 days', '1-13 days', '14-31 days','Not Sure',))
    with select_col_1_2:
        varDECIDE = st.selectbox(
             'For physical or mental reason, do you have difficulty concentrating, remembering, or making decisions? ',
             ('Yes', 'No', 'Not Sure',), 
             index=1,)
    df_user_answer.loc[0,'_MENT14D'] = user_MENT14D(var_MENT14D)
    df_user_answer.loc[0,'DECIDE'] = userDECIDE(varDECIDE)
    # second row
    select_col_2_1, select_col_2_2 = st.columns(2)
    with select_col_2_1:
        varDIFFALON = st.selectbox(
             'For physical or mental reason, do you have difficulty doing errands alone such as visiting a doctor or shopping? ',
             ('Yes', 'No', 'Not Sure',), 
             index=1,)
    with select_col_2_2:
        varACEDEPRS = st.selectbox(
             'Did you live with anyone who was depressed, mentally ill, or suicidal?',
             ('Yes', 'No', 'Not Sure',), 
             index=1,)
    df_user_answer.loc[0,'DIFFALON'] = userDIFFALON(varDIFFALON)
    df_user_answer.loc[0,'ACEDEPRS'] = userACEDEPRS(varACEDEPRS)
    # third row
    select_col_3_1, select_col_3_2 = st.columns(2)
    with select_col_3_1:
        varEMPLOY1 = st.selectbox(
             'For your employment status, are you currently…?',
             ('Employed for wages', 'Self-employed', 'Out of work for 1 year or more', 'Out of work for less than 1 year', 'A homemaker', 'A student', 'Retired', \
                'Unable to work', 'Refused'))
    with select_col_3_2:
        varGENHLTH = st.selectbox(
             'Would you say that in general your health is:',
             ('Excellent', 'Very good', 'Good', 'Fair', 'Poor', 'Not Sure',))
    df_user_answer.loc[0,'EMPLOY1'] = userEMPLOY1(varEMPLOY1)
    df_user_answer.loc[0,'GENHLTH'] = userGENHLTH(varGENHLTH)
    # fourth row
    select_col_4_1, select_col_4_2 = st.columns(2)
    with select_col_4_1:
        varMARITAL = st.selectbox(
             'For your marital status, are you:',
             ('Married', 'Divorced', 'Widowed', 'Separated', 'Never married', 'A member of an unmarried couple', 'Refused',))
    with select_col_4_2:
        var_SMOKER3 = st.selectbox(
             'Four-level smoker status:',
             ('Current smoker - now smokes every day', 'Current smoker - now smokes some days', 'Former smoker', 'Never smoked', 'Refused'), 
             index=3,
             )
    df_user_answer.loc[0,'MARITAL'] = userMARITAL(varMARITAL)
    df_user_answer.loc[0,'_SMOKER3'] = user_SMOKER3(var_SMOKER3)
    # fifth row
    select_col_5_1, select_col_5_2 = st.columns(2)
    with select_col_5_1:
        var_DRDXAR2 = st.selectbox(
             'Have you had a doctor diagnose you as having some form of arthritis?',
             ('Diagnosed with arthritis', 'Not diagnosed with arthritis', 'Not Sure',), 
             index=1,)
    with select_col_5_2:
        varSOFEMALE = st.selectbox(
             'Which of the following best represents how you think of yourself? ',
             ('Lesbian or Gay', 'Straight, that is, not gay', 'Bisexual', 'Something else', 'Refused',), 
             index=1,
             )
    df_user_answer.loc[0,'_DRDXAR2'] = user_DRDXAR2(var_DRDXAR2)
    df_user_answer.loc[0,'SOFEMALE'] = userSOFEMALE(varSOFEMALE)
    # sixth row
    select_col_6_1, select_col_6_2 = st.columns(2)
    with select_col_6_1:
        varRENTHOM1 = st.selectbox(
             'Do you own or rent your home?',
             ('Own', 'Rent', 'Other arrangement',))
    with select_col_6_2:
        var_TOTINDA = st.selectbox(
             'Doing exercise during past 30 days other than regular job',
             ('Yes', 'No', 'Not Sure',), 
             )
    df_user_answer.loc[0,'RENTHOM1'] = userRENTHOM1(varRENTHOM1)
    df_user_answer.loc[0,'_TOTINDA'] = user_TOTINDA(var_TOTINDA)
    # seventh row
    select_col_7_1, select_col_7_2 = st.columns(2)
    with select_col_7_1:
        varEDUCA = st.selectbox(
             'What is the highest grade or year of school (education level) you completed?',
             ('Never attended school or only kindergarten', 'Elementary', 'Some high school', 'High school graduate', \
                'Some college or technical school', 'College graduate', 'Refused'), 
                index=3,)
    with select_col_7_2:
        varPERSDOC2 = st.selectbox(
             'Do you have one person you think of as your personal doctor or health care provider?',
             ('Yes, only one', 'More than one', 'No', 'Not Sure',), 
             )
    df_user_answer.loc[0,'EDUCA'] = userEDUCA(varEDUCA)
    df_user_answer.loc[0,'PERSDOC2'] = userPERSDOC2(varPERSDOC2)    
    # eighth row
    select_col_8_1, select_col_8_2 = st.columns(2)
    with select_col_8_1:
        varINCOME2 = st.selectbox(
             'Is your annual household income from all sources',
             ('Less than $10,000', '$10,000 to less than $15,000', '$15,000 to less than $20,000', '$20,000 to less than $25,000', '$25,000 to less than $35,000', \
                '$35,000 to less than $50,000', '$50,000 to less than $75,000', '$75,000 or more', 'Not Sure', 'Refused'), 
                index=4,)
    with select_col_8_2:
        var_URBSTAT = st.selectbox(
             'Urban/Rural Status',
             ('Urban counties', 'Rural counties', 'Not Sure',), 
             )
    df_user_answer.loc[0,'INCOME2'] = userINCOME2(varINCOME2)
    df_user_answer.loc[0,'_URBSTAT'] = user_URBSTAT(var_URBSTAT)

    ################# Part 2 ###################
    st.subheader('Part 2: Blank filling questions')
    # first row
    num_col_1_1, num_col_1_2 = st.columns(2)
    with num_col_1_1:
        varMENTHLTH = st.number_input('For how many days during the past 30 days was your mental health not good', min_value=0, max_value=30,)
    with num_col_1_2:
        varPOORHLTH = st.number_input('During past 30 days, for how many days did poor physical or mental health keep you from doing usual activities?', min_value=0, max_value=30,)
    num_col_2_1, num_col_2_2 = st.columns(2)
    with num_col_2_1:
        varPHYSHLTH = st.number_input('For how many days during the past 30 days was your physical health not good?', min_value=0, max_value=30,)
    with num_col_2_2:
        varFALL12MN = st.number_input('In the past 12 months, how many times have you fallen? (Enter 77 if not sure)', min_value=0, max_value=77,)
    num_col_3_1, num_col_3_2 = st.columns(2)
    with num_col_3_1:
        varSLEPTIM1 = st.number_input('On average, how many hours of sleep do you get in a 24-hour period?', min_value=0, max_value=24, value=8)
    with num_col_3_2:
        varALCDAY5 = st.number_input('During the past 30 days, how many days did you have at least one drink of any alcoholic beverage?', min_value=0, max_value=30,)
    df_user_answer.loc[0,'MENTHLTH_C'] = 1
    df_user_answer.loc[0,'MENTHLTH_N'] = varMENTHLTH
    df_user_answer.loc[0,'POORHLTH_C'] = 1 if varPOORHLTH != 0 else 8
    df_user_answer.loc[0,'POORHLTH_N'] = varPOORHLTH
    df_user_answer.loc[0,'PHYSHLTH_C'] = 1
    df_user_answer.loc[0,'PHYSHLTH_N'] = varPHYSHLTH
    df_user_answer.loc[0,'FALL12MN_C'] = 1 if varFALL12MN != 77 else -1
    df_user_answer.loc[0,'FALL12MN_N'] = varFALL12MN
    df_user_answer.loc[0,'SLEPTIM1_C'] = 1
    df_user_answer.loc[0,'SLEPTIM1_N'] = varSLEPTIM1
    df_user_answer.loc[0,'ALCDAY5_C'] = 1
    df_user_answer.loc[0,'ALCDAY5_N'] = varALCDAY5

###### Model prediction ######
submit = st.button("Start prediction")
light_GBM_model = ProbabilisticBinaryClassifier(joblib.load('LGBMClassifier-testing-2022-07-09_19_04_48.pkl'), prob_threshold=None)
user_answer = df_user_answer.loc[[0]].to_numpy()
# st.write(get_data_from_testset(361014))

show_result = False
with st.container():
    if submit:
        my_bar = st.progress(0)
        for percent_complete in range(100):
             time.sleep(0.01)
             my_bar.progress(percent_complete + 1)
        time.sleep(0.05)
        st.success('Thanks for waiting, please check your result!')
        pred = light_GBM_model.predict(user_answer)[0][1]
        st.write('---')
        show_result = True

###### Result block ######
if show_result:
    with st.container():
        st.subheader('Your prediction result')
        st.markdown(f'##### Your predicted risk is around: <p style="color:Blue;font-size:24px;border-radius:2%;">***{round(pred, 4)*100}%***</p>', 
        unsafe_allow_html=True)
        st.pyplot(draw_risk_bar(pred))
###### health education block ######
