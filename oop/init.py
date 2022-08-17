"""
init method adalah method special/method pertama yang dipanggil pada saat pembuatan objek
"""
class Employee:
    def __init__(self):
        self.name = "Niken"

    # def enterEmployeeDetails(self):
    #     self.name = "Niken"

    def displayEmployeeDetails(self):
        print(self.name)

employee = Employee() # saat buat object ini secara default ini akan dipanggil
"""
method init adalah method pertama yang dipanggil dan yang menginisialisasi atribut instance
yang disebut nama yang sedang di inisialisasi ke "Niken". Oleh karena itu,
pastikan inisialisasi semua atribut ke dalam method init agar object sepenuhnya
diinisialisasi, dan menghindari error. 
"""

employee.displayEmployeeDetails() 
""" jika tidak ada function ini, proses ini tidak dapat dijalankan
karena method ini memanggil self.name yang belum pernah dipanggil sebelumnya
karena (method enterEmployeeDetails) tidak di panggil sebelum menjalankan displayEmployeeDetails()
oleh karena itu menggunakan init agar bisa di panggil secara langsung tanpa panggil method sebelumnya 
yang memiliki value
"""