import statistics
print('Lenght of a string', len('Benedict'))
print('Suming items in a collection', sum([10, 20, 30]))
# To get an average function, You have to import Statistics
print('Getting the average of items in a collection', statistics.mean([10, 20, 30]))
print('Minimum number in a collection', min([10, 20, 30]))
print('Maximum number in a collection', max([10, 20, 30]))

#Filter takes two arguments in it's parameter (function, iteratable) it returns an iteratable

def get_even_numbers(numbers):
    if numbers % 2 == 0:
        return True
    else:
        return False

even_numbers1 = list(filter(get_even_numbers, range(10)))
print(even_numbers1)

list_numbers = [5, 10, 15, 20, 25, 30, 35, 40]
even_numbers2 = list(filter(get_even_numbers, list_numbers))
for e in even_numbers2:
    print(e)

# Lambda Function to get Even Numbers
list_numbers = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60]
even_numbers3 = list(filter(lambda n: True if(n % 2 == 0) else False, list_numbers))
print(even_numbers3)

# Lambda Function to get Greater number and Lesser Number
list_numbers = [5, 10, 15, 20, 25, 30, 35, 40]
get_numbers = list(filter(lambda n: True if(n > 10 and n < 40) else False, list_numbers))
print(get_numbers)

# Map 

# adding numbers to itself
def double_numbers(n):
    n += n
    return n

double = list(map(double_numbers, range(10)))
print(double)

# raise to power 
def exponent_numbers(n):
    n**=3
    return n
exponent = list(map(exponent_numbers, range(20)))
print(exponent)

# lambda raise to power
exponent2 = list(map(lambda n: n**2, range(20)))
print(exponent2)







