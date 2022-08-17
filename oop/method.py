#instance method
"""
method memiliki akses ke semua atribut

method dalam class yang menggunakan parameter self untuk
mengakses dan memodifikasi instance atribut dalam class.

method static adalah metode yang tidak mengambil parameter self

bagaimana cara membedakan instance method dengan static method?
dilakukan dengan memanfaatkan dekorator yang di sebut @staticmethod

dekorator adalah fungsi yang mengambil fungsi lain dan meluas fungsi mereka
dan mengabaikan pengikatan objek dan python kemudian memahami bahwa
pengikatan telah diabaikan, jadi tanpa self bisa dijalankan/tanpa
melewati pass parameter self default.
"""

class Employee:
    def employeeDetails(self):
        self.name = "Niken"

    @staticmethod
    def welcomeMessage():
        print("Welcome to our organization!")

employee = Employee()
employee.employeeDetails()
print(employee.name)
employee.welcomeMessage()