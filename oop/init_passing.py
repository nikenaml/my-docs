class Employee:
    def __init__(self,name):
        # jika ingin memanggil di parameter harus passing dahulu di parameter init
        self.name = name
        # agar dapat menetapkan atribut instance dengan parameter yang dimasukkan
        # refers to atribut name yang diberikan di parameter/tanda kurung atas

    def displayEmployeeDetails(self):
        print(self.name)

employee = Employee("Niken")
employeeTwo = Employee("Ival")
employee.displayEmployeeDetails()
employeeTwo.displayEmployeeDetails()