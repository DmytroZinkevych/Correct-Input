def input_int(*message, base=10, err="Incorrect input, please try again:"):
    while True:
        if message:                            # if message[0] exists
            num = input(message[0])
        else:
            num = input()
        try:
            num = int(num, base=base)
            return num
        except ValueError:
            print(err)


def input_float(*message, err="Incorrect input, please try again:"):
    while True:
        if message:                            # if message[0] exists
            num = input(message[0])
        else:
            num = input()
        num = num.replace(',', '.')
        if num != '' and num[0] == '.':
            num = '0' + num
        try:
            num = float(num)
            return num
        except ValueError:
            print(err)


def input_num(*message, err="Incorrect input, please try again:"):
    while True:
        if message:                            # if message[0] exists
            num = input(message[0])
        else:
            num = input()
        num = num.replace(',', '.')
        i = num.find('.')
        if i == -1 and num.isdecimal():
            return int(num)
        else:
            if num != '' and num[0] == '.':
                num = '0' + num
            try:
                num = float(num)
                return num
            except ValueError:
                print(err)
