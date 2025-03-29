class Employee:
    number_of_leaves = 11

    def __init__(self, name_is, salary_is, role_is):
        self.name = name_is
        self.salary = salary_is
        self.role = role_is

    def printdetails(self):
        return f"{self.name} is a {self.role} earning {self.salary} yearly"

    @classmethod
    def from_dash(cls, string):
        # params = string.split("-")
        # return cls(params[0], params[1], params[2])
        return cls(*string.split("-"))


# Pooja = Employee("Pooja","30,00,000", "Python Developer")
Pooja = Employee.from_dash("Pooja-30,00,000-Python Developer")
print(Pooja.salary)
print(Pooja.printdetails())


"""
Abstraction - Cheezo ko tukdo mein todna
Encapsulation - Capsule mein cheezo ko band krdena, wo kaise kaam krta, capsule mein kya hai usse humein mtlb ni hai 
i.e. (hinding implementation details)
"""
