def zero_fuel(distance_to_pump, mpg, fuel_left):
    print("You will make it") if distance_to_pump <= mpg * fuel_left else print("Not enough fuel to reach petrol pump!")
    return 1 if distance_to_pump <= mpg * fuel_left else 0


zero_fuel(50, 25, 2)
zero_fuel(100, 50, 1)