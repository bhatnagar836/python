def rake_garden(garden):
    x = garden.split()
    for i in range(len(x)):
        # print(x[i])
        if x[i] != "gravel" and x[i] != "rock":
            x[i] = "gravel"
        else:
            pass
    print(" ".join(x))
    return " ".join(x)


# VALID = {'gravel', 'rock'}
# def rake_garden(garden):
#     return ' '.join(a if a in VALID else 'gravel' for a in garden.split())


rake_garden("slug spider rock gravel gravel gravel gravel gravel")