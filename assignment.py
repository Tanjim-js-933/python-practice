def odd(a):
    for i in a:
        if not i % 2 == 0:
            print(i)
    
a = [1,  2, 3, 5, 8, 13, 21, 34, 55, 89]
odd(a)