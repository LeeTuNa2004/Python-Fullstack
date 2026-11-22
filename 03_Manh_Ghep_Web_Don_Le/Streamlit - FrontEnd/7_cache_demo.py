import time
import streamlit as st

st.title("Demo Cache du lieu - @st.cache_data")

# Luu ket qua tra ve theo tham so dau vao (n)
@st.cache_data
def tinh_binh_phuong_cham(n):
    time.sleep(1.5)             # Gia lap tac vu mat 1,5s moi xong
    return n * n

n = st.number_input("Nhap so nguyen n: ", min_value=1, max_value=50, value=5, step=1)

# Gia su ham xu ly chay 1,5s thi xong, neu cung mot dau vao thi lay thang ket qua da luu ra dung ngay
# Chi khi nao dau vao thay doi moi xu ly lai
ket_qua = tinh_binh_phuong_cham(n)
st.success(f"Binh phuong cua '{n}' la: {ket_qua}")

@st.cache_data
def nhan_doi_cham(x):
    time.sleep(5)
    return x * 2

x = st.slider("Chon so nguyen x: ", min_value=1, max_value=100, value=20)
tich = nhan_doi_cham(x)
st.info(f"Ket qua cua phep nhan doi la: {tich}")
