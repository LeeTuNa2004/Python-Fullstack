# Chi ve giao dien Streamlit & Xu ly hien thi
import streamlit as st
import requests
from api_client import lay_thong_tin_todo, lay_danh_sach_todos

st.title("Demo tach file: API Client & Streamlit UI")

todo_id = st.selectbox("Chon ID cong viec: ", options=[1, 2, 3, 4, 5])

if st.button("Truy van du lieu"):
    try:
        du_lieu = lay_thong_tin_todo(todo_id, 5)
        tieu_de = du_lieu.get("title", "Khong co tieu de")
        hoan_thanh = du_lieu.get("completed", False)

        st.success(f"ID #{todo_id}: {tieu_de}")
        st.caption(f"Trang thai hoan thanh: {hoan_thanh}")
    except requests.RequestException as loi:
        st.error(f"Loi ket noi toi API: {loi}")

st.divider()

st.subheader("Danh sach cong viec theo so luong")
so_dong = st.slider("Chon so luong dong muon xem: ", min_value=1, max_value=10, value=5)

if st.button("Tai danh sach cong viec"):
    try:
        danh_sach = lay_danh_sach_todos(gioi_han=so_dong)
        st.dataframe(danh_sach, width="stretch")
    except requests.RequestException as loi:
        st.error(f"Khong tai duoc danh sach: {loi}")
