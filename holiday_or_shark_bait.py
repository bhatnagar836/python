def shark(pontoon_distance, shark_distance, you_speed, shark_speed, dolphin):
    my_time = pontoon_distance / you_speed
    shark_time = shark_distance / shark_speed
    if dolphin:
        shark_time = 2 * shark_time
    if my_time < shark_time:
        print("Alive!")
        return "Alive!"
    else:
        print("Shark Bait!")
        return "Shark Bait!"


shark(12, 50, 4, 8, True)
shark(7, 55, 4, 16, True)
shark(24, 0, 4, 8, True)
