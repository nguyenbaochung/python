# cau1.py - Quản lý danh sách sách của thư viện

# A
def them_sach(danh_sach, ma, ten, gia, soluong):
    """Thêm một cuốn sách vào danh_sach."""
    sach = {
        "MaSach": ma,
        "TenSach": ten,
        "Gia": gia,
        "SoLuong": soluong,
    }
    danh_sach.append(sach)


# B
def tim_kiem_theo_ten(danh_sach, tu_khoa):
    """Trả về danh sách các sách có TenSach chứa tu_khoa (không phân biệt hoa/thường)."""
    tu_khoa = tu_khoa.strip().lower()
    return [s for s in danh_sach if tu_khoa in s["TenSach"].lower()]


# C
def tong_gia_tri_kho_sach(danh_sach):
    """Trả về tổng giá trị kho sách = tổng (Gia x SoLuong)."""
    return sum(s["Gia"] * s["SoLuong"] for s in danh_sach)


# D
def in_danh_sach(danh_sach):
    """In danh sách sách dạng bảng."""
    if not danh_sach:
        print("Không có sách nào.")
        return
    print(f"{'MaSach':<8}{'TenSach':<35}{'Gia':>10}{'SoLuong':>10}")
    print("-" * 63)
    for s in danh_sach:
        print(f"{s['MaSach']:<8}{s['TenSach']:<35}{s['Gia']:>10}{s['SoLuong']:>10}")


def nhap_so(thong_bao, kieu=int):
    """Nhập số từ bàn phím, yêu cầu nhập lại nếu sai hoặc âm."""
    while True:
        try:
            gia_tri = kieu(input(thong_bao))
            if gia_tri < 0:
                print("Giá trị không được âm, vui lòng nhập lại.")
                continue
            return gia_tri
        except ValueError:
            print("Giá trị không hợp lệ, vui lòng nhập lại.")


def main():
    # Dữ liệu mẫu để kiểm thử
    danh_sach = []
    them_sach(danh_sach, "S001", "Lập trình Python cơ bản", 95000, 40)
    them_sach(danh_sach, "S002", "Cấu trúc dữ liệu và giải thuật", 120000, 6)
    them_sach(danh_sach, "S003", "Nhập môn trí tuệ nhân tạo", 150000, 25)

    while True:
        print("\n===== QUẢN LÝ SÁCH THƯ VIỆN =====")
        print("1. Thêm sách")
        print("2. Tìm kiếm theo tên")
        print("3. Xem tổng giá trị kho sách")
        print("4. Thoát chương trình")
        chon = input("Chọn chức năng (1-4): ").strip()

        if chon == "1":
            ma = input("Nhập mã sách: ").strip()
            ten = input("Nhập tên sách: ").strip()
            gia = nhap_so("Nhập giá: ", float)
            soluong = nhap_so("Nhập số lượng: ", int)
            # Giữ giá là số nguyên nếu không có phần thập phân
            if gia == int(gia):
                gia = int(gia)
            them_sach(danh_sach, ma, ten, gia, soluong)
            print("Đã thêm sách thành công.")

        elif chon == "2":
            tu_khoa = input("Nhập từ khóa cần tìm: ")
            ket_qua = tim_kiem_theo_ten(danh_sach, tu_khoa)
            print(f"\nTìm thấy {len(ket_qua)} kết quả:")
            in_danh_sach(ket_qua)

        elif chon == "3":
            tong = tong_gia_tri_kho_sach(danh_sach)
            print(f"Tổng giá trị kho sách: {tong:,.0f} VNĐ")

        elif chon == "4":
            print("Đã thoát chương trình. Tạm biệt!")
            break

        else:
            print("Lựa chọn không hợp lệ, vui lòng chọn từ 1 đến 4.")


if __name__ == "__main__":
    main()
