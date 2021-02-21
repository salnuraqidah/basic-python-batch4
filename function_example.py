nama_buah = []

def tambah_nama_buah(nama):
    nama_buah.append(nama)
    print_nama_buah()

def print_nama_buah():
    for buah in nama_buah:
        print(buah)
    print('----')

tambah_nama_buah("jeruk")
tambah_nama_buah("melon")
tambah_nama_buah("semangka")
