#Dictionary is just key value pairs
# Following is a blank dictionary
d1={}
# print(type(d1))

d2={"Pooja":"Pizza","Aditi":"Taco",
    "Ritu":"Chaap", "Sonali":{"Breakfast":"Paneer","Lunch":"Kadi-rice","Dinner":"Salad"}}
# print(d2)
# print(d2["Pooja"])
# print(d2["Sonali"])
# print(d2["Sonali"]["Breakfast"])

# Adding key-value pair to dictionary
# d2["Deeksha"]="Dal Bhaat"
# d2[21]="Veg Kababs"
# print(d2)
# del d2[21]
# print(d2)
# UPDATE
# d2.update({"Dimpi":"Oats"})
# print(d2)

# Dictionary values can be a dictionary, list or tuple
d3={"Pooja":"Chilli-potato","Srishti":"Fried-rice",
    "Deeksha":"Chowmein", "Jahnvi":["Samosa","Manchurian","Fruits"]}
# print(d3["Jahnvi"])


# COPY AND ASSIGNMENT
# print(d2.copy())
# d4=d2.copy()
# del d4["Pooja"]
# print(d2)
# d3=d2
# print(d3)
# del d3["Pooja"]
# print(d2)


# GET
print(d2.get("Aditi"))


# KEYS
print(d2.keys())
# ITEMS
print(d2.items())



