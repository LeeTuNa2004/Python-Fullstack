# He thong tra cuu diem so hoc sinh (Lookup)

diem_so = {
    "An": 8.5,
    "Binh": 7.0,
    "Chi": 9.2,
    "Dung": 6.5
}

# .strip() xoa khoang trang thua va .capitalize() tu dong chuan hoa viet hoa chu cai dau
hoc_sinh = input("Nhap ten hoc sinh: ").strip().capitalize()

# Kiem tra su ton tai cua Key trong Dictionary
if hoc_sinh in diem_so:
    diem = diem_so[hoc_sinh]
    print(f"Diem so cua {hoc_sinh} la: {diem:,.2f} diem")
else:
    print(f"Khong tim thay hoc sinh '{hoc_sinh}' trong he thong!")
