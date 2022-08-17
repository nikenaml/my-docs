"""
-> public = publik, bisa diakses dalam atau luar kelas, dalam atau luar inheritance 
(kertas ditempel di luar rumah, semua bisa lihat). dapat diakses dimana saja dalam program.
-> protected = dilindungi, dapat diakses di dalam kelas itu sendiri dan kelas turunannya. 
hanya kelas sendiri dan turunan yang bisa di akses (kertas ditempel di dalam rumah, 
yang bisa melihat anggota keluarga) 
-> private = rahasia/pribadi, menempelkan kerta di dalam kamar, yang bisa akses hanya 
class nya saja sendiri, kelas turunan tidak dapat akses. tidak boleh diakses di luar class.

Public = memberName
Protected = _memberName
Private = __memberName
"""

class Car:
    numberOfWheels = 4
    _color = "Black"
    __yearOfManufacture = 2017 # _Car__yearOfManufacture

class Bmw(Car):
    def __init__(self):
        print("Protected attribute color: ", self._color)

car = Car()
print("Public attribute numberOfWheels: ", car.numberOfWheels)
bmw = Bmw()
print("Private attribute yearOfManufacture: ", car._Car__yearOfManufacture)
"""
proses car._Car__yearOfManufacture, disebut sebagai mangling
ketika mendeklarasikan atribut dengan garis bawah ganda, itu akan
diawali dengan garis bawah tunggal dan nama kelas.
"""