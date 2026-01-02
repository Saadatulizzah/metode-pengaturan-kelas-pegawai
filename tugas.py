#tugas pertama
data=[1,4,3,0,8,6]
print("data awal =", data)
tukar=5
while tukar>0:
    tukar=0
    for i in range(0,5):
        if data[i]<data[i+1]:
            s=data [i]
            data[i]=data[i+1]
            data[i+1]=s
            tukar=tukar+1
print("data akhir =", data)
data=[1,4,3,0,8,6]
print("data awal =", data)
tukar=5
while tukar>0:
    tukar=0
    for i in range(0,5):
        if data[i]>data[i+1]:
            s=data [i]
            data[i]=data[i+1]
            data[i+1]=s
            tukar=tukar+1
print("data akhir =", data)           
data=[1,4,3,0,8,6]
print("data awal =", data)
tukar=5
while tukar>0:
    tukar=0
    for i in range(0,5):
        if data[i]>data[i+1]:
            s=data [i]
            data[i]=data[i+1]
            data[i+1]=s
            tukar=tukar+1 
i = 1 #cari posisi 3 dahulu
while i < 5:# fungsi wile sebagai perulangan sesuai index yang di masukin
    if data[i] == 3: #posisi nilai 3
        x = i
    i=i+1
while x<5: # tukar dengan menggeser
    s = data[x]
    data[x] = data[x + 1]
    data[x + 1] = s 
    x=x+1
print("data akhir=", data)
data=[1,4,3,0,8,6]
print("data awal =",data)
tukar = 1
while tukar > 0:
    tukar=0
    for i in range(0,3):
        if data[i]>data[i+1]:
            s=data [i]
            data[i]=data[i+1]
            data[i+1]=s
            tukar=tukar+1
tukar = 1
while tukar > 0:
    tukar = 0
    for i in range(3,5):
        if data[i]<data[i+1]:
            s=data [i]
            data[i]=data[i+1]
            data[i+1]=s
            tukar=tukar+1 
print("data akhir =",data)
#===================================
#tugas ke 2
class pegawai:
     def __init__(self, nama, jarak, usia, jabatan):
         
         self.nama = nama
         self.jarak = jarak
         self.usia = usia
         self.jabatan = jabatan

     def josjiz(self):
         jumlah = 0 #niali awal e 0
         for huruf in self.nama:
             jumlah +=1 #nak ketemu huruf tambah 1
         return jumlah
     def musafir(self):
         data={"semarang":5,
               "rembang":8,
               "tuban":15,
               "kediri":25,}
         print('data awal=', data)
         jarak = data[self.jarak] 
         if jarak > 10:
             return "Jauh"
         else:
             return "Dekat"
     def gen(self): #logika if,elif,else
         if self.usia < 25:
             return "muda"
         elif 25 <= self.usia <= 50 :
             return "tua"
         else :
             return "lansia"
     def tahta(self):
         data={1:12_000_000,
               2:5_000_000,
               3:8_000_000,
               4:3_000_000,}
         print('data awal=', data)
         gaji = self.jabatan
         if self.jabatan < 5000000:
             return "golongan 1"
         elif 5000000 <= gaji <= 10000000 :
             return "golongn 2"
         else :
             return "golongan 3"
     def __str__(self):
          return f"{self.nama} dari kota {self.jarak} dia berumur{self.usia} tahun dan memiliki gaji {self.jabatan}  "

                   
pegawai1=pegawai("zize","rembang", 20, 12_000_000)
pegawai2=pegawai("marni","semarang", 54,5_000_000 )
pegawai3=pegawai("aqila","tuban", 25, 8_000_000)
pegawai4=pegawai("fattah","kediri", 27, 3_000_000)

print("kota ini berjumlah", pegawai1.josjiz(),"huruf")
print("kota ini berjumlah", pegawai2.josjiz(),"huruf")
print("kota ini berjumlah", pegawai3.josjiz(),"huruf")
print("kota ini berjumlah", pegawai4.josjiz(),"huruf")
print(pegawai4.musafir())
print(pegawai1.musafir())
print(pegawai3.musafir())
print(pegawai2.musafir())
print(pegawai2.gen(),"umur hanyalah angka selalu berbuat baiklah kepada manusia")
print(pegawai1.gen(),"umur hanyalah angka selalu berbuat baik kepada manusia")
print(pegawai3.gen(),"umur hanyalah angka selalu berbuat baik lah pada manusia")
print(pegawai3.tahta())
print(pegawai2.tahta())
print(pegawai4.tahta())
print(pegawai1.tahta())
print(pegawai1)
print(pegawai2)


