from sinh_vien import SinhVien
from datetime import datetime   

class SinhVienPhiCQ(SinhVien):
    def __init__(self, maso: int, hoTen: str, ngaySinh: datetime,trinhdo: str, tgdt: int)->None:
        super().__init__(maso, hoTen, ngaySinh)
        self.thoiGianDaoTao = tgdt
        self.trinhDo = trinhdo
    def __str__(self):
        return f"{super().__str__()}\t{self.thoiGianDaoTao}\t{self.trinhDo}"