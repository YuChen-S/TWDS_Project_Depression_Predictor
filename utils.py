import matplotlib as mpl
import matplotlib.pyplot as plt
import pandas as pd
import streamlit as st

def st_website_setting():
    st.set_page_config(
        page_title="Webpage title",
        page_icon="random",
        layout="centered",
        initial_sidebar_state="auto",
    )

def st_sidebar_info():
    with st.sidebar:
        st.title("About")
        st.info(
            """
            Depressive related disorder risk prediction。\n
            Data : USA CDC BRFSS 2020 data
            """
        )
        st.title("Contact")
        st.info(
            """
            Team: 
            [Eli Chen](), 
            [Sam Shen](),
            [Martin Lee](), 
            [Cobra Chen](), 
            [Allen Shiah](), \n
            Director: [Adms Chung](https://www.linkedin.com/in/admsc/)
            """
        )
        st.success("Contact zoro6mihawk@gmail.com if any problem was found, thanks")
        st.write('''---''')

def st_title_info():
    st.title('Depressive Mood Disorder Predictor')
    st.subheader(
    '''
    This application will help you to identifiy the risk stratification of depressive mood related disorders.
    ''', anchor=None)
    st.write('Thanks for using our product!')
    st.write('---')

def generate_user_input_df():
    basic_features = ['SEXVAR', '_AGEG5YR', '_AGE80', 'HTM4_N', 'HTM4_C', 'WTKG3_C', 'WTKG3_N', '_BMI5_C', '_BMI5_N',]
    mental_features = ['MENTHLTH_C', 'MENTHLTH_N', 'POORHLTH_C', 'POORHLTH_N', '_MENT14D', 'DECIDE', 'DIFFALON', 'ACEDEPRS', ]
    other_features = ['PHYSHLTH_C', 'PHYSHLTH_N', 'FALL12MN_C', 'FALL12MN_N', 'SLEPTIM1_C', 'SLEPTIM1_N', 'ALCDAY5_C', 'ALCDAY5_N', 'EMPLOY1', \
        'GENHLTH', 'MARITAL', '_SMOKER3', '_DRDXAR2', 'SOFEMALE', 'RENTHOM1', '_TOTINDA', 'EDUCA', 'PERSDOC2', 'INCOME2', '_URBSTAT']
    important_features = basic_features + mental_features + other_features
    df_user_answer = pd.DataFrame([], columns=important_features, index=[0])
    return df_user_answer

def draw_risk_bar(pred):
    fig, ax = plt.subplots(figsize=(6, 1))
    fig.subplots_adjust(bottom=0.5)
    cmap = mpl.cm.YlOrRd
    norm = mpl.colors.Normalize(vmin=0, vmax=1)
    cbar = fig.colorbar(mpl.cm.ScalarMappable(norm=norm, cmap=cmap),
                    cax=ax, orientation='horizontal', 
                    ticks=[0, 0.2, 0.4, 0.6, 0.8, 1])
    ax.set_title("Your risk stratification")
    cbar.ax.set_xticklabels(['No risk', 'Low', 'Medium', 'High', 'Very high', 'Extreme high'])   
    cbar.ax.plot([pred, pred], [0, 1], 'black', linewidth=2)
    cbar.ax.plot([pred, pred], [0.9, 1], color='grey', marker='v', linewidth=0.10)
    cbar.ax.plot([pred, pred], [0, 0.1], color='grey', marker='^', linewidth=0.10)
    return fig

def get_data_from_testset(index):
    data = pd.read_csv('brfss_combine_test_v2_important_20220708.csv', index_col=[0])
    data.drop(["ADDEPEV3"], axis=1, inplace=True)
    index_row = data.loc[[index]].to_numpy()
    return index_row 