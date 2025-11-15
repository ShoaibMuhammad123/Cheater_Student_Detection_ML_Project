# import streamlit as st
# import pickle
# import pandas as pd

# # ---------------------------------------------
# # Page Style + Theme
# # ---------------------------------------------
# st.markdown("""
# <style>
# body {
#     background: linear-gradient(135deg, #0A0F1F 0%, #1B2735 100%);
#     color: #E6F4F1;
#     font-family: 'Segoe UI', sans-serif;
# }

# /* Title */
# .title-text {
#     font-size: 45px;
#     text-align: center;
#     font-weight: 800;
#     color: #00E5FF;
#     text-shadow: 0px 0px 12px rgba(0, 229, 255, 0.75);
#     margin-top: -10px;
# }

# /* Subtitle */
# .subtitle-text {
#     text-align: center;
#     color: #D8EFFF;
#     font-size: 20px;
#     margin-top: -10px;
#     margin-bottom: 25px;
# }
# </style>
# """, unsafe_allow_html=True)

# # ---------------------------------------------
# # LOGO SVG
# # ---------------------------------------------
# logo_svg = """
# <div style="text-align:center;">
# <svg width="140" height="140" viewBox="0 0 200 200" xmlns="http://www.w3.org/2000/svg">
# <defs>
#   <linearGradient id="grad" x1="0%" y1="0%" x2="100%" y2="100%">
#     <stop offset="0%" style="stop-color:#00E5FF;stop-opacity:1" />
#     <stop offset="100%" style="stop-color:#1A73E8;stop-opacity:1" />
#   </linearGradient>
# </defs>
# <path d="M100 10 L170 40 L170 110 Q100 180 30 110 L30 40 Z" fill="url(#grad)" stroke="#00E5FF" stroke-width="3"/>
# <path d="M70 85 h60 v30 h-60z" fill="white" opacity="0.9"/>
# <rect x="85" y="55" width="30" height="20" fill="white" opacity="0.9"/>
# <circle cx="100" cy="125" r="10" fill="white"/>
# </svg>
# </div>
# """

# # Show Logo
# st.markdown(logo_svg, unsafe_allow_html=True)

# # Title + Subtitle
# st.markdown("<div class='title-text'>Smart Student Integrity Detection System</div>", unsafe_allow_html=True)
# st.markdown("<div class='subtitle-text'>Cheater Student Detection Model</div>", unsafe_allow_html=True)

# # ---------------------------------------------
# # Load Model & Data
# # ---------------------------------------------
# with open("pipe.pkl", "rb") as f:
#     pipe = pickle.load(f)

# with open('df.pkl', 'rb') as file:
#     df = pickle.load(file)

# # ---------------------------------------------
# # INPUT FIELDS
# # ---------------------------------------------
# st.write("### Enter Student Details:")

# gender = st.selectbox('Gender', df['gender'].unique())
# region = st.selectbox('Region', df['region'].unique())
# imd_band = st.selectbox('IMD Band', df['imd_band'].unique())
# age_band = st.selectbox('Age Band', df['age_band'].unique())
# disability = st.selectbox('Disability', df['disability'].unique())
# final_result = st.selectbox('Final Result', df['final_result'].unique())

# num_of_prev_attempts = st.number_input('Number of Previous Attempts', min_value=0)
# studied_credits = st.number_input('Credit Hours Studied', min_value=0)
# sum_click = st.number_input('Total Clicks Performed', min_value=0)
# score = st.number_input('Exam Score (%)', min_value=0.0, max_value=100.0)


# if st.button("Predict"):

#     input_data = pd.DataFrame({
#         'gender': [gender],
#         'region': [region],
#         'imd_band': [imd_band],
#         'age_band': [age_band],
#         'num_of_prev_attempts': [num_of_prev_attempts],
#         'studied_credits': [studied_credits],
#         'disability': [disability],
#         'final_result': [final_result],
#         'sum_click': [sum_click],
#         'score': [score]
#     })

#     try:
#         prediction = pipe.predict(input_data)

#         if prediction[0] == 0:
#             result_text = " The Student is: 🟢Not a cheater"
#             color = "#C1F2C3"
#             text_color = "#060606"
#         else:
#             result_text = "The Student is a:🔴cheater"
#             color = "#F2C1C1"
#             text_color = "#6B0A0A"

#         st.markdown(
#             f"""
#             <div style="
#                 background-color:{color};
#                 padding:20px;
#                 border-radius:12px;
#                 border:1px solid #ccc;
#                 font-size:24px;
#                 font-weight:700;
#                 color:{text_color};
#                 text-align:center;
#                 margin-top:20px;">
#                 {result_text}
#             </div>
#             """,
#             unsafe_allow_html=True
#         )

#     except Exception as e:
#         st.error(f"Prediction failed: {e}")


import streamlit as st
import pickle
import pandas as pd

# ----------------------------------------------------------
# Page Style + Custom Input Box Size
# ----------------------------------------------------------
st.markdown("""
<style>

body {
    background: linear-gradient(135deg, #0A0F1F 0%, #1B2735 100%);
    color: #E6F4F1;
    font-family: 'Segoe UI', sans-serif;
}

/* Bigger Input Box */
div[data-baseweb="select"] > div {
    height: 53px;
    font-size: 18px;
}

input {
    height: 53px !important;
    font-size: 18px !important;
}

/* Increase label size */
label {
    font-size: 20px !important;
    font-weight: 600 !important;
    color: #AEE9FF !important;
}

/* Title */
.title-text {
    font-size: 45px;
    text-align: center;
    font-weight: 800;
    color: #00E5FF;
    text-shadow: 0px 0px 12px rgba(0, 229, 255, 0.75);
    margin-top: -30px;
}

/* Subtitle */
.subtitle-text {
    text-align: center;
    color: #D8EFFF;
    font-size: 20px;
    margin-top: -10px;
    margin-bottom: 25px;
}

</style>
""", unsafe_allow_html=True)

# ----------------------------------------------------------
# LOGO SVG
# ----------------------------------------------------------
logo_svg = """
<div style="text-align:center;">
<svg width="140" height="140" viewBox="0 0 200 200" xmlns="http://www.w3.org/2000/svg">
<defs>
  <linearGradient id="grad" x1="0%" y1="0%" x2="100%" y2="100%">
    <stop offset="0%" style="stop-color:#00E5FF;stop-opacity:1" />
    <stop offset="100%" style="stop-color:#1A73E8;stop-opacity:1" />
  </linearGradient>
</defs>
<path d="M100 10 L170 40 L170 110 Q100 180 30 110 L30 40 Z" fill="url(#grad)" stroke="#00E5FF" stroke-width="3"/>
<path d="M70 85 h60 v30 h-60z" fill="white" opacity="0.9"/>
<rect x="85" y="55" width="30" height="20" fill="white" opacity="0.9"/>
<circle cx="100" cy="125" r="10" fill="white"/>
</svg>
</div>
"""



# -------------------- 2nd technique -------------------------------------------


st.markdown(logo_svg, unsafe_allow_html=True)
st.markdown("<div class='title-text'>Smart Student Integrity Detection System</div>", unsafe_allow_html=True)
st.markdown("<div class='subtitle-text'>Cheater Student Detection Model</div>", unsafe_allow_html=True)

# ----------------------------------------------------------
# Load Model & Data
# ----------------------------------------------------------
with open("pipe.pkl", "rb") as f:
    pipe = pickle.load(f)

with open("df.pkl", "rb") as f:
    df = pickle.load(f)

# ----------------------------------------------------------
# INPUT FIELDS (2-Column + EMOJIS + Bigger Size)
# ----------------------------------------------------------
st.write("#### 📝 **Enter Student Details**")

# Row 1
col1, col2 = st.columns(2)
with col1:
    gender = st.selectbox("🧑 Gender", df["gender"].unique())
with col2:
    region = st.selectbox("🌍 Region", df["region"].unique())

# Row 2
col3, col4 = st.columns(2)
with col3:
    imd_band = st.selectbox("📊 IMD Band", df["imd_band"].unique())
with col4:
    age_band = st.selectbox("🎂 Age Band", df["age_band"].unique())

# Row 3
col5, col6 = st.columns(2)
with col5:
    disability = st.selectbox("♿ Disability", df["disability"].unique())
with col6:
    final_result = st.selectbox("🏁 Final Result", df["final_result"].unique())

# Row 4
col7, col8 = st.columns(2)
with col7:
    num_of_prev_attempts = st.number_input("🔁 Number of Previous Attempts", min_value=0)
with col8:
    studied_credits = st.number_input("📘 Credits Studied", min_value=0)

# Row 5
col9, col10 = st.columns(2)
with col9:
    sum_click = st.number_input("🖱 Total Clicks Performed", min_value=0)
with col10:
    score = st.number_input("📝 Exam Score (%)", min_value=0.0, max_value=100.0)

# ----------------------------------------------------------
# Predict Button
# ----------------------------------------------------------
if st.button("🔍 Predict",use_container_width=True):

    input_data = pd.DataFrame({
        "gender": [gender],
        "region": [region],
        "imd_band": [imd_band],
        "age_band": [age_band],
        "num_of_prev_attempts": [num_of_prev_attempts],
        "studied_credits": [studied_credits],
        "disability": [disability],
        "final_result": [final_result],
        "sum_click": [sum_click],
        "score": [score]
    })

    try:
        prediction = pipe.predict(input_data)

        # if prediction[0] == 0:
        #     result_text = "🟢 The Student is NOT a Cheater"
        #     color = "#C1F2C3"
        #     text_color = "#060606"
        # else:
        #     result_text = "🔴 The Student IS a Cheater"
        #     color = "#F2C1C1"
        #     text_color = "#6B0A0A"
        if prediction[0] == 0:
            result_text = "🟢 The Student is <span style='color:#00FFAA; font-weight:900;'>NOT a Cheater</span>"
            color = "#503B88"
            text_color = "#C6FFE0"
        else:
            result_text = "🔴 The Student <span style='color:#FF5C5C; font-weight:900;'>IS a Cheater</span>"
            color = "#503B88"
            text_color = "#FFD6D6"


        st.markdown(
            f"""
            <div style="
                background-color:{color};
                padding:25px;
                border-radius:12px;
                border:1px solid #ccc;
                font-size:28px;
                font-weight:700;
                color:{text_color};
                text-align:center;
                margin-top:10px;">
                {result_text}
            </div>
            """,
            unsafe_allow_html=True
        )

    except Exception as e:
        st.error(f"Prediction failed: {e}")


