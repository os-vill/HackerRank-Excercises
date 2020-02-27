
listA=list(range(1,11))
primes=[a for a in listA if a%2 != 0]

### S I M P L E  A R R A Y  S U M ###

data=(len(listA), listA)

def simpleArraySum(data):
    return(sum(i for i in data[1]))

#print(simpleArraySum(data))

# SIMPLE ARRAY SUM solved with simpleArraySum()
"""simpleArraySum is a function that takes input(data)
as an argument and returns the sum of item for item in data[1]"""

### C O M P A R E  T H E  T R I P L E T S ###

def compareTriplets(a, b):
    alice=0
    bob=0
    for i in range(len(a)):
        if a[i]>b[i]:
            alice+=1
        elif a[i]<b[i]:
            bob+=1
        else:
            pass
    return alice, bob

#print(compareTriplets([5,6,7],[3,6,10]))

# COMPARE THE TRIPLETS solved with compareTriplets(a,b)
"""compareTriplets is a function that takes two equal length lists
as arguments. It iterates over the range(len()) of one of the lists
to get indexes to play with. The it compares a[i] > b[i] and viceversa
to get a score. Score count for each argument is added to its corresponding
parameter."""

### A  V E R Y  B I G  S U M ###

def aVeryBigSum(x, y):
    return sum(i for i in y)

#print(aVeryBigSum(5,[1000000001, 1000000002, 1000000003, 1000000004, 1000000005]))

# A VERY BIG SUM solved with aVeryBigSum() #
"""Make sure to double check the difference between this function
and the first one. It seems like the resulting function is the same as
SIMPLE ARRAY SUM. Passed HackerRank: Apparently is a repeated exercise
where the question is formulated differently."""

### D I A G O N A L  D I F F E R E N C E ###

arr=[1,2,3],[4,5,6],[9,8,9]

def diagonalDifference(arr):
    valueOne=0
    valueTwo=0
    for i in range(len(arr)):
        valueOne+=arr[i][i]
        arr[i].reverse()
        valueTwo+=arr[i][i]
    return abs(valueOne-valueTwo)

#print(diagonalDifference(arr))

# Diagonal Difference solved with diagonalDifference(arr) #
"""diagonalDifference is a function that takes one matrix array
as an argument and returns the absolute value of the difference
between the sum of its right and left diagonals. It iterates over
the range(len()) of the array like so: range(len(arr)) and for
every item (precisely range number, like a count) if it is 1,
it'll += the arr[i][i] number to a valueOne instance, then reverse
the arr[i] and += every arr[i][i] to a valueTwo instance, then
substract difference and return its absolute value."""

### P L U S  M I N U S ###

def plusMinus(array):
    count=[0,0,0]
    for i in array:
        if i > 0:
            count[0]+=1
        elif 0 > i:
            count[1]+=1
        elif i == 0:
            count[2]+=1
    print(count[0]/len(array))
    print(count[1]/len(array))
    print(count[2]/len(array))


#print(plusMinus([-4, 3, -9, 0, 4, 1]))

### S T A I R C A S E ###

def stairCase(n):
    for i in range(1,n+1):
        print(('#'*i).rjust(n))
    return ' '

print(stairCase(10))

# B I R T H D A Y  C A K E  C A N D L E S #

print('hi else')

# M I N  M A X  S U M #

