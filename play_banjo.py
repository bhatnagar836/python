def are_you_playing_banjo(name):
    # print("Are you playing banjo?")
    print(name + " plays banjo") if name.startswith('R') or name.startswith('r') else print(name + " does not play "
                                                                                                   "banjo")
    return name + " plays banjo" if name.startswith('R') or name.startswith('r') else name + " does not play banjo"


are_you_playing_banjo("martin")
# martin does not play banjo"
are_you_playing_banjo("Rikke")
# "Rikke plays banjo"
are_you_playing_banjo("bravo")
# "bravo does not play banjo"
are_you_playing_banjo("rolf")
# "rolf plays banjo"