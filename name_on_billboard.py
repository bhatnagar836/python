def billboard(name, price=30):
    amount = 0
    for i in range(len(name)):
        amount = amount + price

    print(amount)
    return amount


# def billboard(name, price=30):
#     return sum(price for letter in name)


billboard("Jeong-Ho Aristotelis")