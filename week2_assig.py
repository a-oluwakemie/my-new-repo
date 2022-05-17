

# user_interger= int(input("enter any positive whole number of your choice\n:>"))

# if user_interger > 1:
#     for x in range(2, user_interger):
#         a = user_interger % x
#         if (a) == 0:
#             print(f"\n Your number: '{user_interger}' \n is NOT a prime number, TRY AGAIN! \n")
#             break
#     else:
#         print(f"\nYour number:'{user_interger}' \nis a prime number! \n"  )
       
# else:
#     print("\nPlease enter number geater than one(1)\n")

# def is_prime(n:int):
#     if n > 1:
#         for x in range(2, n):
#             a= n % x
#             if (a) == 0:
#                 return False
#             else:
#                 return True
#     else:
#         print("enter a value greater than one")
# user_input= int(input("enter user numbe:>"))
# print(is_prime(user_input))


# def is_prime(n):

#     if n > 1:
#         for i in range(2,int(n/2)):
#             if (n%i) == 0:
#                 return False
#         return True
#     else:
#         print("\nPlease enter number geater than one(1)\n")
# number= int(input('enter user number:> '))
# print(is_prime(number))


def is_prime(n:int):
    if n < 2:
        return False
    for i in range(2, n):
        if (n%i) == 0:
            return False
    return True
    
number= int(input('Check if a given number is a prime number... \nNote!\n If it is a Prime number it gives a "TRUE" output\n But if it is a not a prime number it gives "FALSE" output... \nPlease enter any "WHOLE POSITIVE NUMBER" of youR choice below... \n:>>> '))
print(is_prime(number))


# def test_prime(n):
#     if (n==1):
#         return False
#     elif (n==2):
#        return True
#     else:
#         for x in range(2,n):
#             if(n % x==0):
# 	                return False
       
# def prime_test(n):
#     if (n==2):
#         return True;
#     elif n > 1:
#         for x in range(2, n):
#             n_modulus = n % x
#             if (n_modulus) == 0:
#                 return False  
           
#             else:
#                  return True 
#     else:
#         print("\nPlease enter number geater than one(1)\n")

       
# user_interger= int(input("\n Please enter any positive whole number of your choice\n:>"))
# print(prime_test(user_interger))