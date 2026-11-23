import threading
import streamlit as st

st.title("Demo @st.cache_resource")

# Tra ve cung mot the hien (instance) Lock dung chung cho toan bo Web
@st.cache_resource(show_spinner=False)
def get_shared_lock():
    return threading.Lock()

lock = get_shared_lock()
# id(lock) se giu nguyen qua cac lan rerun du bam nut nhieu lan
st.write(f"Dia chi bo nho cua Lock dung chung ('id(lock)'): '{id(lock)}'")
if st.button("Chay thao tac co khoa an toan"):
    # Chi 1 luong di vao duoc khoi ben trong tai mot thoi diem
    with lock:
        st.success(f"Da lay duoc khoa chung va thuc hien thao tac an toan!")
