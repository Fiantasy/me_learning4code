class persegi_panjang:
    def __init__(self, panjang, lebar):
        self.panjang = panjang
        self.lebar = lebar
    
    def luas(self):
        hitung_luas = self.panjang * self.lebar
        self.hitungl = hitung_luas
        return hitung_luas
        
    def keliling(self):
        hitung_keliling = self.hitungl * 2
        return hitung_keliling
    
    def is_square(self):
        return self.panjang == self.lebar
    
hitung = persegi_panjang(panjang= 10, lebar=5)
hitung.luas()
hitung.keliling()
print (f'{hitung.luas()} \n{hitung.keliling()}\nini adalah sebuah persegi: {hitung.is_square()}')

hitung1 = persegi_panjang(panjang= 7, lebar=7)
hitung1.luas()
hitung1.keliling()
print (f'{hitung1.luas()} \n{hitung1.keliling()}\nini adalah sebuah persegi: {hitung1.is_square()}')


class student:
    def __init__(self,nama,usia,jurusan):
        self.nama = nama
        self.usia = usia
        self.jurusan = jurusan
    def profil(self):
        print(f"Nama: {self.nama}\nUmur: {self.usia}\nJurusan: {self.jurusan}")
        
    def greet(self):
        print(f"Halo, {self.nama}! Selamat datang di {self.jurusan}")
        
murid = student(nama = "alfian", usia= 17, jurusan= "informatika")
murid.profil()
murid.greet()


class car:
    def __init__(self, brand, model, year, mileage):
        self.brand = brand
        self.model = model
        self.year = year
        self.mileage= mileage
        
    def drive(self, jarak):
        self.mileage -= jarak
    def get_info(self):
        print(f"Berikut Adalah Profil Mobil:\nMerek: {self.brand} \nModel: {self.model} \nTahun: {self.year} \nKilometer: {self.mileage} km")

mobil = car(brand = 'Toyota', model = 'Corolla', year = 2019, mileage = 25.000)
mobil.drive(jarak = 500 )
mobil.get_info()

class bank_account:
    def __init__(self, nomor_akun, pemilik_akun, saldo):
        self.nomor_akun = nomor_akun
        self.pemilik_akun = pemilik_akun
        self.saldo = saldo
    def deposit(self, jumlah):
        self.saldo = jumlah + self.saldo
    def penarikan(self, ditarik):
        if ditarik > self.saldo:
            print("saldo tidak mencukupi")
        else:
            self.saldo = self.saldo - ditarik
    def get_saldo(self):
        print(self.saldo)
        return self.saldo
    def profil(self):
        print(f'Halo {self.pemilik_akun} \nNomor akun anda: {self.nomor_akun} \nSaldo: {self.saldo}')

nasabah = bank_account(nomor_akun = 5207 , pemilik_akun= "alfian", saldo= 1000)
nasabah.profil()
nasabah.deposit(jumlah= 500)
nasabah.deposit(jumlah= 500)
nasabah.penarikan(ditarik=600)

nasabah.get_saldo()