#CONCATENATING IN PYTHON
#First method
import numpy as n #you can install numpy from terminal using pip install numpy
array1 = n.array([1, 2, 3])
array2 = n.array([4, 5, 6])
array3 = array1 + array2 # Concatenating array1 and array2
print(array3) #This will output [5 7 9]

#second method
myarray1 = ('123; 4,6,5')
myarray2 = (" 348; 216")
myarray3 = myarray1 + myarray2
print(myarray3) #This will output 123; 465 348; 216

#Third method
myarray1 = ("1,2,3; 465;")
myarray2 = (" 348; 2,1,6")
myarray3 = myarray1 + myarray2
print(myarray3) #This will output 1,2,3; 465; 348; 2,1,6

# Fourth method
m = list [str]("123; 465")
mm = list [str] (" 348; 216")
mmm = m + mm
print(mmm) #This will output ['1', '2', '3', ';', ' ', '4', '6', '5', ' ', '3', '4', '8', ';', ' ', '2', '1', '6']
