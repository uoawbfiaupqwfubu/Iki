class Barang:
    penjual="Joko"
    def __init__(self,merek,harga,watt,unit) -> None:
        self.merek=merek
        self.harga=harga
        self.watt=watt
        self.unit=unit
    def detail_pembelian(self):
        print(f"Terimakasih telah membeli barang di toko {self.penjual} dengan pembelian barang {self.merek} dengan harga {self.harga} dan pemakaian watt sebesar{self.watt} dan pembelian unit sebanyak {self.unit}")
barang=Barang("Kulkas",1000000,100,1)
barang.detail_pembelian()

class Barang1(Barang):
    def __init__(self, merek, harga, watt, unit) -> None:
        super().__init__(merek, harga, watt, unit)
        self.Detail_tambahan=[]
    def Tambah(self,tambah):
        return self.Detail_tambahan.append(tambah)
pembeli=Barang1('ac',1500000,145,1)
pembeli.detail_pembelian()