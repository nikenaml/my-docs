class Employee:
    # bagian ini termasuk instance method
    def employeeDetails(self):
        self.name = "Niken"
        print("Name = ", self.name)
        age = 21
        print("Age = ",age)

    def printEmployeeDetails(self):
        print("Printing in another method")
        print("Name: ", self.name)
        # print("Age: ",age)

employee = Employee()
employee.employeeDetails() #opsi cara pemanggilan 1, cara umum
Employee.employeeDetails(employee) #opsi cara pemanggilan 2, internal python memanggil fungsi

"""
gunanya self agar bisa dipanggil di semua method yang dibuat, 
kalau gada self, atribut tersebut hanya bisa di akses pada method itu sendiri,
method lain tidak bisa akses (atau jika dijalankan akan error).
"""

employee.printEmployeeDetails()