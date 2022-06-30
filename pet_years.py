def human_years_cat_years_dog_years(human_years):
    if human_years == 1:
        print([1, 15, 15])
        return [1, 15, 15]
    elif human_years == 2:
        print([2, 24, 24])
        return [2, 24, 24]
    elif human_years >= 3:
        cat_years = 24 + (human_years - 2)*4
        dog_years = 24 + (human_years - 2)*5
        print([human_years, cat_years, dog_years])
        return [human_years, cat_years, dog_years]


human_years_cat_years_dog_years(1)
human_years_cat_years_dog_years(2)
human_years_cat_years_dog_years(10)
