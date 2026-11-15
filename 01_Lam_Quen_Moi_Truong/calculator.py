# Code tự gõ, chưa tối ưu với trường hợp nhập liệu là chuỗi kí tự, đã giải quyết được việc chia cho 0
print("Máy tính trên Terminal.")

print("Nhap so thu nhat: ")
num_1 = float(input())
print("Nhap so thu hai: ")
num_2 = float(input())

tong = num_1 + num_2
hieu = num_1 - num_2
tich = num_1 * num_2
if num_2 != 0:
    thuong = num_1 / num_2
    du = num_1 % num_2
else:
    print("Loi: Khong the chia cho 0")

print("Tong: ", tong)
print("Hieu: ", hieu)
print("Tich: ", tich)
if num_2 != 0:
    print("Thuong: ", thuong)
    print("Du: ", du)
