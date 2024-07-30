successful = True
for number in range(3):
    print('Attempt')
    if successful:
        print("Successful")
        break
else:
    print("Attempted 3 times and failed !!")


for x in range(5):
    print(x)

print(type(5))
print(type(range(5)))

# Iterable
for x in "Jeetali":
    print(x)

count = 0
for x in range(1,10):
    if x%2 == 0:
        count +=1
        print(x)
print(f"we have {count} even numbers !!")
        