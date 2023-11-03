class Rekening_Bank:
    def __init__(self,menabung) -> None:
        self.menabung=menabung
        tabung=int(input("Masukan jumlah uang yang ingin di tabungkan :"))
        self.menabung.append(tabung)
    def cek_saldo(self,saldo):
        self.saldo=saldo
        print(f"jumlah saldo tabungan anda adalah {self.saldo}")
    def menarik(self,menarik):
        self.menarik=menarik
    def mencetak_saldo(self,mencetak):
        self.mencetak=mencetak

