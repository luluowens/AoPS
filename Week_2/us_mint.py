'''You've just been named the new director of the United States Mint.
For some reason, you've been authorized to do whatever you want
with our coinage. You want to simplify our coins using the following criteria:

1. There should be only three denominations of coins.
You can keep any three existing denominations
(for example, 1, 5, and 10; or 1, 10, and 25) or come up with new ones
(for example, 1, 8, and 20).

2. Assume that in any transaction, the number of cents given as change
is equally likely to be any of the hundred quantities from 0 to 99,
and always uses the minimum number of coins necessary.

Your goal is to minimize the average number of coins that have to be given as change.

For this part of the problem, write a Python program to answer the following question:
If you decided to keep 1, 10, and 25 cent coins, what would be the
average number of coins given as change?'''


def changes(value, denoms, value_coins) :
    if value == 0 :
        return 0 
    elif value in value_coins :
        return value_coins[value]
    else :
        return 1 + min([changes(value - denom, denoms, value_coins) for denom in denoms if value >= denom])

def coins(max, denoms, value_coins) :
    total_coins = 0
    for value in range(max) :
        coins = changes(value, denoms, value_coins)
        value_coins.update({value: coins})
        # print(f'value:{value}, coins:{coins}')
        total_coins += coins
    return total_coins / max

def minimum() :
    min_val = 5.4
    d_1 = 10
    d_2 = 25
    min_coins = 0
    for denom_1 in range(3, 100) :
        for denom_2 in range(2, denom_1) :
            value_coins = {}
            denoms = [1, denom_1, denom_2]
            min_coins = coins(100, denoms, value_coins)
            if min_coins <= min_val :
                min_val = min_coins
                d_1 = denom_1
                d_2 = denom_2
    return "1, " + str(d_1) + ", " + str(d_2)

# print(change(10, [25, 10]))
# # should be: 1
# print(change(15, [25, 10]))
# # should be: 6
# print(change(25, [25, 10]))
# # should be: 1
# print(change(50, [25, 10]))
# # should be: 2
# print(change(65, [25, 10]))
# # should be: 8
# print(change(35, [25, 10]))
# # should be: 2
# print(change(44, [25, 10]))
# # should be: 8

# print(coins(100, [25, 10, 1]))
# print(minimum())
print(coins(100, [19, 12, 1], {}))