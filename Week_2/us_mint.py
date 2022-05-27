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