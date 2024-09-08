from numpy import *

twoDarray = array([
    [1,2,3,4,5,6],
    [7,8,9,10,11,12]
])
print(twoDarray)

# To convert this 2-D array to one-d array we use flatten check below

twoDarray = array([
    [1,2,3,4,5,6],
    [7,8,9,10,11,12]
    ])
    
twoDarray2 = twoDarray.flatten()
print(twoDarray2) #The output will be [ 1  2  3  4  5  6  7  8  9 10 11 12]

#Example 2
m1 = matrix('2 3 4; 4 5 6')
m2 = matrix('3 4 7; 2 4 9')
m3 = m1 + m2
print(m3) #The output will be  [[ 5  7 11]
 #                              [ 6  9 15]]