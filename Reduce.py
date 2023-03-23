from functools import reduce

numbers = [1,2,3,4]
def sum(a,b):
    return a+b

#call sum() function on each element
total = reduce(sum,numbers)
print(total)


