nilai_minimum = 70
teori = float(input("Nilai ujian teori : "))
praktek = float(input("Nilai ujian praktek : "))

if teori>=nilai_minimum and praktek>=nilai_minimum:
    print("Selamat, anda lulus!")
elif teori>=nilai_minimum and praktek<nilai_minimum:
    print("Anda harus mengulang ujian praktek")
elif teori<nilai_minimum and praktek>=nilai_minimum:
    print("Anda harus mengulang ujian teori")
else:
    print("Anda harus mengulang ujian teori dan praktek")