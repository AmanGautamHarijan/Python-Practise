sum = lambda a , b : a + b
print(sum(1,2))

mul = lambda a , b : a*b
print(mul(2,4))

numbers = [1,2,3,4,5]
squared_numbers = map(lambda num : num * num,numbers)
print(list(squared_numbers))


odd_nums = filter(lambda num: num % 2 != 0, numbers)

print(list(odd_nums))