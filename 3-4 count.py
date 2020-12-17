number = input('Enter number you want to count by: ')
number = int(number)

n = 0

choice = input('Enter return to continue or q to quit: ')

while not(choice == 'q'):
    print(n)
    n = n + number
    choice = input('Enter return to continue or q to quit: ')
