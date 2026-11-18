# Cu phap Dictionary trong Python
# Luu tru du lieu theo cap khoa - gia tri (Key - Value)
# De truy xuat thi chi can goi truc tiep Key de lay ra Value tuong ung
# Dictionary khac voi List vi khong phai quan tam den so thu tu cua du lieu ma truy xuat theo cap Key - Value

tu_dien = {
    "hello": "xin chao",
    "python": "ngon ngu lap trinh",
    "apple": "qua tao",
    "book": "quyen sach",
    "code": "ma nguon"
}

nghia_python = tu_dien["python"]
print(f"Nghia cua Python la: {nghia_python}")

tu_dien["mentor"] = "nguoi huong dan"
print(tu_dien)
