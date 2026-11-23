import requests
import streamlit as st

st.title("Demo goi API co Auth & Payload")

# Gui POST kem header xac thuc va payload JSON toi API
def gui_yeu_cau_api(token, ten_host, timeout = 5):
    url = "https://httpbin.org/post"
    headers = {
        "Authorization": f"Bearer {token}",             # Gui token xac thuc qua HTTP Header
        "Context-Type": "application/json"
    }
    payload = {
        "action": "monitor_lookup",
        "params": {
            "host_filter": ten_host,
        }
    }
    # Dung tham so json=payload de requests tu dong goi Dict thanh chuoi JSON
    response = requests.post(url, headers=headers, json=payload, timeout=timeout)
    response.raise_for_status()
    return response.json()

token_nhap = st.text_input("API Token / Key: ", type="password")
host_filter = st.text_input("Ten host can loc: ", value="R_1")

if st.button("Gui yeu cau API"):
    if not token_nhap.strip():
        st.warning("Vui long nhap token truoc khi gui.")
    else:
        try:
            ket_qua = gui_yeu_cau_api(token=token_nhap.strip(), ten_host=host_filter.strip())
            st.success("Gui request thanh cong! Server da nhan Header & Payload: ")
            # httpbin echo lai phan du lieu JSON ma client da gui len o key "json"
            st.json(ket_qua.get("json", {}))
        except requests.RequestException as loi:
            st.error(f"Loi goi API: {loi}")
