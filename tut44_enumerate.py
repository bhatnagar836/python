list1 = ["Blessings", "Talents", "God", "Heart"]

# Print item on odd indexes
"""
i = 1
for item in list1:
    if i%2 != 0:
        print(item)
    i += 1

"""
for index, item in enumerate(list1):
    if index%2 == 0:
        print(item)