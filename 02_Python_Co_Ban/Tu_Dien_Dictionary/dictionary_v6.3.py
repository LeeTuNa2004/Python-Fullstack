# Thong ke so lan xuat hien cua cac giao thuc mang (CLI)

def dem_giao_thuc(ds_giao_thuc):
    thong_ke = {}
    for item in ds_giao_thuc:
        giao_thuc = item.strip().lower()
        if not giao_thuc:
            continue
        # Neu giao_thuc da co trong thong_ke thi lay gia tri cu + 1, neu chua co thi lay 0 + 1
        thong_ke[giao_thuc] = thong_ke.get(giao_thuc, 0) + 1
    return thong_ke

def hien_thi_thong_ke(ket_qua):
    for giao_thuc, so_lan in ket_qua.items():
        print(f"- {giao_thuc}: {so_lan} lan")

def main():
  # Test case 1: Co khoang trang, chu hoa/thuong xen ke
  tc1 = [" ospf ", "BGP", "ospf", "MPLS", "bgp", "OSPF"]
  print("=== Test case 1 ===")
  hien_thi_thong_ke(dem_giao_thuc(tc1))

  # Test case 2: Cung mot loai giao thuc
  tc2 = ["ssh", " SSH ", "Ssh"]
  print("\n=== Test case 2 ===")
  hien_thi_thong_ke(dem_giao_thuc(tc2))

  # Test case 3: Danh sach rong
  tc3 = []
  print("\n=== Test case 3 ===")
  kq3 = dem_giao_thuc(tc3)
  print("Dictionary tra ve:", kq3)
  hien_thi_thong_ke(kq3)


if __name__ == "__main__":
  main()
