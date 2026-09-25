# HOAT DONG 1: HAM CO BAN

def uscln(a, b):
    while b != 0:
        a, b = b, a % b
    return a


def bcnn(a, b):
    return a * b // uscln(a, b)


def kiem_tra_nguyen_to(n):
    if n < 2:
        return False

    for i in range(2, n):
        if n % i == 0:
            return False

    return True


def kiem_tra_so_hoan_thien(n):
    tong_uoc = 0

    for i in range(1, n):
        if n % i == 0:
            tong_uoc += i

    return tong_uoc == n


# Goi thu voi 3 bo du lieu
print("USCLN:")
print(uscln(24, 36))
print(uscln(15, 25))
print(uscln(18, 27))

print("\nBCNN:")
print(bcnn(4, 6))
print(bcnn(5, 10))
print(bcnn(8, 12))

print("\nKiem tra so nguyen to:")
print(kiem_tra_nguyen_to(29))
print(kiem_tra_nguyen_to(10))
print(kiem_tra_nguyen_to(17))

print("\nKiem tra so hoan thien:")
print(kiem_tra_so_hoan_thien(28))
print(kiem_tra_so_hoan_thien(6))
print(kiem_tra_so_hoan_thien(10))


# HOAT DONG 1.2

def in_loi_chao(ten):
    print(f"Xin chao, {ten}!")
    return


def chia_lay_thuong_du(a, b):
    return a // b, a % b


in_loi_chao("An")

thuong, du = chia_lay_thuong_du(17, 5)
print(f"Thuong: {thuong}, du: {du}")



# HOAT DONG 2


def gioi_thieu(ten, tuoi=18, lop="Chua ro"):
    print(f"Ten: {ten} - Tuoi: {tuoi} - Lop: {lop}")


gioi_thieu("Duy")
gioi_thieu("Binh", 20)
gioi_thieu("Chi", lop="CNTT01")
gioi_thieu(ten="Dung", lop="CNTT02", tuoi=19)



# HOAT DONG 3.1 - *args

def tinh_tong(*args):
    tong = 0

    for so in args:
        tong += so

    return tong


print("\nTinh tong:")
print(tinh_tong(1, 2, 3))
print(tinh_tong(5, 10, 15, 20, 25))
print(tinh_tong())



# HOAT DONG 3.2 - **kwargs


def in_thong_tin(ho_ten, tuoi, **kwargs):
    print(f"Ho ten: {ho_ten} - Tuoi: {tuoi}")

    for khoa, gia_tri in kwargs.items():
        print(f"{khoa}: {gia_tri}")


print()

in_thong_tin(
    "nguyen bao chung",
    20,
    lop="dh14c1",
    que_quan="thai binh"
)

print()

in_thong_tin(
    "Tran Thi B",
    21,
    email="b@example.com"
)