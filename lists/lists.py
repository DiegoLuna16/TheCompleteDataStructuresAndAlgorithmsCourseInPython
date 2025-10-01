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