barang = []
tujuan = []
pengiriman = []
    
loop = True
 
print('================== paket ==============')
print('1. Tambah Daftar barang kiriman')
print('2. List Beli')
print('3. Keluar')
print('======================================')
while (loop):
       
    paket = input('Masukan pilihan = ')
 
    if paket == "1":
        print("==============")
        print('Silahkan Masukan paket yang anda ingin')
        print('====================== Daftar beli ===================')
        tambah_paket = (input('Mau Kirim Apa :  '))
        tambah_tujuan = (input('Masukan Tujuan Anda :  '))
        tambah_pengiriman = (input('Mau Berapa Lama :  '))
        barang.append(tambah_paket)
        tujuan.append(tambah_tujuan)
        pengiriman.append(tambah_pengiriman)
    elif paket == "2":
        print('===== List Belanja =====')
        for i in range(0,len(barang)):
            info_barang = barang[i]
            info_tujuan = tujuan[i]
            info_pengiriman = pengiriman[i]
            print(f'anda mengirim {info_barang} dengan tujuan {info_tujuan} dan Estimasi waktu {info_pengiriman}')
    elif paket== "3":
        quit()
    else:
        print("Masukan Menu Dengan Benar")
       