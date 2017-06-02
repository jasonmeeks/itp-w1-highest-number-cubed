"""This is the entry point of the program."""


def highest_number_cubed(limit):
    number = 0
    
    while True:
        number += 1
        if number ** 3 > limit:
            return number - 1
            
        

# 1 ** 3 = 1
# 2 ** 3 = 8
# 3 ** 3 = 27
                # < 30
# 4 ** 3 = 64 