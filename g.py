print("="*30)
print("Data umur penduduk desa suka suka")
print("="*30)
umur1=[]
while True:
  umr=int(input("Masukan umur anda:"))
  umur=[umr]
  umur1.append(umur)
  isLanjut=input("Apakah akan dilanjutkan?? y/n:")
  if isLanjut == "y":
    print("Program dilanjutkan!!!!")
  else:
    break
print(umur1)
umur1=sum(umur1,[])
for a in filter(lambda x: x > 18,umur1):
  print(a,end=' ')


    

