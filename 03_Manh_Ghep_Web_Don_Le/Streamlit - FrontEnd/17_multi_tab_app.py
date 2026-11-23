import requests
import api_client
import streamlit as st

st.set_page_config(
    page_title="Multi-Tab Demo",
    page_icon=None,
    layout="wide"
)
st.title("Demo to chuc Da File & Da Tab")

if "nhat_ki" not in st.session_state:
    st.session_state["nhat_ki"] = []

tab_cau_hinh, tab_giam_sat, tab_nhat_ki = st.tabs(["Cau hinh", "Giam sat", "Nhat ki"])
with tab_cau_hinh:
    st.subheader("Khai bao cau hinh")
    with st.form("form_cau_hinh", clear_on_submit=True):
        ten_tb = st.text_input("Ten thiet bi: ")
        nut_luu = st.form_submit_button("Luu vao nhat ky")
        if nut_luu:
            if ten_tb.strip():
                st.session_state["nhat_ki"].append({
                    "Thiet bi": ten_tb.strip(),
                    "Trang thai": "Da luu"
                })
                st.success(f"Da luu thiet bi: {ten_tb.strip()}")
            else:
                st.warning("Vui long nhap ten thiet bi!")
with tab_giam_sat:
    st.subheader("Truy van du lieu qua API Client")
    todo_id = st.selectbox("Chon ID: ", options=[1, 2, 3, 4, 5])
    if st.button("Lay du lieu"):
        with st.spinner("Dang goi API..."):
            try:
                du_lieu = api_client.lay_thong_tin_todo(todo_id, timeout=5)
                st.success(f"Tieu de: {du_lieu.get('title', 'N/A')}")
                with st.expander("Xem JSON chi tiet"):
                    st.json(du_lieu)
            except requests.RequestException as loi:
                st.error(f"Loi goi API: {loi}")
with tab_nhat_ki:
    st.subheader("Nhat ki thao tac")
    if st.session_state["nhat_ki"]:
        st.dataframe(st.session_state["nhat_ki"], width="stretch")
    else:
        st.caption("Chua co ban ghi nao trong nhat ky.")
