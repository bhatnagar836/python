def count_vegetables(string):
    new_tuple = ()
    veggies_count = []
    veggies = ["cabbage", "carrot", "celery", "cucumber", "mushroom", "onion", "pepper", "potato", "tofu", "turnip"]
    x = string.split()
    # print(x)
    for item in x:
        if item in veggies:
            new_tuple = (x.count(item), item)
            veggies_count.append(new_tuple)
        else:
            pass
    sorted_veggies = set(sorted(veggies_count))
    new_list = list(sorted_veggies)
    new_list.sort(reverse=True)
    print(new_list)
    return new_list
    # print(veggies_count)


count_vegetables("potato tofu cucumber cabbage turnip pepper onion carrot celery mushroom potato tofu cucumber cabbage'")