import time
import requests
import streamlit as st

st.title("Demo Expander & Spinner")

target_ip = st.text_input("Dia chi IP thiet bi: ")

if st.button("Kiem tra ket noi"):
    ip_value = target_ip.strip()
    # Hien thi thong bao cho trong suot thoi gian khoi lenh ben trong dang chay
    with st.spinner("Dang kiem tra trang thai thiet bi..."):
        time.sleep(1.5)            # Gia lap thao tac kiem tra / goi API mat 1,5s
        log_chi_tiet = [
            f"Ping toi {target_ip}: 4 packets transmitted, 4 received, 0% packet loss",
            f"Trang thai interface e0/0: up/up"
        ]
    st.success(f"Thiet bi {target_ip} dang hoat dong binh thuong.")

    # Tao khu vuc gap gon de an bot chi tiet cho den khi nguoi dung bam mo
    with st.expander("Xem log chi tiet"):
        for dong_log in log_chi_tiet:
            st.write(dong_log)

st.divider()                       # Duong ke phan tach nhe giua 2 khu vuc tac vu

hostname = st.text_input("Nhap ten thiet bi / Hostname: ")
if st.button("Thu thap du lieu giam sat"):
    ten_thiet_bi = hostname.strip()
    du_lieu = None                 # Khoi tao truoc de tranh NameError neu goi API that bai
    with st.spinner("Dang thu thap du lieu..."):
        time.sleep(1)
        url = "https://jsonplaceholder.typicode.com/todos/1"
        try:
            response = requests.get(url, timeout=5)
            response.raise_for_status()
            du_lieu = response.json()
            st.success(f"Thiet bi {hostname} da co thong tin.")
        except requests.RequestException as loi:
            st.error(f"Khong goi duoc API: {loi}")
    if du_lieu is not None:
        with st.expander("Xem du lieu JSON / chi tiet"):
            tieu_de = du_lieu.get("title", "Khong co du lieu")
            st.write(f"Noi dung / Tieu de: {tieu_de}")
            st.json(du_lieu)
