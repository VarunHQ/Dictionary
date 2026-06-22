d = {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}

user_input = input('Enter a key: ')

try:
    key = int(user_input)
except ValueError:
    print('Invalid input. Please enter an integer key.')
else:
    if key in d:
        print('Value for key', key, 'is', d[key])
    else:
        print('Key not found in dictionary.')
