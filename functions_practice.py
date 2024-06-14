def hello():
    print('Greetings user!')

hello()

def pack(item1, item2, item3):
    return([item1, item2, item3])

print('Here is what I have in my lunchbox today:', pack('Apple', 'Sandwich', 'Cookie'))

# lunchbox = ['Apple', 'Sandwich', 'Juicebox', 'Cookie']

def eat_lunch(lunchbox):
    for i, item in enumerate(lunchbox):
        if i == 0:
            print(f'First I eat my {item}.')
        elif i == 1:
            print(f'Second I eat my {item}')
        elif i == 2:
            print(f'Lastly, I eat my {item}')
        else:
            print('My lunchbox is empty!')

eat_lunch(['Apple', 'Sandwich', 'Cookie'])