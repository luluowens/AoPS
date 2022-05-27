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

def coins() :
    total_num = 0
    for i in range(0, 100) :
        leftover = i - (i // 25) * 25 - ((i % 25) // 10) * 10
        num_coins = i // 25 + (i % 25) // 10 + leftover
        total_num += num_coins
    return total_num / 100

def change(i) :
    leftover = i - (i // 25) * 25 - ((i % 25) // 10) * 10
    return i // 25 + (i % 25) // 10 + leftover


# print(change(10))
# # should be: 1
# print(change(15))
# # should be: 6
# print(change(25))
# # should be: 1
# print(change(50))
# # should be: 2
# print(change(65))
# # should be: 8
# print(change(0))
# # should be: 0
# print(change(99))
# # should be: 9
# print(change(11))
# # should be: 2
print(change(35))
# should be: 2

# print(coins())