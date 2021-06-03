def list_add(list):
    sum = 0
    for i in list:
        sum += i
    return sum

list = [1,2,6,4,5]
n1 = list_add(list)
print(n1)