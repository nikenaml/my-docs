"""
Abstract Base Class (kelas dasar abstrak) = kelas yang tidak memiliki definisi sendiri.
ini memiliki metode abstrak yang memaksa implementasi di kelas turunannya.
-> ABC merupakan kelas dasar yang terdiri dari metode abstrak yang harus didefinisikan
ulang dalam kelas turunannya.

Cara membuat ABC, pelu membuat instance class/kelas turunan dari kelas lain.
perlu memasukkan metaclass dengan maksud = bentuk kelas sebagai turunan dari kelas
ABCMeta. sekarang ABCMeta adalah kelas yang memiliki properti dari kelas dasar abstrak.
jadi dengan ada metaclass dapat memastikan bahwa bentuk sekarang menjadi kelas dasar
abstrak.
-> kelas dasar abstrak anda tidak akan memiliki definisi sendiri. hanya akan berisi metode abstrak.

-> artinya disini bahwa metode disini dalam bentuk kelas anda tidak akan memiliki
definisi sendiri tetapi harus memiliki definisi di kelas turunannya.
dan anda memastikannya dengan menjadikannya sebagai metode abstrak
-> bagaimana menjadikannya sebagai metode abstrak?
-> cara membuatnya dengan menjadikan kelas itu sebagai turunan dari kelas lain ABCMeta
dengan menjadikan kelas itu sebagai kelas turunan dari kelas lain ABCMeta
(metaclass = ABCMeta)
dengan menggunakan dekorator bernama @abstractmethod. dekorator method abstrak tersebut
dan kelas ABCMeta termasuk dalam modul 'abc' python.
--> cara menggunakan ABCMeta dan @abstractmethod, kita perlu melakukan import keduanya dari modul itu
--> selanjutnya buat kelas dasar abstrak sebagai kelas induk/dasar dalam class persegi dan persegi panjang.
----> lakukan hal ini dengan Inheritance
---> kemudian hapus fungsi awal yang sudah di definisikan di class masing2

from abc import ABCMeta, abstractmethod
class Shape(metaclass = ABCMeta):
    @abstractmethod
    def area(self):
        return 0

--> menggunakan kelas dasar abstrak yang mengimplementasikan metode abstrak yang disebut area()
--> untuk memaksa kelas turunan dapat megimplementasikan metode dengan
memanfaatkan kelas dasar abstrak
--> shape = Shape()
kelas dasar abstrak seharusnya tidak dapat membuat instance objek untuk dirinya sendiri/
tidak dapat membuat instance bentuk kelas abstrak. kelas abstrak hanya dapat diwarisi dalam
kelas turunannya

"""

from abc import ABCMeta, abstractmethod

class Shape(metaclass = ABCMeta):
    @abstractmethod
    def area(self):
        return 0

class Square(Shape):
    side = 4
    def area(self):
        print("Area of square: ", self.side * self.side)

class Rectangle(Shape):
    width = 5
    length = 10
    def area(self):
        print("Area of rectangle: ", self.width * self.length)

square = Square()
rectangle = Rectangle()
square.area()
rectangle.area()
# shape = Shape()
"""
kelas dasar abstrak seharusnya tidak dapat membuat instance objek untuk dirinya sendiri/
tidak dapat membuat instance bentuk kelas abstrak. kelas abstrak hanya dapat diwarisi dalam
kelas turunannya
"""