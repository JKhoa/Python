from sinh_vien_chinh_quy import SinhVienChinhQuy
from sv_phi_chinh_quy import SinhVienPhiCQ
from sinh_vien import SinhVien

class DanhSachSv:
    def __init__(self):
        self.dssv = []
    def themSV(self, sv: SinhVien) :
        self.dssv.append(sv)
    def xuat(self):
        for sv in self.dssv:
            print(sv)
    def timSVTheoMs(self, ms: int):
        for i in range(len(self.dssv)):
            if self.dssv[i].maso == ms:
                return i
        else:
            return -1
    def timSvTheoLoai(self, loai: str):
        if loai =="chinhquy":
            return [sv for sv in self.dssv if isinstance(sv, SinhVienChinhQuy)]
        return [sv for sv in self.dssv if isinstance(sv, SinhVienPhiCQ)]