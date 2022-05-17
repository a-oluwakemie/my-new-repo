'''list is a collect data enclosed in square brackets seperated by commas.....
    mutable, every element in a list are indexed organised and can have dupicalte..
'''


''' 
b = [6,7,8,9,10]
b[3] =82
print(b)


a=[1,2,3,4,5,6,7]
print(a[2:5])
for elements in a:
    print(elements)
'''


# LIST EXPRESSION
# list_expression =[x**2 for x in range(10)]
# print(list_expression)

# mim = 0.728
# number_range= [1,2,3,4,5,6,7,8,9,10]
# person = [(x-mim)**2 for x in number_range]
# person_sum = sum(person)
# print(person_sum)


# odd_num_becomes_zero =[x if x%2==0 else 0 for x in range(10)]
# print(odd_num_becomes_zero)


def is_prime(n:int):
    if n < 2:
        return False
    for i in range(2, n):
        if (n%i) == 0:
            return False
    return True

my_prime= [a for a in range(98,176) if is_prime(a) ]
print(my_prime)

