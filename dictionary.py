pelanggan = {
    "nama" : "Astuti",
    "umur" : 20
}
# print(type(pelanggan))

pelanggan_2 = {
    "nama" : "Joko",
    "umur" : 23
}

# print("Nama : {}".format(pelanggan["nama"]))
# print("Umur : {}".format(pelanggan["umur"]))

#change value of dictionary
pelanggan["umur"] = 21

# print(pelanggan)

#loop through dict
for x in pelanggan:
    print(x) #key
    print(pelanggan[x]) #akses value
    print(pelanggan_2[x]) #akses value

daftar_pelanggan = []
daftar_pelanggan.append(pelanggan)
daftar_pelanggan.append(pelanggan_2)

print(daftar_pelanggan)

for pelanggan in daftar_pelanggan:
    print("Nama: {}".format(pelanggan['nama']))
    print("Umur: {}".format(pelanggan['umur']))

