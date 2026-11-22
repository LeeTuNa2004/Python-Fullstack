import streamlit as st

st.title("Demo Nhap so lieu & Bang")

# Tao o nhap so thuc voi gia tri min-max va gia tri mac dinh
# Buoc nhay khi bam nut (+/-) tren o nhap so
can_nang = st.number_input("Nhap can nang (kg): ", min_value=1.0, max_value=120.0, value=65.0, step=0.5,)
chieu_cao = st.number_input("Nhap chieu cao (m): ", min_value=0.5, max_value=2.5, value=1.8, step=0.01)

# Danh sach cac ban ghi (Dang List chua Dict)
du_lieu_mau = [
    {"Muc": "An trua", "So_tien": 45000},
    {"Muc": "Ca phe", "So_tien": 30000}
]

# Hien thi danh sach dang bang truc quan tren giao dien Web
st.dataframe(du_lieu_mau, width="stretch")
st.caption(f"Can nang dang nhap: {can_nang} kg")

# Gom du lieu vao List of Dict truoc khi dua vao st.dataframe()
bang_chi_so = [
    {"Chi_tieu": "Can nang (kg)", "Gia_tri": can_nang},
    {"Chi_tieu": "Chieu cao (m)", "Gia_tri": chieu_cao},
]
st.dataframe(bang_chi_so, width="stretch")
