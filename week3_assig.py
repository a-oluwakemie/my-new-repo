'''
Create functions to calculate the following statistical measures:
1. Mean
2. Median
3. Variance
4. Standard Deviation
5. Skewness

'''


############# FUNCTION FOR 'MEAN'##############




def myMean(numberList):
    if len(numberList) == 0:
        print("\nYou have entered no item or elemnt in your list...")
        return "EMPTY LIST! \n"
    else :
       print('\nThe list of numbers:',numberList) 
       
       meanValue = sum(numberList) / len(numberList)
       return meanValue

print('The "MEAN" is',myMean([3,4,5,6]))




##############FUNCTION FOR 'MEDIAN'##############



def myMedian(numberList):
    if len(numberList) == 0:
        print("\nYou have entered no item or elemnt in your list...")
        return "EMPTY LIST! \n"
    elif len(numberList) > 1:
            sorted_numberList = sorted(numberList)
    if len(sorted_numberList) % 2 != 0:

         odd_median = int( (len(sorted_numberList)+1)/2 -1)

         print(f'\nThis is  list: {numberList}')
         print(f'\nThis is the sorted list: {sorted_numberList}')
         print(f"The median is at 'index[{odd_median}]'. The 'MEDIAN' is:")

         return sorted_numberList[odd_median]

    elif len(sorted_numberList)% 2 == 0:

        even_number1 = int(len(sorted_numberList)/2 -1)
        even_number2 = int(len(sorted_numberList)/2 ) 
        even_median = even_number1+even_number2/2 -1

        print(f'\nThis is  list: {numberList}')
        print(f'\nThis is the sorted list: {sorted_numberList}\n')
        print(f"The two middle numbers are at 'index[{even_number1}]' and 'index[{even_number2}]' , the even median is point is at the middle whic is'index[{even_median}]'")

        return (sorted_numberList[even_number1]+sorted_numberList[even_number2])/2
    else:
        pass
   
print(" The 'MEDIAN' is: ",myMedian([1,10,2,11,7,4]))


########### FUNCTION FOR 'VARIANCE'#############

# 1... CALCULATING SAMPLE VARIANCE

def myVariance(listVariance):
    average = myMean(listVariance)

    return sum([(x - average)**2 for x in listVariance])/ (len(listVariance)-1)

print("Using sample variance formumla, The 'THE SAMPLE VARIANCE' is:", myVariance([4, 8, 6, 5, 3, 2, 8, 9, 2, 5]))

# 2. CALCULATING  POPULATION VARIANCE 

def myVariance_two(listVariance_two):
    average = myMean(listVariance_two)

    return sum([(x - average)**2 for x in listVariance_two])/ len(listVariance_two)

print("Using population variance formula The 'THE POPULATION VARIANCE' is:", myVariance_two([4, 8, 6, 5, 3, 2, 8, 9, 2, 5]))




########### FUNCTION FOR 'STANDARD DEVIATION'#############


# 1.......FUNCTION FOR 'STANDARD DEVIATION' using SAMPLE  Variance
def myStandard(listStandardD):
    the_vaariance = myVariance(listStandardD)
   
    return the_vaariance**0.5
print("Using sample variance formumla The of the above list 'STANDARD DEVIATION' is:", myStandard([4, 8, 6, 5, 3, 2, 8, 9, 2, 5]))


# 2..........FUNCTION FOR 'STANDARD DEVIATION' using POPULATION  Variance
def myStandard_two(listStandardD_two):
    the_variance = myVariance_two(listStandardD_two)
   
    return the_variance**0.5
print("Using population variance formumla,The of the above list 'STANDARD DEVIATION'  is:", myStandard_two([4, 8, 6, 5, 3, 2, 8, 9, 2, 5]))



########### FUNCTION FOR 'SkEWNESS'#############

#1.......... FUNCTION FOR 'SKEWNESS' using SAMPLE  Variance formular

def mySkewness(listSkewness):
    the_average = sum(listSkewness)/len(listSkewness)
    the_standard_deviation = myVariance(listSkewness)

    return sum([(x - the_average)**3 for x in listSkewness])/ ((len(listSkewness)-1) * the_standard_deviation**3)
    
print("Using sample variance formumla,The of the above list 'SKEWNESS'is:",mySkewness([4, 8, 6, 5, 3, 2, 2, 5]))



#2.......... FUNCTION FOR 'SKEWNESS' using POPULATION  Variance formular

def mySkewness(listSkewness):
    the_average = sum(listSkewness)/len(listSkewness)
    the_standard_deviation = myVariance_two(listSkewness)

    return sum([(x - the_average)**3 for x in listSkewness])/ ((len(listSkewness)) * the_standard_deviation**3)
    
print("Using population variance formumla,The of the above list 'SKEWNESS' is:",mySkewness([4, 8, 6, 5, 3, 2, 2, 5]))


