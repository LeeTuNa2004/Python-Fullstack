import streamlit as st

# Tao tieu de chinh cua trang Web
st.title("Demo Thanh truot & Hop chon")

# Tao thanh truot chon so nguyen tu 0 den 100, gia tri mac dinh la value
tuoi = st.slider("Chon tuoi cua ban: ", min_value=0, max_value=100, value=20)

# Tao hop chon 1 gia tri tu danh sach co san
vai_tro = st.selectbox(
    "Chon vai tro hien tai cua ban: ",
    options=["Hoc sinh / Sinh vien", "Lap trinh vien", "Ky su mang"],
)

# Hien thi ket qua ngay khi nguoi dung keo thanh truot hoac doi lua chon
st.info(f"Ban dang chon: {vai_tro}, {tuoi} tuoi.")
