import tgs1

print('Selamat datang di program Manajemen Stok Barang!')
print('Pilihan : ')
print('1. Tambah Data Barang')
print('2. Edit Data')
print('3. Hapus Data Barang')
print('4. Cari Data')
print('5. Tampilkan Data Barang')
print('6. Tampilkan Jumlah Data')
print('7. Keluar')

while True:
    pilihan = int(input('Masukan Pilihan : '))
    print('=================')
    if pilihan == 1 :
        tgs1.tambah_data_barang()
    elif pilihan == 2 :
        tgs1.edit_barang()
    elif pilihan == 3 :
        tgs1.hapus_data_barang()
    elif pilihan == 4 :
        tgs1.cari_data()
    elif pilihan == 5 :
        tgs1.tampilkan_data()
    elif pilihan == 6 :
        tgs1.tampilkan_jumlah_data()
    else:
        pilihan == 7
        print('Terimakasih 😊')
        break



