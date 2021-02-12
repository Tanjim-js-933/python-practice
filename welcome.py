result = 0
for num in range(101):
    print(num)
    if num % 5 == 0:
      print(num)
      result += num
print("sum is:", result) 