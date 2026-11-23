import streamlit as st

st.title("Demo Form & Session state an toan")

if "danh_sach_tac_vu" not in st.session_state:
    st.session_state["danh_sach_tac_vu"] = []
if "lich_su_kiem_tra" not in st.session_state:
    st.session_state["lich_su_kiem_tra"] = []

# clear_on_submit=True giup tu xoa trang cac o trong form sau khi gui thanh cong
with st.form("form_them_tac_vu", clear_on_submit=True):
    ten_tac_vu = st.text_input("Ten tac vu: ")
    muc_uu_tien = st.selectbox("Muc uu tien: ", options=["Thap", "Trung binh", "Cao"])
    da_xac_nhan = st.form_submit_button("Them vao danh sach")

# Xu ly ngoai khoi form va ghi an toan vao session_state
if da_xac_nhan:
    ten_sach = ten_tac_vu.strip()
    if not ten_sach:
        st.warning("Vui long nhap ten tac vu truoc khi them.")
    else:
        st.session_state["danh_sach_tac_vu"].append({
            "Tac_vu": ten_sach,
            "Uu_tien": muc_uu_tien
        })
        st.success(f"Da luu tac vu: {ten_sach}")

st.subheader("Danh sach da luu (giu qua cac lan rerun)")
if st.session_state["danh_sach_tac_vu"]:
    st.dataframe(st.session_state["danh_sach_tac_vu"], width="stretch")
else:
    st.caption("Chua co tac vu nao duoc luu.")

with st.form("form_kiem_tra", clear_on_submit=True):
    nhap_ip = st.text_input("Nhap IP thiet bi: ")
    vlan_id = st.number_input("Nhap VLAN ID: ", min_value=1, max_value=4094, value=10, step=1)
    dong_y = st.form_submit_button("Ghi nhan")
if dong_y:
    ip_value = nhap_ip.strip()
    if not ip_value:
        st.warning("IP khong hop le!")
    else:
        st.session_state["lich_su_kiem_tra"].append({
            "IP": ip_value,
            "VLAN ID": vlan_id
        })
        st.success(f"Kiem tra thanh cong {ip_value}")
st.subheader("Lich su kiem tra thiet bi")
if st.session_state["lich_su_kiem_tra"]:
    st.dataframe(st.session_state["lich_su_kiem_tra"], width="stretch")
else:
    st.caption("Chua co lich su kiem tra thiet bi.")
if st.button("Xoa lich su"):
    st.session_state["lich_su_kiem_tra"] = []
    st.success("Xoa lich su thanh cong!")
