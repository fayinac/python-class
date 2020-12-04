bill = input('What is the total on the bill? ')
tip_percent = input('What % tip would you like to give? ')
share = input('How many people are sharing the bill? ')

bill = int(bill)
tip_percent = int(tip_percent)
share = int(share)

tip_amount = bill * (tip_percent * 0.01)
total_bill = bill + tip_amount
tip_person = tip_amount / share
total_person = total_bill / share

print('Tip amount = ', tip_amount)
print('Total bill = ', total_bill)
print('--------------------')
print('Tip amount per person = ', tip_person)
print('Total amount per person = ', total_person)
