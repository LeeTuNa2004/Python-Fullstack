import streamlit as st

# Phai dat st.set_page_config() o dau (ngay sau phan import) truoc moi lenh st.* hien thi
st.set_page_config(
    page_title="NetDevOps Portal",          # Ten hien tren Tab cua trinh duyet
    page_icon=None,                         # Icon nho tren Tab trinh duyet (Emoji hoac duong dan anh)
    layout="wide"                           # "wide" mo rong chieu ngang, "centered" thu gon o giua
)
st.title("Demo st.set_page_config")
st.write("Hien thi thanh cong!")
