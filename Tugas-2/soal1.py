print('Selamat Datang')

daftar_kontak = []

def show_menu():
    print('--Menu--')
    print('1. Daftar Kontak')
    print('2. Tambah Kontak')
    print('3. Keluar')

def show_contact():
    print('Daftar Kontak')
    for kontak in daftar_kontak:
        print('Nama: ' + kontak['nama'])
        print('No Telepon: ' + kontak['telp'])

def add_contact():
    nama = input('Nama : ')
    telp = input('No Telepon : ')
    kontak = {
        'nama' : nama,
        'telp' : telp
    }
    daftar_kontak.append(kontak)
    print('Kontak berhasil ditambahkan')

while True:
    show_menu()

    menu = input('pilih menu: ')

    if menu == '1':
        show_contact()
    
    elif menu == '2':
        add_contact()
    elif menu == '3':
        print('Program selesai, Sampai Jumpa! ')
        break
    else:
        print('Menu tidak tersedia')
