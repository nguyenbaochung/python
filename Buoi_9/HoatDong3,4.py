# ===== Hoat Dong 3 =====

import tkinter as tk
from tkinter import ttk

cua_so = tk.Tk()
cua_so.title("Vi du Combobox")
cua_so.geometry("300x180")
tk.Label(cua_so, text="Chon thanh pho:").pack(pady=10)
combobox_thanh_pho = ttk.Combobox(cua_so, values=["Ha Noi", "Da Nang", "TP.HCM",
                                                  "Hue"])
combobox_thanh_pho.current(0)  # chon gia tri dau tien lam mac dinh
combobox_thanh_pho.pack(pady=5)


def xem_thanh_pho():
    nhan_ket_qua.config(text=f"Ban chon: {combobox_thanh_pho.get()}")


tk.Button(cua_so, text="Xac nhan", command=xem_thanh_pho).pack(pady=10)
nhan_ket_qua = tk.Label(cua_so, text="")
nhan_ket_qua.pack()
cua_so.mainloop()

# ===== Hoat Dong 4 =====

import tkinter as tk

cua_so = tk.Tk()
cua_so.title("Vi du Scale")
cua_so.geometry("300x180")


def khi_keo_thanh_truot(gia_tri):
    nhan_gia_tri.config(text=f"Gia tri hien tai: {gia_tri}")


thanh_truot = tk.Scale(cua_so, from_=0, to=100, orient="horizontal",
                       command=khi_keo_thanh_truot)
thanh_truot.pack(pady=20, padx=20, fill="x")

nhan_gia_tri = tk.Label(cua_so, text="Gia tri hien tai: 0")
nhan_gia_tri.pack()
cua_so.mainloop()
