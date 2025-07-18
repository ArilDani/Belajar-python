print("==========input==========")
#input
nama = input("masukkan nama:") #input digunakan untuk mengambil data nama dari user
umur = input("masukkan umur:") #input digunakan untuk mengambil data umur dari user
hobi = input("masukkan hobi:") #input digunakan untuk mengambil data hobi dari user
print("nama saya ",nama,"saya berumur ",umur, "hobi saya adalah ",hobi) #print digunakan untuk menampilkan data yang di input oleh user

print("==========casting tipe data==========")
#casting tipe data
#string
data = input("masukkan data string :")
print("data = ",data,"type =",type(data))
#data_int = int(data) #casting string ke integer akan eror karena string tidak bisa diubah menjadi integer
#data_float = float(data) #casting string ke float akan eror jika string tidak bisa diubah menjadi float
data_bool = bool(data) #casting string ke boolean akan selalu menghasilkan True
#print("data = ",data_int,"type =",type(data_int))
#print("data = ",data_float,"type =",type(data_float))
print("data = ",data_bool,"type =",type(data_bool))

#integer
data = input("masukkan data integer :")
print("data = ",data,"type =",type(data))
data_str = str(data) #casting integer ke string akan menghasilkan string, walaupun angka hasilnya akan "1" string
data_float = float(data) #casting integer ke float akan menghasilkan float
data_bool = bool(data) #casting integer ke boolean akan menghasilkan True jika data tidak 0 dan False jika data 0
print("data = ",data_str,"type =",type(data_str))
print("data = ",data_float,"type =",type(data_float))
print("data = ",data_bool,"type =",type(data_bool))

#float
data = input("masukkan data float :")
print("data = ",data,"type =",type(data))
data_str = str(data) #casting float ke string akan menghasilkan string, walaupun angka hasilnya akan "1.0" string
data_int = int(float(data)) #casting float ke integer akan menghasilkan integer, angka dibulatkan ke bawah
data_bool = bool(data) #casting float ke boolean akan menghasilkan True jika data tidak 0
print("data = ",data_str,"type =",type(data_str))
print("data = ",data_int,"type =",type(data_int))
print("data = ",data_bool,"type =",type(data_bool))

#boolean
data = input("masukkan data boolean (True/False) :")
print("data = ",data,"type =",type(data))
data_str = str(data) #casting boolean ke string akan menghasilkan string "True" atau "False"
data_int = int(data == "True") #casting boolean ke integer akan menghasilkan 1 untuk True dan 0 untuk False
data_float = float(data) #casting boolean ke float akan menghasilkan 1.0 untuk True dan 0.0 untuk False
print("data = ",data_str,"type =",type(data_str))
print("data = ",data_int,"type =",type(data_int))
print("data = ",data_float,"type =",type(data_float))














