#Collection = single "variable" used to store multiple values
# List = [] Ordered and changable (Mutable), duplicates are fine.
# Set = {} Unordered and immutable. Add/Remove are fine but no duplicates.
# Tuple = () Ordered and immutable. Suplicates are fine. Faster


#fruits = ["apple", "banana", "orange", "kiwi"]
#print(fruits[3])
#print(dir(fruits))
#print(help(fruits))
#print(len(fruits))
#print('apple' in fruits)
#fruits[0] = 'pineapple'
#print(fruits)

#print(fruits.append('apple'))
#fruits.remove('pineapple')
#print(fruits)
#fruits.insert(0,'pineapple')
#print(fruits)
#fruits.sort()
#print(fruits)
#fruits.reverse()
#print(fruits)
#print(fruits.index('banana'))

#fruits = {"apple", "banana", "orange", "kiwi"}

#fruits.add("pineapple")
#fruits.remove('apple')
#fruits.pop()
#fruits.clear()
#print(fruits)
fruits = ("apple", "banana", "orange", "kiwi")
#print(fruits.index('apple'))
#print(fruits.count('kiwi'))

for f in fruits:
    print(f)