"""
polimorphism dan overriding
-> polimorphism adalah karakteristik suatu entitas untuk dapat hadir
dalam lebih dari satu bentuk.
-> contoh kembar identik, keduanya terlihat sama, tetapi mereka tidak
sama. contoh dalam program python adalah penjumlahan antara dua angka,
jumlah mereka dikembalikan. tetapi ketika melakukan penambahan antara dua
string, rangkaian string yang akan dikembalikan.
operator penambahan ini terlihat sama tetapi berperilaku berbeda
-> contoh lain polymorphism = bapak mempunyai bakat memasak, menurun ke anak
tetapi cara anak memasak tidak sama persis dengan si bapak.
terlihat sama walaupun berbeda.
-> punya class sama namun dengan value yang berbeda

sifat polimorfik dari overriding
-> overriding merupakan bentuk polimorfisme dimana mendefinisikan ulang metode
basis kelas dalam kelas turunan.
--> penggantian dilakukan dengan mengubah perilaku metode kelas dasar di dalam 
kelas turunan. cara melakukannya, menggunakan nama metode yang sama dengan nama
kelas dasar di dalam kelas turunan dan mengubah badan metode didalam kelas turunan
anda.

-> overriding adalah mendefinisikan ulang metode kelas dasar di dalam kelas turunan
-> function super() digunakan untuk mengakses metode kelas dasar
function super() mengizinkan untuk memanggil method di kelas dasar, walaupun
ada kelas turunan yang memiliki method yang sama dengan kelas dasar (masih bisa
memanggal value dari kelas dasar, walaupun di kelas turunan 
sudah ada value yang berbeda). memanggil isi kelas dasar awal/menampilkan pengembalian
isi kelas dasar awal
"""

class Employee:
    def setNumberOfWorkingHours(self):
        self.numberOfWorkingHours = 40

    def displayNumberOfWorkingHours(self):
        print(self.numberOfWorkingHours)

class Trainee(Employee):
    def setNumberOfWorkingHours(self):
        self.numberOfWorkingHours = 45

    def resetNumberOfWorkingHours(self):
        super().setNumberOfWorkingHours()

employee = Employee()
employee.setNumberOfWorkingHours()
print("Number of working hours of employee: ", end = ' ')
employee.displayNumberOfWorkingHours()

trainee = Trainee()
trainee.setNumberOfWorkingHours()
print("Number of working hours of trainee: ", end = ' ')
trainee.displayNumberOfWorkingHours()

trainee.resetNumberOfWorkingHours()
print("Number of working hours of trainee after reset: ", end = ' ')
trainee.displayNumberOfWorkingHours()