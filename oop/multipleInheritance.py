"""
misal, ayah mempunyai bakat bermain sepak bola, ibu pandai memasak, kedua keahlian itu dapat diturunkan
kepada anak
"""

class OperatingSystem:
    multitasking = True
    name = "Mac OS"

class Apple:
    website = "www.apple.com"
    name = "Apple"

"""
multiple inheritance akan mengambil value dari urutan di argumen class
disini argumen OperatingSystem duluan, artinya jika setiap class induk ada class attribut yang sama
(name), maka yang akan dipanggil adalah yang urutan duluan di panggil
yaitu name = "Mac OS"
"""

class MacBook(OperatingSystem, Apple):
    def __init__(self):
        if self.multitasking is True:
            print("This is a multi tasking system. Visit {} for more details".format(self.website))
            print("Name : ", self.name)

macBook = MacBook()
