import array
# 1. create an array and traverse

def createAndTraverse():
    print("1. create an array and traverse")
    arr = array.array('i', [1,2,3,4,5])
    for i in range(len(arr)):
        print(arr[i]);

createAndTraverse();

# 2. Access individual elements through indexes

def accessElementsByIndexes(index):
    print("2. Access individual elements through indexes")
    arr = array.array('i',[1,2,3,4,5])
    if(index >= len(arr)):
        print("There is no any element with that index")
    else:
        print(arr[index])

accessElementsByIndexes(3)

# 3. Append any value to the array using append() method

def appendValue(value):
    print("3. Append any value to the array using append() method")
    arr = array.array('i',[1,2,3,4,5])
    arr = array.array('i',[1,2,3,4,5])
    print(arr)
    arr.append(value)
    print(arr)

appendValue(42)

# 4. Insert value in an array using insert() method
def insertValue(index, value):
    print("4. Insert value in an array using insert() method")
    arr = array.array('i',[1,2,3,4,5])
    print(arr)
    arr.insert(index,value)
    print(arr)

insertValue(3,434)

# 5. Extend python array using extend() method

def extendArray():
    print("5. Extend python array using extend() method")
    arr = array.array('i',[1,2,3,4,5])
    print(arr)
    arr.extend([6,7,8])
    print(arr)

extendArray()

# 6. Add items from list into array using fromList() method

def addItemsFromList():
    print("6. Add items from list into array using fromList() method")
    auxList = [6,7,8,9,10]
    arr = array.array('i',[1,2,3,4,5])
    print(arr)
    arr.fromlist(auxList)
    print(arr)

addItemsFromList()

# 7. Remove any array element using remove() method

def removeElementArray(value):
    print("7. Remove any array element using remove() method")
    arr = array.array('i',[1,2,3,4,5])
    print(arr)
    arr.remove(value)
    print(arr)

removeElementArray(4)

# 8. Remove last array element using pop() method

def removeLastElement():
    print("8. Remove last array element using pop() method")
    arr = array.array('i',[1,2,3,4,5])
    print(arr)
    arr.pop()
    print(arr)
    
removeLastElement()

# 9. Fetch any element through its index using index() method

def fetchElementWithIndexMethod(value):
    print("9. Fetch any element through its index using index() method")
    arr = array.array('i',[1,2,3,4,5])
    print(arr)
    print(arr.index(value))

fetchElementWithIndexMethod(5)

# 10. Reverse a python array using reverse() method
    

def reverseArray():
    print("10. Reverse a python array using reverse() method")
    arr = array.array('i',[1,2,3,4,5])
    print(arr)
    arr.reverse()
    print(arr)
    
reverseArray()

# 11. Get array buffer information through buffer_info() method

def getBufferInfo():
    print("11. Get array buffer information through buffer_info() method")
    arr = array.array('i',[1,2,3,4,5])
    print(arr.buffer_info())
    
getBufferInfo();

# 12. Check for number of occurrences of an element using count() method

def getOccurrences(value):
    print("12. Check for number of occurrences of an element using count() method")
    arr = array.array('i',[1,2,3,4,5,3,5,2,4,3,23,2,3,123,24,3,3,4,23,423,4,32,])
    print(f"Occurrences of {value}: {arr.count(value)}")
    
getOccurrences(3)

# 13. Convert array to a python list with same elements using toList() method
def convertArrayToList():
    print("13. Convert array to a python list with same elements using toList() method")
    arr = array.array('i',[1,2,3,4,5])
    print(arr.tolist())
    
convertArrayToList()
    
# 14. Slice Elements from an array

def sliceElementsFromArray():
    print("14. Slice Elements from an array")
    arr = array.array('i',[1,2,3,4,5,6,7,8])
    print(f"First half: {arr[0:4]}")
    print(f"Seconf half: {arr[4:8]}")

sliceElementsFromArray();