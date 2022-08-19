def hello():
    print('Hello!')


hello()


def pack(arg1, arg2, arg3):
    return [arg1, arg2, arg3]


print(pack('toothbrush', 'socks', 'pillow'))
print(pack(1, 2, 3))


def eat_lunch(list):
    if len(list) == 0:
        print('My lunchbox is empty!')
    else:
        for i in range(len(list)):
            if i == 0:
                print(f"First I eat {list[0]}")
            else:
                print(f'Next I eat {list[i]}')


eat_lunch(['sandwich'])
eat_lunch(['sandwich', 'yogurt', 'grapes'])
eat_lunch([])
