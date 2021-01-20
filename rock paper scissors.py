import random

choices = ('rock', 'paper', 'scissors')

win = loss = tie = 0

while True:
   user_choice = input('Enter rock, paper, scissors, or stop: ')
   if user_choice == 'stop':
      break
   if user_choice not in choices:
      print('invalid input')
      continue
   
   cpu_choice = random.choice(choices)
   print('Computer chose', cpu_choice)

   if user_choice == 'rock' and cpu_choice == 'rock':
      print("it's a tie")
      tie += 1
      continue
   if user_choice == 'rock' and cpu_choice == 'paper':
      print('you lose')
      loss += 1
      continue
   if user_choice == 'rock' and cpu_choice == 'scissors':
      print('you win!')
      win += 1
      continue

   if user_choice == 'paper' and cpu_choice == 'paper':
      print("it's a tie")
      tie += 1
      continue
   if user_choice == 'paper' and cpu_choice == 'scissors':
      print('you lose')
      loss += 1
      continue
   if user_choice == 'paper' and cpu_choice == 'rock':
      print('you win!')
      win += 1
      continue

   if user_choice == 'scissors' and cpu_choice == 'scissors':
      print("it's a tie")
      tie += 1
      continue
   if user_choice == 'scissors' and cpu_choice == 'rock':
      print('you lose')
      loss += 1
      continue
   if user_choice == 'scissors' and cpu_choice == 'paper':
      print('you win!')
      win += 1
      continue

print('you have', win, 'win(s),', loss, 'loss(es), and', tie, 'tie(s).' )

   

   
   
   
