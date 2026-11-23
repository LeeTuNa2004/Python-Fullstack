import streamlit as st

st.title("Demo Hien thi Log - st.code")

# Gia lap chuoi log nhieu dong tra ve tu tac vu cau hinh / kiem tra thiet bi
sample_log = """TASK [Gathering Facts] *********************************************************
ok: [pe_1]
TASK [Configure VRF & Interface] **********************************************
changed: [pe_1] => (item=VRF_KH_ABC)"""

if st.button("Hien thi log mau"):
    st.success("Hoan tat chay tac vu mau.")
    # language="bash" giup hien thi dang khoi ma/log chuan monospace va to mau cu phap bash
    st.code(sample_log, language="bash")
