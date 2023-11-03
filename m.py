class Buku:
    def __init__(self,judul,penulis,penerbit,harga):
        self.judul=judul 
        self.penulis=penulis
        self.penerbit=penerbit
        self.harga=harga
    def cetak(self):
        print(f"Buku ini berjudul : {self.judul}")
        print(f"Buku ini ditulis oleh : {self.penulis}")
        print(f"Buku ini diterbitkan oleh : {self.penerbit}")
        print(f"Buku ini berharga : {self.harga}")
class Tokobuku:
    def __init__(self,):
        self.daftar_buku=[]
    def tambah_buku(self,buku):
        self.daftar_buku.append(buku)
    def cari_buku(self,judul):
        for buku in self.daftar_buku:
            if buku.judul==judul:
                return buku
            else:
                none
def main():
    buku1 = Buku("Harry Potter dan Batu Bertuah", "J.K. Rowling", "Bentang Pustaka", 100000)
    buku2 = Buku("The Lord of the Rings", "J.R.R. Tolkien", "Gramedia", 200000)
    
    toko_buku = TokoBuku()
    toko_buku.tambah_buku(buku1)
    toko_buku.tambah_buku(buku2)
    
    print("Daftar buku di toko:")
    for buku in toko_buku.daftar_buku:
        buku.cetak()
    
    buku_dicari = toko_buku.cari_buku("Harry Potter dan Batu Bertuah")
    if buku_dicari is not None:
        buku_dicari.cetak()
        
if __name__=="__main__":
    main()
                