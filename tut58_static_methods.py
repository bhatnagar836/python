"""
When we don't want either instance variable nor class variable
Then we use static methods - are made by using decorators
Then why are we putting it inside a class - because we want to run this method only on our objects (instances)
"""

class Employee:
    number_of_leaves = 11

    def __init__(self, name_is, salary_is, role_is):
        self.name = name_is
        self.salary = salary_is
        self.role = role_is

    @staticmethod
    def print_good(food):
        print(f"This is so good! You should try {food} here!")
        return "Yummy!!"


Pooja = Employee("Pooja","30,00,000", "Python Developer")

# print(Pooja.print_good("Veggies salad")) #will output "None" if print_good() returns nothing
Pooja.print_good("this burger")

