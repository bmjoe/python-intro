# Messages block

hi_message = '''
Hi dude!
Whats your name?
'''

print(hi_message)
usr_name = input()

age_message = '''
Nice to meet you!
How old are you {}?
'''.format(usr_name)

prognosis_message = '''
Holy cow, {0}, you have {1} years left!
If I had {1} years I\'ll learn programming everyday!
'''
false_message = '''
No way {}! You can\'t be so old! Type your real age.
'''


print(age_message)

while True:
    usr_age = input()
    if int(usr_age) < 100:

        years_left = str(100 - int(usr_age))
        print(prognosis_message.format(usr_name, years_left))
        break
    else:
        print(false_message.format(usr_name))

print('Good Luck, {}!\n'.format(usr_name))
