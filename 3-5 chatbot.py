import time

print('Hello. I am Zyxo 64. I am a chatbot.')
print('I like animals and I love to talk about food.')
name = input('What is your name?: ')
print('Hello', name, ', Nice to meet you.')

time.sleep(1)

# get year information
year = input('I am not very good at dates. What \
is the year?: ')
while not (year == '2020'):
    year = input('I don`t think that is correct. Try again? ')
print('Yes, I think you are correct.')

time.sleep(1)

# ask user to guess age
myage = input('Can you guess my age? - enter a \
number: ')
print('Yes you are right. I am ', myage)

time.sleep(1)

# do math to calculate when chatbot will be 100
myage = int(myage)
nyears = 100 - myage
print('I will be 100 in', nyears, 'years.')
print('That will be the year', int(year) + \
      nyears, '.')

time.sleep(1)

# food conversation
print('I love chocolate and I also like trying out new kinds of food')
food = input('How about you? What is your favorite food?: ')
print('I like', food, 'too.')
question = 'How many times a day do you eat ' + food + '?: '
howoften = input(question)
howoften = int(howoften)
if howoften > 3:
    print('Wow. That is probably not healthy.')
else:
    print('That seems like a healthy amount of' + food + ".")

time.sleep(1)

# animal conversation
animal = input('My favorite animal is a giraffe. What is yours?: ')
if animal == 'cat':
    print('I love cats! They are very cute.')
elif animal == 'dog':
    print('I love dogs! They bark very loud though.')
else:
    print(animal,'! I do not like them.')
print('I wonder if a', animal, 'likes to eat', food, '?')

time.sleep(1)

# conversation about feelings
feeling = input('How are you feeling today?: ')
if feeling == 'sad' or feeling == 'mad' or feeling == 'angry':
    print('I am sorry to hear that :C I hope you feel better soon.')
elif feeling == 'happy':
    print('That is great to hear! I am glad you feel ' + feeling + ".")
    
print('Why are you feeling', feeling, 'now?')
reason = input('Please tell me: ')
print('I understand. Thanks for sharing.')

time.sleep(1)

# goodbye
print('It has been a long day')
print('I am too tired to talk. We can chat again later.')
print('Goodbye', name,', I liked chatting with you.')
