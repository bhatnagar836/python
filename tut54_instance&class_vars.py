"""
Convention - starting class with capital letter is a good practice
The difference between the instances' variables and classes' variables is :
The variable of the instance will be the property of that particular instance only
Whereas, the variable of the class will be the shared variable among all the instances of that class
"""


class Employee:
    number_of_leaves = 11
    # The Class variable is inherited by both Pooja and Aditi (all the instances of the class)
    pass


Pooja = Employee()
Pooja.name = "Pooja"
Pooja.role = "Python Developer"
Pooja.salary = 30,00,000

Aditi = Employee()
Aditi.name = "Aditi"
Aditi.role = "TGT Teacher"
Aditi.salary = 25,00,000


print(Pooja.salary)

# All the following will give output as 11
print(Pooja.number_of_leaves)
print(Aditi.number_of_leaves)
print(Employee.number_of_leaves)
Employee.number_of_leaves = 21
print(Employee.number_of_leaves)
print(Employee.__dict__)


# If we want to edit class variable then we have to access it as class variable only
# If we try to edit class variable via using instance, then it will create a new variable of that instance instead of accessing class(shared) variable

print(Aditi.__dict__)
Aditi.number_of_leaves = 7  # this will not edit the class variable, it will create new instance variable of Aditi as shown below
print(Aditi.__dict__)






