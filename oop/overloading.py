"""
properti polimorfik -> overloading (kelebihan beban operator) <-
yaitu anda memberitahu operator tertentu untuk menangani operasi
antara objek kelas dengan cara tertentu dengan mendefinisikan metode
khusus dari operator tersebut.

metode khusus add()
"""

"""
overloading dalam operator penjumlahan, kemampuan operator penjumlahan
untuk berperilaku berbeda dalam kasus yang berbeda

metode add yang disebut sebagai operator overloading atau overloading
operator tambahan
"""

class Square:
    def __init__(self, side):
        self.side = side
    
    # overloading (ada tanda __ )
    def __add__(squareOne, squareTwo):
        return((4 * squareOne.side) + (4 * squareTwo.side))

squareOne = Square(5) # 5*4=20
squareTwo = Square(10) # 10*4=40
print("Sum of sides of both the squares = ", squareOne + squareTwo)