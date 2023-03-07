# OOP
# 1. class
# 2. inheritance / pewaris
# 3. setter & getter

class BangunDatar:
    def __init__(self, panjang, lebar):
        self.panjang = panjang
        self.lebar = lebar

    """
    SETTER DAN GETTER
    SETTER : method atau function yang kita gunakan untuk mengubah nilai caviable pada class
    GETTER : method atau function untuk mengambil nilai
    """
    def set_panjang(self, panjang):
        self.panjang = panjang
    
    def set_lebar(self, lebar):
        self.lebar = lebar

    def get_panjang(self):
        return self.panjang
    
    def get_lebar(self):
        return self.lebar

class PersegiPanjang(BangunDatar):
    def __init__(self, panjang, lebar):
        BangunDatar.__init__(self, panjang, lebar)

    def luas(self):
        # return BangunDatar.get_panjang(self) * BangunDatar.get_lebar(self)
        return self.panjang * self.lebar 
       
PP = PersegiPanjang(5,10)
print(PP.luas())
# rb = BangunDatar(5,10)
# rb.set_panjang(6)
# print(rb.get_panjang())


