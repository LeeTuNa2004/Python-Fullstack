import streamlit as st

st.title("Demo Chia Tab - st.tabs")

# Tao cac tab ngang hang nhau, tra ve cac bien dai dien cho tung tab
tab_cau_hinh, tab_giam_sat, tab_nhat_ki = st.tabs(["Khai bao Cau hinh", "Giam sat", "Nhat ki"])
du_lieu_mau = [
    {"Thiet bi": "Router", "Log - Trang thai": "up"},
    {"Thiet bi": "Switch", "Log - Trang thai": "down"},
    {"Thiet bi": "Firewall", "Log - Trang thai": "admin-down"},
    {"Thiet bi": "Access Point", "Log - Trang thai": "err-disable"}
]

# Khoi tao danh sach luu nhat ky trong session_state de giu qua cac lan rerun
if "nhat_ki_thiet_bi" not in st.session_state:
    st.session_state["nhat_ki_thiet_bi"] = []

with tab_cau_hinh:
    st.subheader("Tac vu Cau hinh")
    with st.form("form_khai_bao_thiet_bi"):
        ten_thiet_bi = st.text_input("Ten thiet bi / Hostname: ")
        dai_ip = st.text_input("Nhap thong tin IP: ")
        subnet_mask = st.text_input("Nhap Subnet mask: ")
        loai_thiet_bi = st.selectbox("Chon loai thiet bi: ", options=["Router", "Switch", "Firewall", "Access Point"])
        hang_cung_cap = st.selectbox("Chon hang cung cap: ", options=["Cisco", "Aruba", "Palo Alto"])
        dong_y = st.checkbox("Xac nhan thong tin tren la chinh xac!")
        ap_dung = st.form_submit_button("Luu thong tin")
    if ap_dung:
        if not ten_thiet_bi.strip():
            st.warning("Ban chua nhap ten thiet bi!")
        elif not dai_ip.strip():
            st.warning("Ban chua nhap thong tin IP!")
        elif not subnet_mask.strip():
            st.warning("Ban chua nhap Subnet mask!")
        elif not dong_y:
            st.error("Vui long tich vao o xac nhan truoc khi luu!")
        else:
            st.success(f"Da luu thong tin thiet bi {ten_thiet_bi.strip()} loai {loai_thiet_bi} cua hang {hang_cung_cap}")
            st.session_state["nhat_ki_thiet_bi"].append({
                "Hostname": ten_thiet_bi.strip(),
                "IP": dai_ip.strip(),
                "Subnet mask": subnet_mask.strip(),
                "Loai thiet bi": loai_thiet_bi,
                "Hang cung cap": hang_cung_cap
            })
with tab_giam_sat:
    st.subheader("Tac vu giam sat")
    st.info("Khu vuc hien thi trang thai / du lieu giam sat.")
with tab_nhat_ki:
    st.subheader("Nhat ki khai bao")
    if st.session_state["nhat_ki_thiet_bi"]:
        st.dataframe(st.session_state["nhat_ki_thiet_bi"], width="stretch")
    else:
        st.caption("Chua co thiet bi nao duoc luu. Hien thi du lieu trang thai mau")
        st.dataframe(du_lieu_mau, width="stretch")
    if st.button("Xoa nhat ki"):
        st.session_state["nhat_ki_thiet_bi"] = []
        st.success("Da xoa nhat ki!")
