barang = []
tujuan = []
pengiriman = []

loop = True

print('================== Paket ==============')
print('1. Tambah Daftar Parang Kiriman')
print('2. List Beli')
print('3. Keluar')
print('======================================')
while (loop):

    paket = input('Masukan Pilihan = ')

    if paket == "1":
        print("==============")
        print('Silahkan Masukan Paket yang Anda Ingin')
        print('====================== Daftar  ===================')
        tambah_paket = (input('Mau Kirim Apa :  '))
        tambah_tujuan = (input('Masukan Tujuan Anda :  '))
        tambah_pengiriman = (input('Mau Berapa Lama :  '))
        barang.append(tambah_paket)
        tujuan.append(tambah_tujuan)
        pengiriman.append(tambah_pengiriman)
    elif paket == "2":
        print('===== List Belanja =====')
        for i in range(0, len(barang)):
            info_barang = barang[i]
            info_tujuan = tujuan[i]
            info_pengiriman = pengiriman[i]
            print(
                f'anda mengirim {info_barang} dengan tujuan {info_tujuan} dan Estimasi waktu {info_pengiriman}')
    elif paket == "3":
        print('terimakasih telah memilih layaanan kami, permintaan anda akan kamu proses')
        break
    else:
        print("Masukan Menu Dengan Benar")
