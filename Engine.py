
listA=list(range(1,11))
primes=[a for a in listA if a%2 != 0]

### --1--  S I M P L E  A R R A Y  S U M ###

data=(len(listA), listA)

def simpleArraySum(data):
    return(sum(i for i in data[1]))

#print(simpleArraySum(data))

# SIMPLE ARRAY SUM solved with simpleArraySum()
"""simpleArraySum is a function that takes input(data)
as an argument and returns the sum of item for item in data[1]"""

### --2--  C O M P A R E  T H E  T R I P L E T S ###

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

### --3--  A  V E R Y  B I G  S U M ###

def aVeryBigSum(x, y):
    return sum(i for i in y)

#print(aVeryBigSum(5,[1000000001, 1000000002, 1000000003, 1000000004, 1000000005]))

# A VERY BIG SUM solved with aVeryBigSum() #
"""Make sure to double check the difference between this function
and the first one. It seems like the resulting function is the same as
SIMPLE ARRAY SUM. Passed HackerRank: Apparently is a repeated exercise
where the question is formulated differently."""

### --4--  D I A G O N A L  D I F F E R E N C E ###

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
the arr[i] and += every arr[i][i] to a valueTwo instance. Finally,
substract difference and return its absolute value."""

### --5--  P L U S  M I N U S ###

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

### --6--  S T A I R C A S E ###

def stairCase(n):
    for i in range(1,n+1):
        print(('#'*i).rjust(n))
    return ''

#print(stairCase(7))

# --7-- B I R T H D A Y  C A K E  C A N D L E S #
"""Note:
        Divide input into one height per unique digit.
        Tallest height is returned."""
#------------------------------------------------------#
import numpy as np
var=np.random.randint((3,3)*3)
#print(list(var*81)) <-------: print right before birthdayCakeCandles() call.
#------------------------------------------------------#
with open('test9.txt') as file:
    line=file.readlines()
    listNines=line[1].split(' ')
    #for i in (listNines[0:5]):
       #print(int(i))
#------------------------------------------------------#
equalDigits=[0,0,0,0]

def birthdayCakeCandles(n, ar):
    ar.sort()
    ar.reverse()
    print(ar)
    for i in range(n-1):
        if ar[i]>ar[i+1]:
            return(i+1)
        else:
            pass
    return n

#print(list(var))
#print(birthdayCakeCandles(len(var),list(var)))
#print(birthdayCakeCandles(len(equalDigits), equalDigits))
#print(birthdayCakeCandles(len(listNines), listNines))


#-----------------------------------#
#-----------------------------------#
#-----------------------------------#
# S U B S T I T U T I O N   T O O L #
#-----------------------------------#
#-----------------------------------#
#-----------------------------------#


#helper function to find elements
def subFunction(testList, repList, start=0):   #<---[first line defines a function that takes three args.----]
    length=len(repList)                        #<---[defines a var called length, set to len(repl_list).-----]
    for i in range(start, len(testList)):      #<---[loop id over range(start, len(test_list).---------------]
        if testList[i:i+length]==repList:      #<---[if testList[id:id+length]==repList.---------------------]
            #print(i, i+length)
            return i, i + length               #<---[return id and (id + length).----------------------------]
"""
amazing short little app. Takes two lists. One, the testList, is the main list on which you want to perform
changes and two, the second one called repList, it contains the values on -the main list- that are to be 
replaced. Then !!check this out!!, a third argument which is a self-contained variable set to the value of 0.
Write that down, ok, now interesting part, FOR item within range of -start- until the length of the 
testList IF THE INDEX OF testList SET TO THE RANGE OF [i:i+length] <---opens portal---> IS ==EQUAL== TO
-THE- repList, then it returns ~THOSE~ values. So basically it locates a specific SET OF ITEMs 
--WITHIN THAT RANGE--
by looking for MATCHES, and then returns the 3 values if it found a match. This example does not include what
to do if the values don't match, so note to self.

"""
#helper function to perform final task
def replaceSub(testList, repList, newList):        #<---[takes three arguments, testList, repList and newList]
    length=len(newList)                       #<---[acknowledge length of newList and assign to length var.---]
    idx=0                                          #<---[counter for index.----------------------------------]
    for start, end in iter(lambda: subFunction(testList, repList, idx), None):
        #start and end could be x and y. lambda function retrieves tuple from subFunction().
        #then looks for that range in testList and replaces that content with the contents of new list.
        testList[start:end]=newList               #<---[Assigns newList with the value of testList range.---]
        #idx=start+length                         #<---[------]
        print(testList)
# initializing list
test_list=[4,5,6,7,10,2]
# printing original list
#-----print("The original list is: "+str(test_list))
# replace list
repl_list=[5,6,7]
new_list=[0,0,0]
# Replace sublist with other in list
# using loop (when sublist is given)
#------this calls function: replaceSub(test_list, repl_list, new_list)
# Printing result
#------print("List after replacing sublist: "+ str(test_list))

#-------substitution--tool----------#
#-----------------------------------#
#-----------------------------------#
#-----------------------------------#

# --8--  M I N  M A X  S U M #

"""Note:
Use substitution tool."""

def minMaxSum(array):
    lst=[]
    lst.append([i for i in array])
    lst=lst[0]
    #print(lst)
    cam=[]
    for i in range(len(array)):
        array[i]=0
        cam.append(sum(array))
        array[:i+1]=lst[:i+1]
        #print(cam)
    print(min(cam), max(cam))



#fiveDigits=[1,2,3,4,5,6,7,9,15,19]
#fiveEquals=[1,1,1,1,1]
#minMaxSum(fiveDigits)
#minMaxSum(fiveEquals)


#  --9--  T I M E  C O N V E R S I O N #
"""
07:05:45PM
19:05:45PM


def timeConversion(s):
    if s.endswith("PM"):
        var=int((s[0:2]))
        print("{}{}".format(var+12,s[2:8]))
    else:
        print("{}".format(s[0:8]))

timeConversion("07:05:45PM")
timeConversion("07:05:45AM")
"""

"""FAILED TRY, SOLUTION BELOW, ANALYSIS PENDING"""
"""On initial assesment, it looks like the mistake was originated
byt using the print statement instead of returning the result.

In the successful solution a variable was specifically created to
hold the result to enable the use of return."""

def timeConversion(s):
    # Complete this function
    amOrPm = s[-2:]
    toReturn = ""

    if(amOrPm == "PM"):
        if(int(s[0:2]) < 12):
            toReturn = toReturn + str(12 + int(s[0:2])) + s[2:-2]
        else:
            toReturn = toReturn + str(int(s[0:2])) + s[2:-2]
    else:
        if(s[0:2] == '12'):
            toReturn = toReturn + "00" + s[2:-2]
        else:
            toReturn = toReturn + s[:-2]

    return toReturn

#print(timeConversion("07:05:45PM"))
#timeConversion("07:05:45AM")


#  --10--  C O U N T I N G  V A L L E Y S #

"""n steps, for every step hiker recorded if it was uphill, U,
or a downhill, D. the hike starts and ends at sea level and
each step represents a unit change of altitude.

A Mountain is a sequence of consecutive steps ABOVE sea level and
A Valley is a sequence of consecutive steps below sea level.

Given hikers sequence of up and down steps during his last hike,
find and print the number of valleys he walked through.

"""
def countingValleys(n, ar):
    count=0
    valleyCount=0
    for i in range(n):
        if ar[i] == "U":
            count+=1
            if count==0:
                valleyCount+=1
        elif ar[i]=="D":
            count-=1
    print(valleyCount)

#countingValleys(10, "UDDDUDUUDU")
#countingValleys(8, "UDDDUDUU")

#  --11--  S T O C K  M E R C H A N T #

def stockMerchant(n, arr):
    arr.sort()
    pairs=0
    count=0
    while count < n-1:
        if arr[count]==arr[count+1]:
            count+=2
            pairs+=1
        else:
            count+=1
    return(pairs)

#stockMerchant(10, [50,10,20,20,10,10,30,50,10,20])
print(stockMerchant(9, [10,20,20,10,10,30,50,10,20]))


