# kata7
def redistribute_wealth(wealth):
    num_of_citizens = len(wealth)
    equal_amount = (sum(wealth) / num_of_citizens)
    for citizens in range(0, num_of_citizens):
        wealth[citizens] = equal_amount
    print(wealth)


redistribute_wealth([5, 10, 6])