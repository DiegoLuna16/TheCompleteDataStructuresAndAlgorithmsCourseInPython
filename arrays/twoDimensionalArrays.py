import numpy as np

#Creating two dimensional array 

twoDimensionalArray = np.array( [ [11, 15, 10, 6], [10, 14, 11, 5], [12, 17, 12, 8], [15, 18, 14, 9]] )
print(twoDimensionalArray)

#Insertion in two dimensional array

twoDimensionalArray2 = np.insert(twoDimensionalArray, 1, [[1,2,3,4]], axis=1)
print(twoDimensionalArray2)

twoDimensionalArray3 = np.append(twoDimensionalArray, [[1,2,3,4]], axis=0)
print(twoDimensionalArray3)

#Accesing values in two dimensional array

twoDimensionalArray4 = np.array( [ [11, 15, 10, 6], [10, 14, 11, 5], [12, 17, 12, 8], [15, 18, 14, 9]] )
print(twoDimensionalArray4[0])
def accessElement(array, rowIndex, colIndex):
    if rowIndex >= len(array) and colIndex >= len(array[0]):
        print("There no element with those indexes")
    else:
        print(array[rowIndex][colIndex])

accessElement(twoDimensionalArray4,3,3)

#Traversing Two Dimensional Array

def traversing(array):
    for i in range(len(array)):
        for j in range(len(array[0])):
            print(array[i][j])
    
traversing(twoDimensionalArray4)


