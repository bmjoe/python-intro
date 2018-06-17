print('Hi dude!')

print('Whats your name?')
usr_name = input()
print('So, ' + usr_name + ' is my homie.')

print('How old are you?')

while True:
    usr_age = input()
    if int(usr_age) < 100:

        years_left = str(100 - int(usr_age))

        print(
            'Holy cow, {0}, you have {1} years left! \nIf I had {1} years I\'ll learn \
programming till I die!'.format(
                usr_name,
                years_left
            )
        )
        break
    else:
        print('No way {} you can\'t be so old! Type your real age'.format(
            usr_name
        ))

print('Good Luck, {}!'.format(usr_name))
