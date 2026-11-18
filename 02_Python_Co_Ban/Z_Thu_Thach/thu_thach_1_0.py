# Tro choi doan so bi mat

import random

so_bi_mat = random.randint(1, 100)
dem = 0

while True:
    try:
        n = int(input("Nhap so muon doan: "))
    except ValueError:
        print("Ki tu nhap khong phai la so. Xin moi nhap lai! \n")
        continue
    
    dem += 1                                    # Chi tinh so luot dem khi nguoi dung nhap so hop le

    if n < 1 or n > 100:
        print("Vui long nhap so trong khoang tu 1 den 100. Vui long nhap lai! \n")
        continue
    if n < so_bi_mat:
        print("So bi mat lon hon so cua ban!")
    elif n > so_bi_mat:
        print("So bi mat nho hon so cua ban!")
    else:
        print("Chuc mung da doan trung!")
        print(f"So lan doan: {dem} lan")
        break
