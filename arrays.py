#Initialization 
import array

arr = array.array('i',)
print(arr)

arr_1 = array.array('i', [1,2,3])
print(arr_1)

import numpy as np

np_arr = np.array([], dtype=int)
print(np_arr)

np_arr1 = np.array([1,2,3,4], dtype=int)
print(np_arr)

#Insertion to Array

arr_3 = array.array('i', [1,2,3,4])
print(arr_3)
arr_3.insert(0,6) #first parameter is the index and the seconde one the value 
print(arr_3)

#Array traversal

def traversalArray(array):
    for i in array:
        print(i)

traversalArray(arr_3)

#Access array element
arr_4 = array.array('i', [1,2,3,4])

def accessElement(array, index):
    if index > len(array):
        print('There is not any element in this index')
    else:
        print(array[index])

accessElement(arr_4,12)