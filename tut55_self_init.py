
# Constructor is a way to give arguments to the employee
# For making instructor, we have to make init

class Employee:
    number_of_leaves = 11
    # The Class variable is inherited by both Pooja and Aditi

    def __init__(self, name_is, salary_is, role_is):
        self.name = name_is
        self.salary = salary_is
        self.role = role_is

    def printdetails(self):
        return f"{self.name} is a {self.role} earning {self.salary} yearly"
    pass


# Pooja = Employee()
# Pooja.name = "Pooja"
# Pooja.role = "Python Developer"
# Pooja.salary = "30,00,000"

# After making constructor, above can be written as follows :
Pooja = Employee("Pooja","30,00,000", "Python Developer")


print(Pooja.printdetails())
