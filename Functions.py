#def greet(first_name, last_name):
#    print(f'Hi {first_name} {last_name}')
#    print('Welcome aboard')


#greet("Jeetali", "Srivastava")

#greet("J","S")

#There are two types of functions
# 1- A function that perform a task
#def get_greeting(name):
#    return f'Hi {name}'

#name  = get_greeting("Jeetali")
#print(name)

# 2- A function that return a calculated value
#round(1.9)
#def increment(number, by=4):
#    return number+by

#print(increment(2))
    


def fizzbuzz(input):
    if (input % 3 ==0) and (input % 5 == 0):
        return "FizzBuzz"
    if input % 3 == 0:
        return "Fizz"
    if input % 5 == 0:
        return "Buzz"
    return input

print(fizzbuzz(17))
