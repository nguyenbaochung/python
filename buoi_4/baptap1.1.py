#====bai_1====
sinh_vien = {
    "ho_ten":"nguyen bao chung",
    "nam sinh": 2006,
    "diem_tb": 10
}
print(sinh_vien['ho_ten'])
print(sinh_vien.get('diem_tb'))
print(sinh_vien.get('lop', 'chua co'))
#====bai_1.2====
sinh_vien['lop'] = 'CNTT01'
sinh_vien['diem_tb'] = 10
print(sinh_vien)
diem_cu = sinh_vien.pop('diem_tb')
print(sinh_vien,'-diem da xoa', diem_cu)
sinh_vien.update({'nam_sinh':2006,"email": '2411060039@exaple.com'})
print(sinh_vien)


#====bai_2====


diem_mon_hoc = {
    "Toan": 8.0,
    "Ly": 7.5,
    "Hoa": 9.0,
    "Van": 6.5
}
for mon in diem_mon_hoc.keys():
    print(mon)
for diem in diem_mon_hoc.values():
    print(diem)
for mon, diem in diem_mon_hoc.items():
    print(f"{mon}: {diem}")
tong_diem = 0
for diem in diem_mon_hoc.values():
    tong_diem = tong_diem + diem
print("Diem trung binh:", round(tong_diem / len(diem_mon_hoc), 2))


#====bai_3.1====


diem_mon_hoc = {
    "Toan": 8.0,
    "Ly": 7.5,
    "Hoa": 9.0,
    "Van": 6.5
}

diem_cong_diem = {
    mon: round(diem + 0.5, 2)
    for mon, diem in diem_mon_hoc.items()
}
print(diem_cong_diem)
ten_mon_viet_hoa = {
    mon.upper(): diem
    for mon, diem in diem_mon_hoc.items()
}
print(ten_mon_viet_hoa)


#====bai_3.2====


mon_hoc_ky1 = {"Toan", "Ly", "Hoa", "Van"}
mon_hoc_ky2 = {"Toan", "Anh", "Tin", "Van"}
print(mon_hoc_ky1 & mon_hoc_ky2)
print(mon_hoc_ky1 | mon_hoc_ky2)
print(mon_hoc_ky1 - mon_hoc_ky2)


#====bai_4.1====


chuoi_so = "25"
so = int(chuoi_so)
print(so, type(so))

so_thuc = float("3.14")
print(so_thuc, type(so_thuc))

danh_sach = list((1, 2, 3))
bo_ba = tuple([4, 5, 6])
tap_hop = set([1, 2, 2, 3, 3, 3])
tu_dien = dict([("a", 1), ("b", 2)])

print(danh_sach, bo_ba, tap_hop, tu_dien)


#====bai_4.2====


# int("abc")   # Bo comment dong nay se bao loi: ValueError
# int("3.14")  # Bo comment dong nay se bao loi: ValueError

so_hop_le = int(float("3.14"))      # cach lam dung: ep qua float truoc
print(so_hop_le)


#====bai_4.3====


ket_qua = 5 + 2.5       # int + float -> Python tu dong chuyen thanh float
print(ket_qua, type(ket_qua))

ket_qua_2 = "Diem: " + str(8.5) # phai ep str() tuong minh, Python KHONG tu dong noi str voi so
print(ket_qua_2)


#====bai_5====

tu_dien_anh_viet = {
    "hello": "xin chao",
    "book": "quyen sach",
    "table": "cai ban"
}

# Tra tu
print(tu_dien_anh_viet.get("hello", "Khong tim thay tu nay"))
print(tu_dien_anh_viet.get("computer", "Khong tim thay tu nay"))

# Them tu moi
tu_dien_anh_viet["computer"] = "may tinh"

# Xoa mot tu
tu_dien_anh_viet.pop("table")

print("Tu dien hien tai:")
for tu_anh, tu_viet in tu_dien_anh_viet.items():
    print(f"{tu_anh} - {tu_viet}")


#====bai_6====


doan_van = "python la ngon ngu lap trinh python de hoc python de dung"

danh_sach_tu = doan_van.split()
tan_suat = {}

for tu in danh_sach_tu:
    tan_suat[tu] = tan_suat.get(tu, 0) + 1

print("Tan suat xuat hien cac tu:")
for tu, so_lan in tan_suat.items():
    print(f"{tu}: {so_lan}")


#====bai_7====


quan_ly_diem = {
    "Nguyen Van A": [8.0, 7.5, 9.0],
    "Tran Thi B": [6.0, 6.5, 5.5],
    "Le Van C": [9.0, 9.5, 8.5]
}

# Them sinh vien moi
quan_ly_diem["Pham Thi D"] = [7.0, 8.0, 7.5]

# Sua diem mon dau tien cua mot sinh vien
quan_ly_diem["Tran Thi B"][0] = 7.0

diem_trung_binh = {}
for ho_ten, danh_sach_diem in quan_ly_diem.items():
    diem_trung_binh[ho_ten] = round(sum(danh_sach_diem) / len(danh_sach_diem), 2)

print("BANG DIEM TRUNG BINH:")
for ho_ten, dtb in diem_trung_binh.items():
    dat_loai_gioi = dtb >= 8.0
    print(f"{ho_ten:<15} - DTB: {dtb:<5} - Dat loai Gioi? {dat_loai_gioi}")









