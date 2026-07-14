#Loops: allow us to iterate over collection of items

#Basic for loop
fruits = ['apple', 'banana', 'cherry']
for fruit in fruits:
    print(fruit)

#for loop with range
for i in range(5):
    print(i)

    # for loop with dictionary
    person = {'name': 'Harsh', 'age': 20, 'city': 'Mumbai'}
    for key, value in person.items():
        print(f"{key}: {value}")