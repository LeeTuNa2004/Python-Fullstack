import streamlit as st

st.title("Demo Bo Cuc: Sidebar & Columns")

# Dua bo loc vao thanh ben trai (sidebar)
st.sidebar.header("Bo loc nhanh")
che_do = st.sidebar.radio("Chon che do hien thi:", ["Tom tat", "Chi tiet", "Thong tin quan trong"])

# Chia khu vuc chinh thanh 3 cot ngang nhau
cot_1, cot_2, cot_3 = st.columns(3)
with cot_1:
    st.subheader("Cot 1")
    st.write("Thong tin o cot 1.")
with cot_2:
    st.subheader("Cot 2")
    if che_do == "Chi tiet":
        st.success("Dang bat che do Chi tiet: Hien thi day du thong tin.")
    elif che_do == "Tom tat":
        st.info("Dang bat che do Tom tat.")
    else:
        st.write("Thong tin o cot 2.")
with cot_3:
    st.subheader("Cot 3")
    if che_do == "Thong tin quan trong":
        st.success("Dang hien thi thong tin quan trong.")
