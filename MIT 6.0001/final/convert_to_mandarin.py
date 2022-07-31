trans = {'0':'ling', '1':'yi', '2':'er', '3':'san', '4': 'si',
          '5':'wu', '6':'liu', '7':'qi', '8':'ba', '9':'jiu', '10': 'shi'}

def convert_to_mandarin(us_num):
    '''
    us_num, a string representing a US number 0 to 99
    returns the string mandarin representation of us_num
    '''
    num = int(us_num)
    if num <= 10 :
        return trans[us_num]
    elif num > 10 and num < 20 :
        return trans["10"] + " " + trans[str(num - 10)]
    else :
        if num % 10 == 0 :
            return trans[str(num // 10)] + " " + trans["10"]
        else :
            return trans[str(num // 10)] + " " + trans["10"] + " " + trans[str(num % 10)]


# testing
print(convert_to_mandarin('36'))
print(convert_to_mandarin('20'))
print(convert_to_mandarin('16'))
print(convert_to_mandarin("10"))