# Write a program that takes 3 numbers from the user and computes the average

# first_number = float(input("Enter your first number:\n"))
# second_number = float(input("Enter your second numbe:\n"))
# third_number = float(input("Enter your third number: \n"))
# a =[first_number, second_number, third_number]
# length_of_numbers = len(a)
# sum_of_numbers = a[0]+a[1]+a[2]
# average = sum_of_numbers / length_of_numbers
# print(f"""

#     the average of {first_number}, {second_number}, {third_number}
#     is calculated as:

#       average = "{average}"
# """)


# 2.Write a program that takes a sentence from the user and changes the first word to upper case.


# solution one

# user_sentence = input("Enter a sentence of your choice bellow: \n >").lower()
# user_sentence_split = user_sentence.split(" ", 1)
# first_word = user_sentence_split[0].upper()
# new_user_sentence = first_word + " " +user_sentence_split[1]
# print(first_word)
# print(new_user_sentence)
# print (f"""
#     the first word of the sentence is "{first_word}"

#     Your new sentence is : "{new_user_sentence}"
# """)

# solution2
sentence = input("enter any sentence of your choice:> ").lower().split()
sentence[0] = sentence[0].upper() 
print (f'solution:/n {" ".join(sentence)}')




#3. Write a program with the sentence "I am learning python". When your program is run, the string "I" should be changed to "you"

# i_sentence =  "I am learning programing"
# you_sentence = i_sentence.replace("I", "You")
# print(f""" 
# {you_sentence}
# """)




#4. Write a program that takes the string "I hope you had fun today in class". Print the number of times that the string "a" appears in the sentence.

# random_sentence =  "I hope you had fun today in class"
# count_number_of_a_in_random_sentence = random_sentence.count("a")
# print(f"""

# The letter 'a' appears in the sentence {count_number_of_a_in_random_sentence} times!

# """)
