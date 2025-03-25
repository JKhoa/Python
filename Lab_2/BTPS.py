class PhanSo:
    def __init__(self, tu: int, mau: int):
        self.__tu = tu
        self.__mau = mau
        self.rutGon()

    def rutGon(self):
        gcd = self.uocChungCua2So(self.__tu, self.__mau)
        self.__tu //= gcd
        self.__mau //= gcd

    def uocChungCua2So(self, a: int, b: int):
        while b != 0:
            a, b = b, a % b
        return abs(a)

    def __add__(self, ps):
        return PhanSo(self.__tu * ps.__mau + ps.__tu * self.__mau, self.__mau * ps.__mau)

    def __sub__(self, ps):
        return PhanSo(self.__tu * ps.__mau - ps.__tu * self.__mau, self.__mau * ps.__mau)

    def __mul__(self, ps):
        return PhanSo(self.__tu * ps.__tu, self.__mau * ps.__mau)

    def __truediv__(self, ps):
        return PhanSo(self.__tu * ps.__mau, self.__mau * ps.__tu)
    
    def giaTri(self):
        return self.__tu / self.__mau
    
    def tu(self):
        return self.__tu
    
    def mau(self):
        return self.__mau

    def __str__(self):
        return f"{self.__tu}/{self.__mau}"

    def laPhanSoAm(self):
        return (self.__tu < 0 and self.__mau > 0) or (self.__tu > 0 and self.__mau < 0)

# Sửa lỗi khởi tạo đối tượng PhanSo
a = PhanSo(2, 3)
b = PhanSo(3, 5)

print(f"{a} + {b} = {a + b}")
print(f"{a} - {b} = {a - b}")
print(f"{a} * {b} = {a * b}")
print(f"{a} / {b} = {a / b}")

class DanhSachPhanSo:
    def __init__(self):
        self.dsps = []

    def themPhanSo(self, ps: PhanSo):
        self.dsps.append(ps)

    def demPhanSoAm(self):
        return len([ps for ps in self.dsps if ps.laPhanSoAm()])
    
    def timPhanSoDuongNhoNhat(self):
        soDuong = [ps for ps in self.dsps if not ps.laPhanSoAm()]
        return min(soDuong, key=lambda ps: ps.giaTri(), default=None)
    
    def timTatCaViTriCuaPhanSo(self, x: PhanSo):
        return [i for i, ps in enumerate(self.dsps) if ps.giaTri() == x.giaTri()]
    
    def tongPhanSoAm(self):
        tong = PhanSo(0, 1)
        for ps in self.dsps:
            if ps.laPhanSoAm():
                tong += ps
        return tong

    def xoaPhanSo(self, x: PhanSo):
        self.dsps = [ps for ps in self.dsps if ps.giaTri() != x.giaTri()]

    def xoaPhanSoCoTu(self, tu: int):
        self.dsps = [ps for ps in self.dsps if ps.tu() != tu]

    def sapXepTangTheoGiaTri(self):
        self.dsps.sort(key=lambda ps: ps.giaTri())

    def sapXepGiamTheoGiaTri(self):
        self.dsps.sort(key=lambda ps: ps.giaTri(), reverse=True)

    def sapXepTangTheoMau(self):
        self.dsps.sort(key=lambda ps: ps.mau())

    def sapXepGiamTheoMau(self):
        self.dsps.sort(key=lambda ps: ps.mau(), reverse=True)

    def sapXepTangTheoTu(self):
        self.dsps.sort(key=lambda ps: ps.tu())

    def sapXepGiamTheoTu(self):
        self.dsps.sort(key=lambda ps: ps.tu(), reverse=True)

dsPhanSo = DanhSachPhanSo()
dsPhanSo.themPhanSo(PhanSo(-1, 2))
dsPhanSo.themPhanSo(PhanSo(1, 3))
dsPhanSo.themPhanSo(PhanSo(2, 5))
dsPhanSo.themPhanSo(PhanSo(-3, 4))

print("Số phân số âm:", dsPhanSo.demPhanSoAm())
print("Phân số dương nhỏ nhất:", dsPhanSo.timPhanSoDuongNhoNhat())

phanSoTimKiem = PhanSo(1, 3)
print(f"Tìm vị trí của phân số {phanSoTimKiem}: ", dsPhanSo.timTatCaViTriCuaPhanSo(phanSoTimKiem))

print("Tổng các phân số âm:", dsPhanSo.tongPhanSoAm())

phanSoXoa = PhanSo(-1, 2)
dsPhanSo.xoaPhanSo(phanSoXoa)
print("Danh sách phân số sau khi xóa phân số", phanSoXoa, ":", [str(ps) for ps in dsPhanSo.dsps])

tuSoXoa = -3
dsPhanSo.xoaPhanSoCoTu(tuSoXoa)
print("Danh sách phân số sau khi xóa các phân số có tử số là", tuSoXoa, ":", [str(ps) for ps in dsPhanSo.dsps])

dsPhanSo.sapXepTangTheoGiaTri()
print("Danh sách phân số sau khi sắp xếp tăng theo giá trị:", [str(ps) for ps in dsPhanSo.dsps])

dsPhanSo.sapXepGiamTheoGiaTri()
print("Danh sách phân số sau khi sắp xếp giảm theo giá trị:", [str(ps) for ps in dsPhanSo.dsps])

dsPhanSo.sapXepTangTheoMau()
print("Danh sách phân số sau khi sắp xếp tăng theo mẫu số:", [str(ps) for ps in dsPhanSo.dsps])

