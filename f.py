def data(n,m):
    print(f"{n}\n{m}")

while True:
    n=str(input("Masukan nama mu:"))
    m=int(input("Masukan umur mu:"))
    isLanjut=str(input("apakah akan dilanjutkan atau tidak y/n :"))
    if isLanjut == "y":
        print("Program dilanjutkan!!!")
    else:
        break
def main():
    with open("Data.txt", "a") as f:
        f.write(str(n))
        f.write(str(m))
    with open("Data.txt", "r") as f:
        Data=f.read()
        print(Data)


if __name__== "__main__":
    main()


