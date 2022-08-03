def decode_ints(s_from, s_to, L):
    """ s_from, s_to are lowercase strings of equal length, each 
                     only containing character digits 0-9 in some order
        L is a list of positive ints
        
        Returns a tuple of (map, L_decoded) where:
        * map is a dict of 10 keys mapping an int digit in s_from at index i
          to a corresponding int digit in s_to at index i. 
        * L_decoded is list of decoded ints using the map, where each digit
          in the int is mapped to its corresponding digit from the map
          (ignore all leading zeroes in decoded ints. ) """
    map = {}
    for i in range(len(s_from)) :
        map[int(s_from[i])] = int(s_to[i])
    
    L_decoded = []
    for number in L :
        encrypted = str(number)
        decoded = ""
        for digit in encrypted :
            decoded += str(map[int(digit)])
        L_decoded.append(int(decoded))
    
    return (map, L_decoded)



# testing
s_from = "0123456789"
s_to =   "9876543210"
L = [1, 5, 123]
print(decode_ints(s_from, s_to, L))  # prints a tuple:
# ({0:9,1:8,2:7,3:6,4:5,5:4,6:3,7:2,8:1,9:0}, [8, 4, 876])

s_from = "1234567890"
s_to =   "0234567891"
L = [0, 6719]
print(decode_ints(s_from, s_to, L))  # prints a tuple:
# ({1:0,2:2,3:3,4:4,5:5,6:6,7:7,8:8,9:9,0:1}, [1, 6709])

s_from = "1234567890"
s_to =   "9743652018"
L = [571, 233, 1089, 64]
print(decode_ints(s_from, s_to, L))  # prints a tuple:
# ({1:9,2:7,3:4,4:3,5:6,6:5,7:2,8:0,9:1,0:8}, [629, 744, 9801, 53])