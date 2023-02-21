
nama = "Mizard"
nim = 5220411093

#1
print("Nama Saya : ",nama)

#2
print("Nama Saya : "+ nama)

#3
print("Nama Saya : {}".format(nama))

#4
print(f"Nama Saya : {nama}")

#5
print("Nama Saya : %s" %(nama))

#Mengubah string menjadi kapital
print(nama.upper())

#Mengubah string menjadi kecil
print(nama.lower())

#Mengubah string dalam kalimat
print(nama.replace(nama,"Mz"))

#Mencari tau awalan string
no_hp = ["+6289529449568", "+123456789"]
for i in no_hp:
    if i.startswith("+62"):
        print("Ini momor indonesia",i)
    else:
        print("Bukan Nomor indonesia")

#Mencari akhiran string
gmail = "mizardalb@gmail.com"
if gmail.endswith("gmail.com"):
    print("Ini Gmail")

if no_hp.startswith("+62"):
#mengubah yahoo.com menjadi gmail.com
    print("Ini momor indonesia")

list1 = ["mizard@gmail.com", "kepin@yahoo.com","aryan@gmail.com"]
gmail = []
for item in list1:
    if item.endswith("yahoo.com"):
        gmail.append(item.replace("yahoo.com","gmail.com"))
    else:
        gmail.append(item)
print(gmail)


list1 = ["mizard@gmail.com", "kepin@yahoo.com","aryan@gmail.com"]
gmail = []
for item in list1:
    if item.endswith("gmail.com"):
        gmail.append(item.replace("gmail.com","yahoo.com"))
    else:
        gmail.append(item)
print(gmail)

list1 = ["mizard@gmail.com", "kepin@yahoo.com","aryan@gmail.com"]
gmail = []
for i in list1:
    if i.endswith("yahoo.com"):
        i = i.replace("yahoo.com","gmail.com")
        gmail.append(i)
print(gmail)
