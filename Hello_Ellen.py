print('hello from AWESOME Ellen')
print('Ellen is so cool yay')
print('are ready to become an Ellen member?')
print('take this test')
name = input('What is your name? ')
color = input('What is your favorite color? ')
print(name + ' likes ' + color)
birth_year = input('Birth year: ')
age = 2019 - int(birth_year)
print(type(birth_year))
print(type(age))
print(age)
print('Yay you successfully past the test')
print('Here is an activity you can do')
command = ''
while command != 'quit':
    command = input('> '). lower()
    if command == 'start':
        print('Car Started...')
    elif command == 'stop':
        print('Car Stopped')
    elif command =='help':
        print('''
        Start- To Start The Car
        Stop- To Stop The Car
        Quit- To Quit
        ''')
    else:
        print('Sorry, what you entered could not be understood')
