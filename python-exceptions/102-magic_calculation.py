#!/usr/bin/python

def magic_calculation(a, b):
    result = 0

    for i in range(1, 3):
        try:
            if a > i:
                raise Exception('Too far')
            else:
                result = result + (a ** b) / i
        except:
            result = a + b
            break

        
    return result
