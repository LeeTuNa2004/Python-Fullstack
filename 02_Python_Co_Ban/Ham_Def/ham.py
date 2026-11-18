# Cu phap ham trong Python

def tinh_tong(a, b):
    ket_qua = a + b
    return ket_qua

tong_1 = tinh_tong(5, 10)
print(f"Ket qua la: {tong_1}")

def dien_tich_hinh_chu_nhat(chieu_dai, chieu_rong):
    dien_tich = chieu_dai * chieu_rong
    return dien_tich

dien_tich_1 = dien_tich_hinh_chu_nhat(10.0, 5.8)
print(f"Dien tich hinh chu nhat: {dien_tich_1:,.2f}")
