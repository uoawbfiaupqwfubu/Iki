class kucing:
    def __init__(self,nama) -> None:
        self.nama=nama
    def respon(self):
        print(self.nama + " Meong-meong")
    
class anjing:
    def __init__(self,nama) -> None:
        self.nama=nama
    def respon(self):
        print(self.nama + " Guk guk ")
riri=kucing(nama="riri")
bono=anjing(nama="bono")
riri.respon()
bono.respon()

for binatang in [riri,bono]:
    print(type(binatang))
    print(binatang.respon())
