import datetime as dt
import math as math
class SinhVien:
    truong = "Đại học Đà Lạt"
    def __init__(self, maso: int, hoTen: str, ngaySinh: dt.date) -> None:
        self.__maso = maso
        self.__hoTen = hoTen
        self.__ngaySinh = ngaySinh

    @property
    def maso(self):
        return self.__maso

    @maso.setter
    def maso(self, maso):
        if self.laMaSoHopLe(maso):
            self.__maso = maso

    @staticmethod
    def laMaSoHopLe(maso: int):
        return len(str(maso)) == 7

    @classmethod
    def doiTenTruong(self, tenmoi):
        self.truong = tenmoi

    def __str__(self) -> str:
        return f"{self.__maso}\t{self.__hoTen}\t{self.__ngaySinh}"

class DanhSachSV:
    def __init__(self) -> None:
        self.dssv = []

    def themSinhVien(self, sv: SinhVien):
        self.dssv.append(sv)

    def xuat(self):
        for sv in self.dssv:
            print(sv)

    def timSvTheoMSSV(self, mssv: int):
        return [sv for sv in self.dssv if sv.maso == mssv]

    def timVTSvTheoMSSV(self, mssv: int):
        for i in range(len(self.dssv)):
            if self.dssv[i].maso == mssv:
                return i
        return -1

    def xoaSvTheoMssv(self, maSo: int) -> bool:
        vt = self.timVTSvTheoMSSV(maSo)
        if vt != -1:
            del self.dssv[vt]
            return True
        else:
            return False

    def timSvTheoTen(self, ten: str):
        return [sv for sv in self.dssv if sv._SinhVien__hoTen == ten]
    def timSvTruocNgay(self, ngay:dt.datetime):
        return [sv for sv in self.dssv if sv._SinhVien__ngaySinh < ngay]

# Tạo các đối tượng SinhVien
sv1 = SinhVien(1000001, "Nguyen van Nam", dt.date(2000, 1, 1))
sv2 = SinhVien(1000002, "Nguyen Van B", dt.date(2000, 5, 13))
sv3 = SinhVien(1000003, "Nguyen Van A", dt.date(2000, 12, 13))

# Tạo đối tượng DanhSachSV và thêm sinh viên
danhSach = DanhSachSV()
danhSach.themSinhVien(sv1)
danhSach.themSinhVien(sv2)
danhSach.themSinhVien(sv3)

# Xuất danh sách sinh viên  
danhSach.xuat()

ngaySoSanh = dt.date(2000, 6, 15)
sinhVienTruocNgay = danhSach.timSvTruocNgay(ngaySoSanh)

print("\nSinh viên sinh trước ngày 15-6-2000: ")
for sv in sinhVienTruocNgay:
        print(sv)

print("\nTìm sinh viên tên Nam ")
tenCanTim = "Nguyen van Nam"
sinhVienTheoTen = danhSach.timSvTheoTen(tenCanTim)
for sv in sinhVienTheoTen:
        print(sv)
