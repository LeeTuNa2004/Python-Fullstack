import streamlit as st

st.title("Demo Form & Checkbox")

# Gom cac o nhap vao mot form, chi khi bam nut Submit ben trong form moi xu ly
with st.form("form_thong_tin"):
    ho_ten = st.text_input("Nhap ho va ten: ")
    tuoi = st.number_input("Nhap tuoi (1 - 100): ", min_value=1, max_value=100, value=20, step=1)
    # Tham so dau tien la label (tieu de o chon), tham so thu 2 la options (danh sach lua chon)
    mon_hoc = st.selectbox("Chon mon hoc: ", options=["Python", "Mang may tinh", "Streamlit"])
    lua_chon = st.checkbox("Bat che do nhac nho on tap!")
    dong_y_luu = st.checkbox("Xac nhan thong tin tren la chinh xac!")

    # Nut gui bat buoc dung st.form_submit_button() khi lam viec voi form
    da_gui = st.form_submit_button("Luu thong tin")
    ap_dung = st.form_submit_button("Ap dung")

if da_gui:
    if not ho_ten.strip():
        st.warning("Ban chua nhap ho ten!")
    elif not dong_y_luu:
        st.error("Vui long tich vao o xac nhan truoc khi luu.")
    else:
        st.success(f"Da luu: {ho_ten.strip()} - {tuoi} tuoi")
if ap_dung:
    if not mon_hoc:
        st.warning("Vui long chon mon hoc!")
    elif not lua_chon:
        st.error("Vui long tich vao o nhac nho")
    else:
        st.info(f"Da bat nhac nho cho mon: {mon_hoc}")
