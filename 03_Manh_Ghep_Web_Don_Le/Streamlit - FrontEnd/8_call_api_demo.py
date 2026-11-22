import requests
import streamlit as st

st.title("Demo goi API tu Streamlit")

todo_id = st.selectbox("Chon ID cong viec: ", options=[1, 2, 3, 4, 5])

if st.button("Lay du lieu tu API"):
    # Dung API cong khai gia lap du lieu mau (JSONPlaceholder)
    # Ghep dong "todo_id" vao cuoi URL
    url = f"https://jsonplaceholder.typicode.com/todos/{todo_id}"
    try:
        # Gui yeu cau GET toi dia chi API voi thoi gian cho toi da 5s
        response = requests.get(url, timeout=5)
        # Bao loi neu HTTP status khong thanh cong (VD: 404, 500,...)
        response.raise_for_status()

        # Chuyen du lieu JSON tra ve thanh Dict trong Python
        du_lieu = response.json()
        st.success("Lay du lieu thanh cong!")
        # Hien thi du lieu dang JSON tren giao dien
        st.json(du_lieu)
        tieu_de = du_lieu.get("title", "Khong co tieu de")
        st.info(f"Cong viec #{todo_id}: {tieu_de}")
    except requests.RequestException as loi:
        st.error(f"Khong goi duoc API: {loi}")
