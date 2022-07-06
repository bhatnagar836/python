def warn_the_sheep(queue):
    index_b = queue.index('wolf')
    b_index = len(queue)-index_b
    N = b_index-1
    if b_index != 1:
        print(f"Oi! Sheep number {N}! You are about to be eaten by a wolf!")
        return f"Oi! Sheep number {N}! You are about to be eaten by a wolf!"
    else:
        print("Pls go away and stop eating my sheep")
        return "Pls go away and stop eating my sheep"

# def warn_the_sheep(queue):
#     n = len(queue) - queue.index('wolf') - 1
#     return f'Oi! Sheep number {n}! You are about to be eaten by a wolf!' if n else 'Pls go away and stop eating my sheep'


warn_the_sheep(['sheep', 'sheep', 'sheep', 'wolf', 'sheep', 'sheep', 'sheep', 'sheep'])
warn_the_sheep(['sheep', 'sheep', 'wolf'])