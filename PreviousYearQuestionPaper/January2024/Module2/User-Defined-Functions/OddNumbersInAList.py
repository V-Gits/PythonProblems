def odd_numbers_in_list(NUMLIST):
    ODDLIST = [x for x in NUMLIST if x%2 != 0]
    return ODDLIST

NUMLIST = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
ODDLIST = odd_numbers_in_list(NUMLIST)
print(f"{ODDLIST= }")