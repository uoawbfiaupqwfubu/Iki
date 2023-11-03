def hello_world():
    print("Hello world")
hello_world()

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

def main():
    n=int(input("Masukan angka n :"))
    try:
        print(factorial(n))
    except:
        print("Nilai n harus berupa positif!!")

    with open("nilai_n.txt", "w") as f:
        f.write(str(n))
    f.close()
    with open("nilai_n.txt", "r") as f:
        nilai_n=f.read()
        print(f"nilai_n adalah {nilai_n}")


if __name__== "__main__":
    main()
