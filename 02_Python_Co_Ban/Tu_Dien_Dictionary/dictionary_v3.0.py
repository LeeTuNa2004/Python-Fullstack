# He thong quan ly danh ba dien thoai

danh_ba_dien_thoai = {
    "An": "0912345678",
    "Binh": "0988888888",
    "Chi": "0905555555",
    "Dung": "0909999999"
}

# .title() tu dong chuan hoa viet hoa chu cai dau
nguoi_lien_he = input("Nhap nguoi lien he: ").strip().title()

if nguoi_lien_he in danh_ba_dien_thoai:
    so_lien_he = danh_ba_dien_thoai[nguoi_lien_he]
    print(f"Lien he: {nguoi_lien_he} - So dien thoai: {so_lien_he}")
    print("-" * 50)
else:
    print(f"Khong tim thay ten '{nguoi_lien_he}' trong danh ba!")
