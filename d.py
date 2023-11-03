import numpy as np

dtipe=[('nama','S10'),('tinggi',int)]
data=[
    ('udin',170),
    ('ucup',168),
    ('dadang',167)
]
a=np.array(data, dtype=dtipe)
print(a)
print(np.sort(a, order='nama'))

def menghitung_sisi_kubus(a,b,c):
    hasil=a*b*c
    return hasil
hitung=menghitung_sisi_kubus(5,5,5,)
print(hitung)
    