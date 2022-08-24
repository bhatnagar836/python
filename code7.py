def break_chocolate(n, m):
    if n == 0 or m == 0:
        return 0
    elif n == 1:
        return m-1
    elif m == 1:
        return n-1
    else:
        return (n-1)*m+(m-1)
        
        
break_chocolate(5, 5)
#24
break_chocolate(7, 4)
#27
break_chocolate(1, 1)
#0
break_chocolate(0, 0)
#0
break_chocolate(6, 1)
#5
