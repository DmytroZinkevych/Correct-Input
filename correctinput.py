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
        i = num.find('.')
        if num[:i].isdecimal() and num[i + 1:].isdecimal():     # if symbols in num before and after point are ONLY decimal digits
            return float(num)
        else:
            print(err)


def input_num(*message, err="Incorrect input, please try again:"):
    while True:
        if message:                            # if message[0] exists
            num = input(message[0])
        else:
            num = input()
        num = num.replace(',', '.')
        i = num.find('.')
        if i == -1:
            if num.isdecimal():
                return int(num)
            else:
                print(err)
        else:
            if num[:i].isdecimal() and num[i + 1:].isdecimal():     # if symbols in num before and after point are ONLY decimal digits
                return float(num)
            else:
                print(err)
