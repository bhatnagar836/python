def people_with_age_drink(age):
    if 1 <= age < 14:
        return "drink toddy"
    elif 14 <= age < 18:
        return "drink coke"
    elif 18 <= age < 21:
        return "drink beer"
    else:
        return "drink whisky"


# def people_with_age_drink(age):
    # return 'drink ' + ('toddy' if age < 14 else 'coke' if age < 18 else 'beer' if age < 21 else 'whisky')