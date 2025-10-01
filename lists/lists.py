#Creation
ingredients = ['egg','meat']
print(ingredients)

invoices = [["Xbox", 12000], ["Play", 13000]]
print(invoices)

#Accesing element

firstElement = ingredients[0];
print(firstElement)

print('egg' in ingredients)
print('jam' in ingredients)

print(ingredients[-1])

#Traversing

for i in ingredients:
    print(i)
    
for i in range(len(ingredients)):
    ingredients[i] = ingredients[i]+"+"

print(ingredients)


#Update/Insert 

myList = [1,2,3,4,5,6,7]
print(myList)
myList[2] = 33
print(myList)
myList.insert(0, 100);
print(myList)
myList.append(200)
print(myList)

newList = [34,54,2,3,212,32,42]
myList.extend(newList);
print(myList)

#Slice/Delete

myList = ['a', 'b', 'c','d','e','f']
myList[0:2] = ['x','y']
print(myList[0:2])
print(myList)
myList.remove('x')
print(myList)
myList.pop(3)

del myList[-1]
print(myList)

#Searching

numbers = [10,20,30,40,50,60,70,80,90]

#in operator
target = 50
if target in numbers:
    print(f"{target} is in the list")
else:
    print(f"{target} is not in the list")

#Linear search

def linearSearch(list,target):
    for i, value in enumerate(list):
        if value == target:
            return i;
    return -1

print(linearSearch(numbers,80))
