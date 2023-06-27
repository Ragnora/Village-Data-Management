import os,time,pandas,csv

data = [{'NIK': 3525015201880002, '   Nama': 'Lintang', '   Jenis Kelamin': 'Perempuan', '   Umur': 20,'   Alamat': 'Jember','   No HP': '081'},
         {'NIK': 3123456789123456, '   Nama': 'Dika', '   Jenis Kelamin': 'Laki-laki', '   Umur': 21, '   Alamat': 'Jember','   No HP': '082'},
         {'NIK': 3525016005650004, '   Nama': 'Nabil', '   Jenis Kelamin': 'Laki-laki', '   Umur': 17, '   Alamat': 'Situbondo','   No HP': '083'},
         {'NIK': 3525015306780002, '   Nama': 'Wahyu', '   Jenis Kelamin': 'Laki-laki', '   Umur': 23, '   Alamat': 'Banyuwangi','   No HP': '084'},
         {'NIK': 3525015306780002, '   Nama': 'Rainey', '   Jenis Kelamin': 'Perempuan', '   Umur': 21, '   Alamat': 'Surabaya','   No HP': '085'},
         {'NIK': 3525017006620060, '   Nama': 'Foxy', '   Jenis Kelamin': 'Perempuan', '   Umur': 22, '   Alamat': 'Surabaya','   No HP': '086'},
         {'NIK': 3525016401830001, '   Nama': 'Marvel', '   Jenis Kelamin': 'Laki-laki', '   Umur': 15, '   Alamat': 'Situbondo','   No HP': '087'},
         {'NIK': 3314076404720003, '   Nama': 'Naufal', '   Jenis Kelamin': 'Laki-laki', '   Umur': 19, '   Alamat': 'Sidoarjo','   No HP': '088'},
         {'NIK': 3525016401830001, '   Nama': 'Ava', '   Jenis Kelamin': 'Laki-laki', '   Umur': 18, '   Alamat': 'Semarang','   No HP': '089'},
         {'NIK': 3525015002690001, '   Nama': 'Ragnora', '   Jenis Kelamin': 'Perempuan', '   Umur': 19, '   Alamat': 'Jember','   No HP': '090'},
         {'NIK': 3525016011620001, '   Nama': 'Clause', '   Jenis Kelamin': 'Laki-laki', '   Umur': 19, '   Alamat': 'Jember','   No HP': '091'},
         {'NIK': 3525013006770017, '   Nama': 'Lucas', '   Jenis Kelamin': 'Laki-laki', '   Umur': 20, '   Alamat': 'Jember','   No HP': '092'},
         {'NIK': 3525014305710001, '   Nama': 'Charlie', '   Jenis Kelamin': 'Laki-laki', '   Umur': 30, '   Alamat': 'Jember','   No HP': '093'},
         {'NIK': 3525011512820002, '   Nama': 'Joy', '   Jenis Kelamin': 'Laki-laki', '   Umur': 35, '   Alamat': 'Jember','   No HP': '094'},
         {'NIK': 3525016211930001, '   Nama': 'Amri', '   Jenis Kelamin': 'Laki-laki', '   Umur': 40, '   Alamat': 'Jember','   No HP': '095'},
         {'NIK': 3525017006520020, '   Nama': 'Sayyid', '   Jenis Kelamin': 'Laki-laki', '   Umur': 29, '   Alamat': 'Jember','   No HP': '096'},
         {'NIK': 3525012005590001, '   Nama': 'Reo', '   Jenis Kelamin': 'Laki-laki', '   Umur': 20, '   Alamat': 'Jember','   No HP': '097'},
         {'NIK': 3525014908920001, '   Nama': 'Winter', '   Jenis Kelamin': 'Perempuan', '   Umur': 25, '   Alamat': 'Jember','   No HP': '098'},
         {'NIK': 3326160107400474, '   Nama': 'Knoby', '   Jenis Kelamin': 'Laki-laki', '   Umur': 27, '   Alamat': 'Jember','   No HP': '099'},
         {'NIK': 3326161606790002, '   Nama': 'Hector', '   Jenis Kelamin': 'Laki-laki', '   Umur': 26, '   Alamat': 'Jember','   No HP': '100'},
         {'NIK': 3326164410800003, '   Nama': 'Syri', '   Jenis Kelamin': 'Perempuan', '   Umur': 29, '   Alamat': 'Jember','   No HP': '101'},
         {'NIK': 3326167001090001, '   Nama': 'Sandpy', '   Jenis Kelamin': 'Perempuan', '   Umur': 24, '   Alamat': 'Jember','   No HP': '102'},
         {'NIK': 3326160706800001, '   Nama': 'Albi', '   Jenis Kelamin': 'Perempuan', '   Umur': 23, '   Alamat': 'Jember','   No HP': '103'},
         {'NIK': 3326162610790021, '   Nama': 'Chess', '   Jenis Kelamin': 'Perempuan', '   Umur': 18, '   Alamat': 'Jember','   No HP': '104'},
         {'NIK': 3326164107440286, '   Nama': 'Snowy', '   Jenis Kelamin': 'Perempuan', '   Umur': 31, '   Alamat': 'Jember','   No HP': '105'},
         ]

def clean():
    os.system('cls')

def menu():
    print('='*73)
    print('\t\t\t     SELAMAT DATANG')
    print('='*73)
    print('\t\t Silahkan Masukan Username dan Password!')
    print(' ')
    user = []
    with open ('user.csv') as usr:
        username = csv.reader(usr)
        for i in username:
            user.append(i)
    un = input('Username: ')
    pw = input('Password: ')
    print('')
    time.sleep(1)
    halamanUtama()if [un,pw] in user else print('\t\t      Username atau Password Salah!')
    print('-'*73)
    print('')
    time.sleep(1)
    input('Ketik Apapun Untuk Memuat Ulang: ')
    time.sleep(1)
    clean()
    menu()

def halamanUtama():
    clean()
    print('='*73, '\n',
    '\t\t\t      DATA PENDUDUK DESA', '\n'+
    '='*73, '\n',
    ' ', '\n'+
    '1. Cari Data', '\n'+
    '2. Tampilkan Data')
    print(' ')
    user = input('Pilih Nomor: ')
    print(' ')
    time.sleep(1)
    dataFilter() if user=='1' else (dataSort() if user=='2' else print('\t\t    Pilih Sesuai Nomor Yang Tersedia!'))
    print('-'*73)
    print(' ')
    time.sleep(1)
    input('Ketik Apapun Untuk Memuat Ulang: ')
    time.sleep(1)
    halamanUtama()

#---------------------------------------------------Filter---------------------------------------------------#

def dataFilter():
    clean()
    print('='*73)
    print('\t\t\t\tCARI DATA')
    print('='*73)
    print(' ')
    print('Cari data berdasarkan: ')
    print('1. NIK')
    print('2. Nama')
    print('3. Umur')
    print('4. Alamat')
    print('5. No HP')
    print('6. Kembali')
    print(' ')
    user = input('Pilih Nomor: ')
    print(' ')
    time.sleep(1)
    dataFilterNIK() if user=='1' else (dataFilterNama() if user=='2' else (dataFilterUmur() if user=='3' else (dataFilterAlamat() if user=='4' else (dataFilterNoHP() if user=='5' else (halamanUtama() if user=='6' else print('\t\t    Pilih Sesuai Nomor Yang Tersedia!'))))))
    print('-'*73)
    print(' ')
    time.sleep(1)
    input('Ketik Apapun Untuk Kembali : ')
    time.sleep(1)
    dataFilter()

def dataFilterNIK():
    clean()
    user = input('Masukan NIK: ')
    nik = [dataNIK for dataNIK in data if dataNIK['NIK']==int(user)]
    print(' ')
    print('Berikut ini data yang sudah di filter:')
    print('-'*73)
    df = pandas.DataFrame(nik)
    print(df)

def dataFilterNama():
    clean()
    user = input('Masukan Nama: ')
    nama = [dataNama for dataNama in data if dataNama['   Nama']==user]
    print(' ')
    print('Berikut ini data yang sudah di filter:')
    print('-'*73)
    df = pandas.DataFrame(nama)
    print(df)

def dataFilterUmur():
    clean()
    user = input('Masukan Umur: ')
    umur = [dataUmur for dataUmur in data if dataUmur['   Umur']==int(user)]
    print(' ')
    print('Berikut ini data yang sudah di filter:')
    print('-'*73)
    df = pandas.DataFrame(umur)
    print(df)

def dataFilterAlamat():
    user = input('Masukan Alamat: ')
    alamat = [dataNama for dataNama in data if dataNama['   Alamat']==user]
    print(' ')
    print('Berikut ini data yang sudah di filter:')
    print('-'*73)
    df = pandas.DataFrame(alamat)
    print(df)

def dataFilterNoHP():
    clean()
    user = input('Masukan No HP: ')
    noHP = [dataNoHP for dataNoHP in data if dataNoHP['   No HP']==user]
    print(' ')
    print('Berikut ini data yang sudah di filter:')
    print('-'*73)
    df = pandas.DataFrame(noHP)
    print(df)
#---------------------------------------------------Filter---------------------------------------------------#



#---------------------------------------------------Sort---------------------------------------------------#

def dataSort():
    clean()
    print('='*73)
    print('\t\t\t  TAMPILKAN DATA PENDUDUK')
    print('='*73)
    print(' ')
    print('Urutkan data berdasarkan: ')
    print('1. Nama')
    print('2. Umur')
    print('3. Alamat')
    print('4. Kembali')
    print(' ')
    user = input('Pilih Nomor: ')
    print(' ')
    dataSortNama() if user=='1' else (dataSortUmur() if user=='2' else (dataSortAlamat() if user=='3' else (halamanUtama() if user=='4' else print('\t\t    Pilih Sesuai Nomor Yang Tersedia!'))))
    print('-'*73)
    print(' ')
    time.sleep(1)
    input('Ketik Apapun Untuk Kembali: ')
    time.sleep(2)
    dataSort()

def mySort(list_, func, key):
    if len(list_) < 2:
        return list_
    if len(list_) == 2:
        return list_ if func(list_[0], key) <= func(list_[1], key) else [list_[1], list_[0]] 
    result = [list_[0]] + mySort([list_[1]]+list_[2:], func, key) if func(list_[0], key) <= func(list_[1], key) else [list_[1]] + mySort([list_[0]]+list_[2:], func,key)
    return mySort(result[:-1], func, key)+result[-1:]

def dataSortNama():
    clean()
    print('='*73)
    print('\t\t\t    DATA PENDUDUK DESA')
    print('\t\t\t       Menurut Nama')
    print('='*73)
    x = (mySort(data, lambda x,y: x[y], '   Nama'))
    df = pandas.DataFrame(x)
    print(df)
    print('-'*73)

def dataSortUmur():
    clean()
    print('='*73)
    print('\t\t\t    DATA PENDUDUK DESA')
    print('\t\t\t       Menurut Umur')
    print('='*73)
    x = (mySort(data, lambda x,y: x[y], '   Umur'))
    df = pandas.DataFrame(x)
    print(df)
    print('-'*73)

def dataSortAlamat():
    clean()
    print('='*73)
    print('\t\t\t    DATA PENDUDUK DESA')
    print('\t\t\t      Menurut Alamat')
    print('='*73)
    x = (mySort(data, lambda x,y: x[y], '   Alamat'))
    df = pandas.DataFrame(x)
    print(df)
    print('-'*73)
#---------------------------------------------------Sort---------------------------------------------------#
menu()