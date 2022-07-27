def split(word):
    return [char for char in word]


def DNA_strand(dna):
    i = 0
    dna = split(dna)
    while i < len(dna):
        if dna[i] == 'A':
            dna[i] = 'T'
        elif dna[i] == 'T':
            dna[i] = 'A'
        elif dna[i] == 'G':
            dna[i] = 'C'
        elif dna[i] == 'C':
            dna[i] = 'G'
        i += 1
    # print("".join(dna))
    return "".join(dna)


# def DNA_strand(dna):
#     reference = { "A": "T",
#                   "T": "A",
#                   "C": "G",
#                   "G": "C"
#                   }
#     return "".join([reference[x] for x in dna])


DNA_strand("ATTGC")