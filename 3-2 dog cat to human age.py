animal = input('Enter dog or cat: ')

while not(animal == 'dog' or animal == 'cat'):
    animal = input('Enter dog or cat: ')

age = input('Enter age of animal: ')
age = int(age)

if animal == 'dog' and age == 1:
    human_age = 12
elif animal == 'dog' and age == 2:
    human_age = 24
elif animal == 'cat' and age == 1:
    human_age = 15
elif animal == 'cat' and age == 2:
    human_age = 24
elif age > 2:
    human_age = 24 + (age - 2) * 4

print('Human age of', animal, " is", human_age)
