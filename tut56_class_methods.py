
"""
We want to change number of leaves, not by directly accessing class variable but via a function
For this, we will use class method (using class method decorator)
"""

class Employee:
    number_of_leaves = 11

    def __init__(self, name_is, salary_is, role_is):
        self.name = name_is
        self.salary = salary_is
        self.role = role_is

    def printdetails(self):
        return f"{self.name} is a {self.role} earning {self.salary} yearly"
    pass

    @classmethod
    def change_leaves(cls, new_leaves): #cls is that class(i.e. Employee), whose instance is the object(i.e. Pooja) on which we will run the function
        cls.number_of_leaves = new_leaves #i.e. Employee.number_of_leaves = new_leaves(i.e the argument passed with the class or the instance of that class)


"""
When it comes to instance, it will first check for instance variable and in case of not found,
it will check for class variable 
"""

# Changing varibale value via instance using class method
Pooja = Employee("Pooja","30,00,000", "Python Developer")
Pooja.change_leaves(51) #here after changing the number of leaves via class method, even the variable value, of the class, has been updated
print(Employee.number_of_leaves)
