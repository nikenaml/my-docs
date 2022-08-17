"""
misal, ayah mempunyai bakat bermain sepak bola, ibu pandai memasak, kedua keahlian itu dapat diturunkan
kepada anak. Namun, selain memiliki kedua keahlian tersebut, si anak juga memiliki keahlian sendiri seperti
pandai bernyanyi (kelas turunan ini menjadi kelas dasar dari kelas turunan lainnya)

jadi kelas turunan di tingkat paling bawah akan memiliki akses ke atribut dan metode ke keluarga kelas dasar
"""

class MusicalInstruments:
    numberOfMajorKeys = 12

class StringInstruments(MusicalInstruments):
    typeOfWood = "Tonewood"

class Guitar(StringInstruments):
    def __init__(self):
        self.numberOfStrings = 6
        print("This guitar consist of {} strings. It is made of {} and it can play {} keys".format(self.numberOfStrings, self.typeOfWood, self.numberOfMajorKeys))

guitar = Guitar()