import streamlit as st
import pandas as pd
import skops.io as sio

st.set_page_config(
    page_title='Home',
    page_icon='🏠'
)

st.sidebar.success('Select a Page Above')

st.title(':green[Project PredthePrice 💰]')
st.subheader('Exploring Resale Price Prediction for Cars, Motorcycles and Many more in future')
st.text(' \t Discover the world of resale price prediction with advanced models. \n This is a curated collection that includes foreign luxury cars, popular \n Indian vehicles, and a range of bikes, including some luxurious options. \n The prediction models boast an impressive average accuracy score of 90%, \n ensuring reliable insights into the future resale value of your favorite rides.\n Data is collected from Google Open Source Data Search, GitHub Open source Data \n and Kaggle.')

st.info('✅ [Check out the original project on GitHub (Created Using Flask and Bootstrap)](https://github.com/AnuraagaNath/Project-PredthePrice)')


st.warning('Select the Sidebar Options to predict your vehicle resale price')
st.markdown('---')

st.header('Models Description')
df = pd.DataFrame()
df['Prediction Model'] = ['Luxury Car', 'Indian Car', 'Indian Motorcycle', 'Image Classifier']
df['Model Used'] = ['XGB Regressor', 'XGB Regressor', 'XGB Regressor', 'CNN']
df['Training Score (R-Sqaured/Accuracy)'] = [0.8100, 0.9692, 0.941, 0.9994]
df['Testing Score (R-Sqaured/Accuracy)'] = [0.8039, 0.8905, 0.9121, 0.9953]

st.table(df)

st.markdown('---')

st.header('About the Developer')
st.subheader('Anuraaga Nath')
st.text('Masters in Data Science, B. P. Poddar Institute of Technology, Kolkata')
st.markdown('To get in touch, please contact at: [anuraaga.oct15@gmail.com](https://mail.google.com/mail/?view=cm&fs=1&to=anuraaga.oct15@gmail.com&su=RE:Project-PredthePrice&body=PlaceYourMessageHere)')



st.markdown(
    """
    <footer>
        <div class="container">
            <p>© 2023 Anuraaga Nath. All rights reserved. | Created using Streamlit</p>
            <div class="social-links">
                <a href="https://github.com/AnuraagaNath" target="_blank"><img src="https://github.githubassets.com/images/modules/logos_page/GitHub-Mark.png" alt="GitHub Logo" style="width: 30px; height: 30px;"></a>
                <a href="http://linkedin.com/in/anuraaga-nath" target="_blank"><img src="https://content.linkedin.com/content/dam/me/business/en-us/amp/brand-site/v2/bg/LI-Bug.svg.original.svg" alt="LinkedIn Logo" style="width: 30px; height: 30px;"></a>
            </div>
        </div>
    </footer>
    """,
    unsafe_allow_html=True,
)



