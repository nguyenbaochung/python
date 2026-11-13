from tkinter import *
from tkinter import messagebox


def them_sach(danh_sach, ma, ten, gia, soluong):
    sach = [ma, ten, gia, soluong]
    danh_sach.append(sach)


def tim_kiem_theo_ten(danh_sach, tu_khoa):
    ket_qua = []
    tu_khoa = tu_khoa.lower()
    for s in danh_sach:
        if tu_khoa in s[1].lower():
            ket_qua.append(s)
    return ket_qua


danh_sach = []  # danh sách sách đang lưu trong chương trình

# ===== a) FORM NHẬP LIỆU =====
cua_so = Tk()
cua_so.title("Quản lý sách thư viện")

Label(cua_so, text="Mã sách:").grid(row=0, column=0, padx=5, pady=5, sticky="w")
Label(cua_so, text="Tên sách:").grid(row=1, column=0, padx=5, pady=5, sticky="w")
Label(cua_so, text="Giá:").grid(row=2, column=0, padx=5, pady=5, sticky="w")
Label(cua_so, text="Số lượng:").grid(row=3, column=0, padx=5, pady=5, sticky="w")

o_ma = Entry(cua_so, width=30)
o_ten = Entry(cua_so, width=30)
o_gia = Entry(cua_so, width=30)
o_soluong = Entry(cua_so, width=30)

o_ma.grid(row=0, column=1, padx=5, pady=5)
o_ten.grid(row=1, column=1, padx=5, pady=5)
o_gia.grid(row=2, column=1, padx=5, pady=5)
o_soluong.grid(row=3, column=1, padx=5, pady=5)

# Vùng hiển thị danh sách (đặt trước các hàm dùng đến nó)
khung_ds = Listbox(cua_so, width=60, height=10)
khung_ds.grid(row=7, column=0, columnspan=2, padx=5, pady=5)


# ===== b) + d) NÚT THÊM SÁCH VÀ KIỂM TRA DỮ LIỆU =====
def nhan_them_sach():
    ma = o_ma.get().strip()
    ten = o_ten.get().strip()
    gia_chu = o_gia.get().strip()
    sl_chu = o_soluong.get().strip()

    # d) Kiểm tra dữ liệu
    if ma == "" or ten == "":
        messagebox.showerror("Lỗi", "Mã sách và Tên sách không được để trống!")
        return

    try:
        gia = int(gia_chu)
        soluong = int(sl_chu)
    except ValueError:
        messagebox.showerror("Lỗi", "Giá và Số lượng phải là số nguyên hợp lệ!")
        return

    if gia < 0 or soluong < 0:
        messagebox.showerror("Lỗi", "Giá và Số lượng không được âm!")
        return

    # b) Thêm vào danh sách và hiển thị sách vừa thêm
    them_sach(danh_sach, ma, ten, gia, soluong)
    dong = ma + " - " + ten + " - " + str(gia) + "đ - SL: " + str(soluong)
    khung_ds.insert(END, dong)

    # Xóa trắng form để nhập tiếp
    o_ma.delete(0, END)
    o_ten.delete(0, END)
    o_gia.delete(0, END)
    o_soluong.delete(0, END)


Button(cua_so, text="Thêm sách", command=nhan_them_sach).grid(row=4, column=0, columnspan=2, pady=8)

# ===== c) TÌM KIẾM =====
Label(cua_so, text="Từ khóa tìm kiếm:").grid(row=5, column=0, padx=5, pady=5, sticky="w")
o_timkiem = Entry(cua_so, width=30)
o_timkiem.grid(row=5, column=1, padx=5, pady=5)


def hien_thi(ds):
    khung_ds.delete(0, END)  # xóa kết quả cũ
    for s in ds:
        dong = s[0] + " - " + s[1] + " - " + str(s[2]) + "đ - SL: " + str(s[3])
        khung_ds.insert(END, dong)


def nhan_tim_kiem():
    tu_khoa = o_timkiem.get().strip()
    ket_qua = tim_kiem_theo_ten(danh_sach, tu_khoa)
    hien_thi(ket_qua)


def nhan_hien_tat_ca():
    hien_thi(danh_sach)


Button(cua_so, text="Tìm kiếm", command=nhan_tim_kiem).grid(row=6, column=0, pady=5)
Button(cua_so, text="Hiện tất cả", command=nhan_hien_tat_ca).grid(row=6, column=1, pady=5)

cua_so.mainloop()
