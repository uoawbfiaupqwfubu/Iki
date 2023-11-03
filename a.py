class Tabungan:
    def __init__(self,nama,saldo) -> None:
        self.nama=nama
        self.saldo=saldo
    def setor(self,jumlah):
        self.saldo += jumlah
    def penarikan(self,jumlah):
        if self.saldo >= jumlah:
            self.saldo -= jumlah
        else:
            print("Tidak bisa menarik karena jumlah saldo tidak mencukupi!!!")
tabungan=Tabungan('Andi',980000)

print("="*30)
print("Selamat datang di ATM mini")
print("="*30)
print("="*30)
print(f"saldo awal anda adalah {tabungan.saldo}")
print("="*30)
print("1)Menabung\n2)Setor\n3)Tarik Tunai\n4)Exit")
pilih=str(input("Pilih setor atau tarik??:"))
if pilih == "1" :
    jumlah1=int(input("Masukan jumlah yang ingin di setor:"))
    tabungan.setor(int(jumlah1))
    print(f"Terimakasih telah menggunakan ATM mini kami sekarang saldo anda bertambah menjadi {tabungan.saldo}")
elif pilih == "2":
    jumlah=int(input("Masukan jumlah yang ingin di setor:"))
    tabungan.penarikan(int(jumlah))
    print(f"Terimakasih telah menggunakan ATM mini kami sekarang saldo anda berkurang menjadi {tabungan.saldo}")
elif pilih == "3":
    jumlah=int(input("Masukan jumlah yang ingin di tarik:"))
    tabungan.penarikan(int(jumlah))
    print(f"Terimakasih telah menggunakan ATM mini kami sekarang saldo anda berkurang menjadi {tabungan.saldo}")
else:
    print("Program berhenti")



