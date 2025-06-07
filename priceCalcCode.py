import streamlit as st

# PAGE CONFIG 
st.set_page_config(page_title="💸 Work Hours Calculator", page_icon="💼", layout="centered")

# HIDE STREAMLIT FOOTER 
st.markdown("""
    <style>
    footer {visibility: hidden;}
    .st-emotion-cache-1dp5vir {visibility: hidden;}  /* Hides top-right menu */
    html, body, [class*="css"] {
        font-family: 'Verdana', sans-serif;
        background-color: #1e1e1e;
        color: #ffffff;
    }
    .stNumberInput input {
        background-color: #2e2e2e;
        color: white;
    }
    h1 {
        color: #facc15;
        text-align: center;
        font-size: 3rem;
        margin-bottom: 30px;
    }
    </style>
""", unsafe_allow_html=True)

# TITLE
st.markdown("<h1> Work Hours Calculator</h1>", unsafe_allow_html=True)

# INPUTS
user_hourly_wage = st.number_input("Enter your hourly wage:", min_value=0.01, format="%.2f")
price_of_item = st.number_input("Enter the price of the item:", min_value=0.01, format="%.2f")

# CALCULATION 
if user_hourly_wage > 0 and price_of_item > 0:
    hours_needed = price_of_item / user_hourly_wage
    st.success(f"You need to work {hours_needed:.2f} hours to afford this item.")

# CUSTOM CAPTION
st.caption("Created by Caro")
