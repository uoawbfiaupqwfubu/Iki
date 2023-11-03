class mahasiswa:
    status="mahasiswa"
    def __init__(self,nama,kelas) -> None:
        self.nama=nama
        self.kelas=kelas
    def keterangan(self):
        print(f"Nama {self.nama} status {self.status} dari kelas {self.kelas}")
data=mahasiswa("joko","Sistem informasi")
data.keterangan()

class Nilai(mahasiswa):
    def __init__(self, nama, kelas) -> None:
        super().__init__(nama, kelas)
        self.nilai_update=[]
    def input_nilai(self,tambah):
        return self.nilai_update.append(tambah)
budi=Nilai('budi',13)
budi.keterangan()
    


