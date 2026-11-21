# Tra cuu & Tinh gia do uong quan ca phe

menu = {
    "ca_phe": 25000,
    "tra_dao": 30000,
    "matcha": 35000
}

do_uong = input("Nhap ten mon can tra: ").strip().lower()
ket_qua = menu.get(do_uong, "Mon chua co trong Menu.")
# Dinh dang phan hien thi gia tuy theo ket qua tra ve la so hay chuoi thong bao
if isinstance(ket_qua, int):
    gia_hien_thi = f"{ket_qua} VND"
else:
    gia_hien_thi = ket_qua
print(f"Mon: {do_uong} | Gia: {gia_hien_thi}")
