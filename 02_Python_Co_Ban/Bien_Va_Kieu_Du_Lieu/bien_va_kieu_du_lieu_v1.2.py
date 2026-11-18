# Hệ thống Quản lý & Tính lương theo Gemini

# 1. Khai báo biến kèm Type Hints (Gợi ý kiểu dữ liệu rõ ràng)
ho_va_ten: str = "Le Manh Tuan"
so_nam_kinh_nghiem: int = 1
luong_co_ban_moi_ngay: float = 100000.0
so_ngay_lam_viec_trong_thang: int = 23
trang_thai_nhan_vien: bool = True

# 2. Xử lý logic tính toán thu nhập
tong_thu_nhap: float = luong_co_ban_moi_ngay * so_ngay_lam_viec_trong_thang

# 3. Trình bày giao diện Terminal chuyên nghiệp
print("=" * 42)
print("          THÔNG TIN LƯƠNG NHÂN SỰ")
print("=" * 42)
print(f"• Họ và tên     : {ho_va_ten}")
print(f"• Kinh nghiệm   : {so_nam_kinh_nghiem} năm")
print(f"• Chính thức    : {trang_thai_nhan_vien}")
# Mẹo: Dùng định dạng {bien:,.1f} để tự động thêm dấu phẩy ngăn cách hàng nghìn
print(f"• Tổng thu nhập : {tong_thu_nhap:,.1f} VNĐ")
print("=" * 42)