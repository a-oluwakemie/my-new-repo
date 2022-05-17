# strings doc strings and normal strings 
# string1 = "This is a string"
# string2 = " i love this string"
# string3 = "984"
# string4 = 12334
# print(string1 + " " + string2)
# print(string1, string2)
# print(string1[8])
# print(string1[-1])
# print(string3[-1])
# print(string4[-1])
# string slicing [start:stop:step] note the stop index does not take the count in the returning answer
# print(string1[3:10])
# print(string1[1:-1:2])

# STRING FORMATING Formating
# name =""
# my_name = "vera"
# my_new_name = input("Enter your name: ")
# print("my name is {name}")
# print(f"my name is {my_name}")
# print(f""" Welcome, {my_new_name}.

# You have signed up succefully.

# Cheers,
# Newlife Team.

# """)


# my_firstname= input("Enter your firstname: ")
# my_lastname= input("Enter your lastname: ")
# first_username = my_firstname[-2:]
# last_username = my_lastname[0:3]
# print(first_username)
# print(last_username)

# print(f""" Welcome, {my_firstname}{my_lastname}.

# your username is "{first_username}{last_username}"

#  You have signed up succefully.

#  Cheers,
#  Newlife Team.""")


# dog_name= input("Enter your 'dog's name' : ")
# dog_birthmonth= input("Enter your 'dog's birth' : ")
# vet_password = dog_name[:3]+ dog_birthmonth[-2:]

# print(f""" Welcome, {dog_name} born in {dog_birthmonth}.

# your vet username is "{vet_password}"

#  Cheers,
# cheekyvets Team.""")

# name = input("Enter your: \n::>>")
# month_star = input("Enter your month and star: \n::>>")
# print(name.capitalize())
# print(name.title())
# print(name.upper())
# print(month_star.split(" "))
# print(month_star.split(","))
# a = name.split()
# print(a[0])
# print(a[1])
daddy = ["alani" , "iskilu"]
print(" ".join(daddy).title())
print("".join(daddy).upper())


# sequence_word = " You are either born a boy or a girl there is no such thing as binary non binary"
# user_word = input("Enter a word to search for in the following sequence of word : \n \"You are either born a boy or a girl there is no such thing as binary non binary.\" \n your word search::>")
# new_sequence_word = sequence_word.lower()
# new_user_word = user_word.lower()
# no_of_inputed_word = new_sequence_word.count(new_user_word)
# highlited_sequence_word = new_sequence_word.replace(new_user_word,new_user_word.upper())
# print(f""" {no_of_inputed_word} result of your word search is found.
     
#      your result is :
#      " {highlited_sequence_word}"

# """)

