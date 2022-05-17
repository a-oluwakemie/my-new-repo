# def print_lyrics():
#     print("I'm a lumberjack, and I'm okay.")
#     print ("I sleep all night and I work all day.")
# def repeat_lyrics():
#     print_lyrics()
#     print_lyrics()
#     repeat_lyrics()
# print_lyrics()
# def print_twice(bruce):
#     print(bruce)
#     print(bruce)
# michel ="iam mia"
# print_twice(michel )

# def absolute_value(x, y):
#     if x > y:
#      return 1
#     if x < y:
#         return -1
#     if x == y:
#         return 0

# print(absolute_value(23, 23))
# print(absolute_value(10, 20))
# print(absolute_value(27, 2))
# def b(z):
#     prod = a(z, z)
#     print(z, prod) 
#     return prod
# def a(x, y):
#     x = x + 1
#     return x * y
# def c(x, y, z):
#     total = x + y + z
#     square = b(total)**2
#     return square
# x = 1
# y = x + 1
# print(c(x, y+3, x+y)) 






'''
Create functions to calculate the following statistical measures:
1. Mean
2. Median
3. Variance
4. Standard Deviation
5. Skewness

'''

# FUNCTION FOR 'MEAN'

from statistics import variance


def myMean(numberList):
    if len(numberList) == 0:
        print("\nYou have entered no item or elemnt in your list...")
        return "EMPTY LIST! \n"
    else :
       print('\nThe list of numbers:',numberList) 
       
       meanValue = sum(numberList) / len(numberList)
       return meanValue
print("\nThe mean of the above list is:")
print(myMean([12,3,44,55]))




# FUNCTION FOR 'MEDIAN'


''' 
def myMedian(numberList):
    sorted_numberList = sorted(numberList)
    if len(sorted_numberList) % 2 != 0:

         odd_median = int( (len(sorted_numberList)+1)/2 -1)

         print(f'\nThis is the sorted list: {sorted_numberList}')
         print(f"The median is at 'index[{odd_median}]'. The 'MEDIAN' is:")

         return sorted_numberList[odd_median]

    elif len(sorted_numberList)% 2 == 0:

        even_number1 = int(len(sorted_numberList)/2 -1)
        even_number2 = int(len(sorted_numberList)/2 ) 
        even_median = even_number1+even_number2/2 -1

        print(f'\nThis is the sorted list: {sorted_numberList}\n')
        print(f"The two middle numbers are at 'index[{even_number1}]' and 'index[{even_number2}]' , the even median is point is at the middle whic is'index[{even_median}]', the. MEDIAN' is: ")

        return (sorted_numberList[even_number1]+sorted_numberList[even_number2])/2
 '''  


def myMedian(numberList):
    if len(numberList) == 0:
        print("\nYou have entered no item or elemnt in your list...")
        return "EMPTY LIST! \n"
    elif len(numberList) > 1:
            sorted_numberList = sorted(numberList)
    if len(sorted_numberList) % 2 != 0:

         odd_median = int( (len(sorted_numberList)+1)/2 -1)

         print(f'\nThis is the sorted list: {sorted_numberList}')
         print(f"The median is at 'index[{odd_median}]'. The 'MEDIAN' is:")

         return sorted_numberList[odd_median]

    elif len(sorted_numberList)% 2 == 0:

        even_number1 = int(len(sorted_numberList)/2 -1)
        even_number2 = int(len(sorted_numberList)/2 ) 
        even_median = even_number1+even_number2/2 -1

        print(f'\nThis is the sorted list: {sorted_numberList}\n')
        print(f"The two middle numbers are at 'index[{even_number1}]' and 'index[{even_number2}]' , the even median is point is at the middle whic is'index[{even_median}]', the. MEDIAN' is: ")

        return (sorted_numberList[even_number1]+sorted_numberList[even_number2])/2
    else:
        pass
   
print(myMedian([]))


# FUNCTION FOR 'VARIANCE'

# 1.. CALCULATING SIMPLE VARIANCE 


# 2... CALCULATING POPULATION VARIANCE



def myVariance(listVariance):
    average = myMean(listVariance)

    return sum([(x - average)**2 for x in listVariance])/ len(listVariance)
print(F'\nThe of the above list variance is:')    
print(myVariance([4, 8, 6, 5, 3, 2, 8, 9, 2, 5]))


# FUNCTION FOR 'STANDARD DEVIATION'
# def myStandard(listStandardD):
#     the_vaariance = myVariance(listStandardD)
#     print(F'The of the above list standard deviation is:')
#     return the_vaariance**0.5
# print(myStandard([4, 8, 6, 5, 3, 2, 8, 9, 2, 5]))



# FUNCTION FOR 'SKEWNESS'

def mySkewness(listSkewness):
    the_average = myMean(listSkewness)
    the_vaariance = myVariance(listSkewness)
    print(F'The of the above list standard deviation is:')
    return sum([(x - the_average)**3 for x in listSkewness])/ ((len(listSkewness)-1) * the_vaariance**3)
    
print(mySkewness([4, 8, 6, 5, 3, 2, 8, 9, 2, 5]))


'''USING MODULES'''
# import statistics
# def mymean(data):
#     mean = statistics.mean([data])
#     return mean

# def mymedian(data):
#     median =  statistics.median([data])
#     return median
# def myvariance(data):
#     variance = statistics.variance([data])
#     return variance

# print(mymean([4, 8, 6, 5, 3, 2, 8, 9, 2, 5]))

# print(statistics.mean([4, 8, 6, 5, 3, 2, 8, 9, 2, 5]))
# print(statistics.median([4, 8, 6, 5, 3, 2, 8, 9, 2, 5,7]))
# print(statistics.variance([4, 8, 6, 5, 3, 2, 8, 9, 2, 5]))
# print(statistics.stdev([4, 8, 6, 5, 3, 2, 8, 9, 2, 5])

