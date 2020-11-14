for a in range(0, 1000):
    if a%10 in [2, 3, 4] and a%100 not in [12, 13, 14] :
    
        print(a, "программиста")
    
    elif a %10 == 1 and a%100 !=11:
    
        print(a, "программист")
    
    else:
        print(a, "программистов")