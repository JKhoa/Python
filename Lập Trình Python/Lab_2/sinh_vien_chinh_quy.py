from sinh_vien import SinhVien
from datetime import datetime

class SinhVienChinhQuy(SinhVien):
    def __init__(self, maso: int, hoTen: str, ngaySinh: datetime, diemRL: int) -> None:
        super().__init__(maso, hoTen, ngaySinh)
        self.diemRL = diemRL
    def __str__(self):
        return super().__str__()+ f"\t{self.diemRL}"