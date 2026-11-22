import streamlit as st

st.title("Demo Bo nho phien - st.session_state")

# Khoi tao gia tri mac dinh chi khi chua co key "so_lan_bam"
if "so_lan_bam" not in st.session_state:
    st.session_state["so_lan_bam"] = 0

# Khi bam nut, tang gia tri luu trong session_state len 1
if st.button("Tang bo dem"):
    st.session_state["so_lan_bam"] += 1

if st.button("Dat lai ve 0"):
    st.session_state["so_lan_bam"] = 0

# Hien thi gia tri hien tai tu session_state
st.write(f"Ban da bam nut {st.session_state['so_lan_bam']} lan.")
