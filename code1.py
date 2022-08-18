def add_length(str_):
    new_l = []
    x = str_.split()
    print(x)
    for items in x:
        new_l.append(items + " " + str(len(items)))
    return new_l
  
  
  add_length('you will win')
  #["you 3", "will 4", "win 3"]
