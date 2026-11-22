import streamlit as st

# Dat tieu de lon cho trang Web
st.title("Hello, World!")
st.write("Chao mung buoc sang Giai doan 3 - Lam quen giao dien Web bang Python!")

# Tao o nhap ten tu nguoi dung
ten_nguoi_dung = st.text_input("Nhap ten cua ban: ")

# Tao nut bam va xu ly khi nguoi dung bam vao nut
if st.button("Gui loi chao"):
    if ten_nguoi_dung.strip():
        st.success(f"Xin chao {ten_nguoi_dung.strip()}! Ban da chay thanh cong giao dien dau tien.")
    else:
        st.warning("Ban chua nhap ten!")
