"""
Inheritance - Class ke saare attributes (code reusability) + some extra attributes
"""

class Employee:
    number_of_leaves = 11

    def __init__(self, name_is, salary_is, role_is):
        self.name = name_is
        self.salary = salary_is
        self.role = role_is

    def printdetails(self):
        return f"Her name is {self.name}. She is a brilliant {self.role} having a salary {self.salary} per year"


# Following class shows single inheritance (inheriting from class Employee)
class Programmer(Employee):
    def __init__(self, name_is,salary_is, role_is, languages_are ):
        self.name = name_is
        self.salary = salary_is
        self.role = role_is
        # Instead of the above 3 lines, we could have use the "super" keyword, for a better way to make the constructor
        self.langugage = languages_are

    def print_prog(self):
        return f"{self.name} is a {self.role} earning {self.salary} yearly using the knowledge of {self.langugage} "


Aditi = Employee("Aditi","25,00,000", "TGT Teacher")
Ritu = Employee("Ritu", "20,00,000", "Data Ananlyst")
Pooja = Programmer("Pooja","35,00,000", "AI Engineer", ["Python", "C", "MySQL"])
print(Pooja.print_prog())
print(Pooja.printdetails()) #Here note that printdetails is being inherited from the Employee class (and is not present in the programmer class)
