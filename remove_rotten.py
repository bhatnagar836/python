def remove_rotten(bag_of_fruits):
    new_list = []
    for fruits in bag_of_fruits:
        if "rotten" in fruits:
            fruits = fruits[6:len(fruits)].lower()
            new_list.append(fruits)
        elif fruits in bag_of_fruits:
            new_list.append(fruits)
        else:
            pass
    print(new_list)
    return new_list


remove_rotten(["rottenApple", "rottenBanana", "rottenApple", "rottenPineapple", "rottenKiwi"])

