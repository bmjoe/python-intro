print('\nHi dude!')
print('Whats your name?\n')

usr_name = input()
print(' ')

print('So, ' + usr_name + ' is my homie.')
print('How old are you?\n')

while True:
    usr_age = input()
    print(' ')
    if int(usr_age) < 100:

        years_left = str(100 - int(usr_age))

        print(
            'Holy cow, {0}, you have {1} years left! \nIf I had {1} years I\'ll learn \
programming everyday!\n'.format(
                usr_name,
                years_left
            )
        )
        break
    else:
        print('No way {}! You can\'t be so old! Type your real age.\n'.format(
            usr_name
        ))

print('Good Luck, {}!\n'.format(usr_name))
