import random 
pilihan=['batu','gunting','kertas']
pilihan_pemain=input("Pilih diantara batu/gunting/kertas:")
pilihan_komputer=random.choice(pilihan)

print(f"anda memilih {pilihan_pemain}")
print(f"komputer memilih {pilihan_komputer}")
if pilihan_pemain == pilihan_komputer:
    print("seri!!!")
elif pilihan_pemain == "batu":
    if piihan_komputer == "gunting":
        print("Pemain menang")
    else:
        print("Pemain kalah")
elif pilihan_pemain == "gunting":
    if pilihan_komputer == "kertas":
        print("pemain menang")
    else:
        print("pemain kalah")
elif pilihan_pemain == "kertas":
    if pilihan_komputer == "batu":
        print("pemain menang")
    else:
        print("pemain kalah")