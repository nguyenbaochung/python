# ==============================================================================
# ĐỒ ÁN MÔN HỌC: QUẢN LÝ SINH VIÊN MINI
# Ngôn ngữ: Python 3
# Kỹ thuật: List, Dictionary, Loop, Function, Try-Except
# ==============================================================================

# Dữ liệu khởi tạo ban đầu
danh_sach_sv = [
    {
        "ma_sv": "SV01",
        "ho_ten": "Nguyen Bao Chung",
        "toan": 8.5,
        "ly": 7.0,
        "hoa": 9.0,
        "dtb": 8.17,
        "xep_loai": "Gioi"
    },
    {
        "ma_sv": "SV02",
        "ho_ten": "Nguyen Manh Dung",
        "toan": 6.0,
        "ly": 6.5,
        "hoa": 7.0,
        "dtb": 6.50,
        "xep_loai": "Kha"
    },
    {
        "ma_sv": "SV03",
        "ho_ten": "Vu quoc Chi",
        "toan": 4.0,
        "ly": 5.0,
        "hoa": 4.5,
        "dtb": 4.50,
        "xep_loai": "Yeu"
    }
]


# ==============================================================================
# 1. TÍNH ĐIỂM TRUNG BÌNH VÀ XẾP LOẠI
# ==============================================================================

def tinh_dtb_va_xep_loai(toan, ly, hoa):
    """Tính điểm trung bình và trả về xếp loại"""

    dtb = round((toan + ly + hoa) / 3, 2)

    if dtb >= 8.0:
        xep_loai = "Gioi"
    elif dtb >= 6.5:
        xep_loai = "Kha"
    elif dtb >= 5.0:
        xep_loai = "Trung binh"
    else:
        xep_loai = "Yeu"

    return dtb, xep_loai


# ==============================================================================
# 2. NHẬP ĐIỂM HỢP LỆ
# ==============================================================================

def nhap_diem_hop_le(ten_mon):
    """Hàm nhập điểm an toàn bằng try-except"""

    while True:
        try:
            diem = float(input(f"Nhap diem {ten_mon} (0 - 10): "))

            if 0.0 <= diem <= 10.0:
                return diem

            print("-> Loi: Diem phai nam trong khoang tu 0 den 10!")

        except ValueError:
            print("-> Loi: Du lieu khong hop le! Vui long nhap mot so.")


# ==============================================================================
# 3. TÌM SINH VIÊN THEO MÃ
# ==============================================================================

def tim_sv_theo_ma(ma_sv):
    """Tìm sinh viên trong danh sách theo mã sinh viên"""

    for sv in danh_sach_sv:
        if sv["ma_sv"] == ma_sv:
            return sv

    return None


# ==============================================================================
# 4. HIỂN THỊ DANH SÁCH
# ==============================================================================

def hien_thi_danh_sach():
    """Hiển thị danh sách toàn bộ sinh viên"""

    print("\n" + "=" * 75)

    print(
        f"{'Ma SV':<8}"
        f"{'Ho va Ten':<20}"
        f"{'Toan':<8}"
        f"{'Ly':<8}"
        f"{'Hoa':<8}"
        f"{'DTB':<8}"
        f"{'Xep loai':<10}"
    )

    print("-" * 75)

    if not danh_sach_sv:
        print("Danh sach hien tai dang trong!")

    else:
        for sv in danh_sach_sv:
            print(
                f"{sv['ma_sv']:<8}"
                f"{sv['ho_ten']:<20}"
                f"{sv['toan']:<8.1f}"
                f"{sv['ly']:<8.1f}"
                f"{sv['hoa']:<8.1f}"
                f"{sv['dtb']:<8.2f}"
                f"{sv['xep_loai']:<10}"
            )

    print("=" * 75)



# 5. THÊM SINH VIÊN


def them_sinh_vien():
    """Thêm sinh viên mới"""

    print("\n--- THEM SINH VIEN MOI ---")

    ma_sv = input("Nhap ma sinh vien (vd: SV04): ").strip().upper()

    # Kiểm tra mã sinh viên đã tồn tại chưa
    if tim_sv_theo_ma(ma_sv) is not None:
        print(f"-> Loi: Ma sinh vien {ma_sv} da ton tai!")
        return

    ho_ten = input("Nhap ho va ten sinh vien: ").strip().title()

    toan = nhap_diem_hop_le("Toan")
    ly = nhap_diem_hop_le("Ly")
    hoa = nhap_diem_hop_le("Hoa")

    # Tính ĐTB và xếp loại
    dtb, xep_loai = tinh_dtb_va_xep_loai(toan, ly, hoa)

    # Thêm vào danh sách
    danh_sach_sv.append({
        "ma_sv": ma_sv,
        "ho_ten": ho_ten,
        "toan": toan,
        "ly": ly,
        "hoa": hoa,
        "dtb": dtb,
        "xep_loai": xep_loai
    })

    print(f"-> Da them sinh vien {ho_ten} ({ma_sv}) thanh cong!")


# 6. CẬP NHẬT SINH VIÊN


def cap_nhat_sinh_vien():
    """Cập nhật thông tin sinh viên"""

    print("\n--- CAP NHAT THONG TIN SINH VIEN ---")

    ma_sv = input("Nhap ma sinh vien can sua: ").strip().upper()

    sv = tim_sv_theo_ma(ma_sv)

    if sv is None:
        print(f"-> Khong tim thay sinh vien voi ma {ma_sv}!")
        return

    print(f"Dang sua thong tin cho sinh vien: {sv['ho_ten']}")

    # Nhập tên mới
    ho_ten_moi = input(
        f"Nhap ho ten moi (De trong neu giu nguyen '{sv['ho_ten']}'): "
    ).strip().title()

    if ho_ten_moi:
        sv["ho_ten"] = ho_ten_moi

    # Hỏi có sửa điểm không
    sua_diem = input(
        "Ban co muon nhap lai diem khong? (y/n): "
    ).strip().lower()

    if sua_diem == "y":

        sv["toan"] = nhap_diem_hop_le("Toan")
        sv["ly"] = nhap_diem_hop_le("Ly")
        sv["hoa"] = nhap_diem_hop_le("Hoa")

        # Tính lại ĐTB và xếp loại
        sv["dtb"], sv["xep_loai"] = tinh_dtb_va_xep_loai(
            sv["toan"],
            sv["ly"],
            sv["hoa"]
        )

    print(f"-> Cap nhat sinh vien {ma_sv} thanh cong!")



# 7. XÓA SINH VIÊN


def xoa_sinh_vien():
    """Xóa sinh viên"""

    print("\n--- XOA SINH VIEN ---")

    ma_sv = input("Nhap ma sinh vien can xoa: ").strip().upper()

    sv = tim_sv_theo_ma(ma_sv)

    if sv is None:
        print(f"-> Khong tim thay sinh vien voi ma {ma_sv}!")
        return

    danh_sach_sv.remove(sv)

    print(
        f"-> Da xoa sinh vien {sv['ho_ten']} "
        f"({ma_sv}) khoi danh sach!"
    )


# ==============================================================================
# 8. TÌM KIẾM SINH VIÊN
# ==============================================================================

def tim_kiem_sinh_vien():
    """Tìm kiếm sinh viên"""

    print("\n--- TIM KIEM SINH VIEN ---")

    ma_sv = input("Nhap ma sinh vien can tim: ").strip().upper()

    sv = tim_sv_theo_ma(ma_sv)

    if sv is None:
        print(f"-> Khong tim thay sinh vien voi ma {ma_sv}!")
        return

    print("\nTHONG TIN SINH VIEN TIM THAY:")

    print(f"Ma SV     : {sv['ma_sv']}")
    print(f"Ho va ten : {sv['ho_ten']}")
    print(f"Diem Toan : {sv['toan']}")
    print(f"Diem Ly   : {sv['ly']}")
    print(f"Diem Hoa  : {sv['hoa']}")
    print(f"Diem TB   : {sv['dtb']}")
    print(f"Xep loai  : {sv['xep_loai']}")


# ==============================================================================
# 9. THỐNG KÊ
# ==============================================================================

def thong_ke():
    """Thống kê chung"""

    print("\n--- THONG KE CHUNG ---")

    tong_sv = len(danh_sach_sv)

    if tong_sv == 0:
        print("Chua co sinh vien nao trong he thong!")
        return

    # Tính ĐTB chung
    tong_dtb = sum(sv["dtb"] for sv in danh_sach_sv)

    dtb_lop = round(tong_dtb / tong_sv, 2)

    # Đếm số sinh viên từng loại
    gioi = sum(
        1 for sv in danh_sach_sv
        if sv["xep_loai"] == "Gioi"
    )

    kha = sum(
        1 for sv in danh_sach_sv
        if sv["xep_loai"] == "Kha"
    )

    tb = sum(
        1 for sv in danh_sach_sv
        if sv["xep_loai"] == "Trung binh"
    )

    yeu = sum(
        1 for sv in danh_sach_sv
        if sv["xep_loai"] == "Yeu"
    )

    print(f"Tong so sinh vien       : {tong_sv}")
    print(f"Diem trung binh chung   : {dtb_lop}")

    print(
        f"So sinh vien Gioi       : "
        f"{gioi} ({gioi / tong_sv * 100:.1f}%)"
    )

    print(
        f"So sinh vien Kha        : "
        f"{kha} ({kha / tong_sv * 100:.1f}%)"
    )

    print(
        f"So sinh vien Trung binh : "
        f"{tb} ({tb / tong_sv * 100:.1f}%)"
    )

    print(
        f"So sinh vien Yeu        : "
        f"{yeu} ({yeu / tong_sv * 100:.1f}%)"
    )


# ==============================================================================
# 10. HIỂN THỊ MENU
# ==============================================================================

def hien_thi_menu():

    print("\n===== HE THONG QUAN LY SINH VIEN MINI =====")

    print("1. Hien thi danh sach sinh vien")
    print("2. Them sinh vien moi")
    print("3. Cap nhat thong tin sinh vien")
    print("4. Xoa sinh vien")
    print("5. Tim kiem sinh vien")
    print("6. Thong ke")
    print("0. Thoat chuong trinh")


# ==============================================================================
# 11. HÀM MAIN
# ==============================================================================

def main():

    while True:

        hien_thi_menu()

        lua_chon = input(
            "Nhap lua chon cua ban (0-6): "
        ).strip()

        if lua_chon == "1":

            hien_thi_danh_sach()

        elif lua_chon == "2":

            them_sinh_vien()

        elif lua_chon == "3":

            cap_nhat_sinh_vien()

        elif lua_chon == "4":

            xoa_sinh_vien()

        elif lua_chon == "5":

            tim_kiem_sinh_vien()

        elif lua_chon == "6":

            thong_ke()

        elif lua_chon == "0":

            print(
                "Cam on ban da su dung chuong trinh. Tam biet!"
            )

            break

        else:

            print(
                "-> Lua chon khong hop le, "
                "vui long chon lai (0-6)."
            )


# ==============================================================================
# 12. CHẠY CHƯƠNG TRÌNH
# ==============================================================================

if __name__ == "__main__":
    main()