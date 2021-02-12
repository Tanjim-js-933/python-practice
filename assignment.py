def oddeven(n1):
    if n1 % 2 == 0:
        return'this is an even number'
    else:
        return'this is an odd number'
    
while True:
    user = input();    
    user1 = int(user)
    call = oddeven(user1)
    print(call)
