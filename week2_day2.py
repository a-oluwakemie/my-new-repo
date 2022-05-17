""" 
########FUNCTIONS AND ITS ATTRIBUTES########

SYNTAX OF A FUNCTION WITH PARAMETERS: def function_name(par1, par_2..... par_n):
SYNTAX OF A FUNCTION WITHOUT PARAMETERS: def function_name():

PARAMETERS :these are used when declaring a function


ARGUMENTS : these are used when calling a function. we have three types of arguements
i. postional 
funct3(10,20,40)
ii.keyword argument
funct3(a=20, b=40, c=40 )
iii. a mixture of postional and keyword arguement
func3(1, b=20, c=40)
note: when mixing postional argument and keyword argument your positional argument should always come first
iv.


"""

# def test_function():
#     print(4*2+2)
# call a function
# test_function()

# def funct2(n:int):
#     print(n**2)
# funct2(10)

# def funct3(a,b,c):
#     print(a+b+c)
# funct3(10, 20, 30)
# funct3(a=20, b=40, c=10 )
# funct3(10, b=20, c=40)




# def func_global(n:int):
#     global result
#     result = n**2
#     return result
# print (func_global(4))
# print(result)

# ##########global variable#############
# new_result= 4
# def func_test(n:int):
#     return new_result*n
# print (func_test(4))
# print(new_result)

# ########### global keyword #################

# def return_statement_sample(n:int):
#     print("i am running")
#     return n**2
#     print("they dance")
# return_statement_sample(3)
# print(return_statement_sample(3))

# def f_mean(numbers):
    
#     sum_of_numbers = sum(numbers)
#     length_of_arr = len(numbers)
# print(f_mean)
    



# def one_mean(numbers):
#     mean = sum(numbers)/ len(numbers)
#     return mean
# print(f' your mean is one_mean([0,3,8,91])')



# first_number = float(input("Enter your first number:\n"))

user_input = input("enter your numbers seperated by comma\n :>").split(",")
mapped = list(map(int, user_input))

def rounded_mean(array_numbers):
    rounded_mean = sum(array_numbers)/ len(array_numbers)
    return  round(rounded_mean, 2)
    
# user_input = input("enter your numbers seperated by comma\n :>").split(",")
# mapped = list(map(int, user_input))
print(rounded_mean(mapped))
