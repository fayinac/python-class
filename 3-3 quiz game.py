score = 0

question = ['What is the capital of Arizona: ', 'How many federal states does Germany have: ', 'What is the capital of Denmark: ', 'what is the Largest state in the US: ',
             'How many timezones does China have: ']

answers = ['Phoenix', '16', 'Copenhagen', 'Alaska', '1']

n = 5

for i in range(5):
    answer = input(question[i])
    if answer == answers[i]:
        print('Your answer is correct')
        score += 1
    else:
        print('You are incorrect')
        print('the correct answer is ', answers[i])
print('your score is', score)
        
