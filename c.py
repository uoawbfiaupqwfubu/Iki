class binatang:
    hewan="mamalia"
    def __init__(self,kucing) -> None:
        self.kucing=kucing
    def respon(self):
        print(f"{self.kucing} meong-meong")
class binatang1:
    hewani="unggas"
    def __init__(self,burung) -> None:
        self.burung=burung
    def respon(self):
        print(f"{self.burung} caw-caw")
gagak=binatang1("gagak")
kcng=binatang("kucing")
gagak.respon()
kcng.respon()
for bnt in [gagak,kcng]:
    print(type(bnt))
    print(bnt.respon())