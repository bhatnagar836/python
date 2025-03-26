"""
Class - It is a template
Example : withdrawing money form - it has certain things already filled like date and then space provided to fill it,
Name of the withdrawer and the amount to be withdrawn - that we have to fill
So the form is a class

Object - Instance of that class
Example : when we fill the details for person A, it is instance1 and when we fill the details for person B, that particular form will be instance2

OOPS works on the concept of DRY
DRY - Do not repeat yourself
We can also restrict the class for a particular type of customer like only the withdrawer who is withdrawing cash above Rs. 1500 will be able
to use the form and other withdrawers
"""

class Successful():
    pass


Pooja = Successful()
Aditi = Successful()
Ritu = Successful()
# All the above 3 are different instances of class Successful, present at different memory location as shown below
print(Pooja, Aditi, Ritu)

# We can make instance variables of each of them or any of them
Pooja.name = "Pooja"
Pooja.dob = "21st Nov"

Aditi.subjects = ["Social Science", "English"]
print(Pooja.name)
print(Aditi.subjects)
