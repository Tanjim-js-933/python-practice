# Hello Test! 123 123, good
user_ask = input("Please enter your string: ")   
capital = "" 
small = ""
digit = ""
all = ''
for i in user_ask:                                                                                                                                                                            
    
    if i.isupper():
        capital = capital + i
    elif i.islower():
        small = small + i
    elif i.isdigit():
        digit = digit + i
    else:
        all = all + i
print(capital)
print(small)
print(digit)
print(all)