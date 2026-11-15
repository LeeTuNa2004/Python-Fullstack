# Hướng dẫn từ Skill Gemini
print("=== May tinh bo tui thong minh ===")

num_1 = float(input("Nhap so thu nhat: "))
num_2 = float(input("Nhap so thu hai: "))

print("-" * 30)
print("Ket qua tinh toan:")
print(f"- Tong (A + B): {num_1 + num_2}")
print(f"- Hieu (A - B): {num_1 - num_2}")
print(f"- Tich (A * B): {num_1 * num_2}")

if num_2 != 0:
    thuong = num_1 / num_2
    du = num_1 % num_2
    print(f"- Thuong (A / B): {thuong}")
    print(f"- Du (A % B): {du}")
else:
    print("Loi: Khong the chia cho 0")

print("-" * 30)