import random
ls = ['tossing', 'throwing', 'kicking', 'shooting', 'blowing', 'dancing', 'dropping']
ls2 = ['shot','bot','cot','pot','lot','dot']
one = ls2[random.randint(0,6)]
two = ls[random.randint(0,5)]
three = ls2[random.randint(0,5)]
ls3 = ['young','old']
four = ls3[random.randint(0,1)]
ls4 = ['scrappy','happy','hungry','sappy','ratty','naughty','crappy']
five = ls4[random.randint(0,6)]
six = ls4[random.randint(0,6)]

print('''I am not throwing away my %s
I am not %s away my %s
Hey yo, I'm just like my country
I'm %s, %s and %s
And I'm not %s away my %s
''' %(one, two, three, four, five, six, two, three))
