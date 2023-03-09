#!/usr/bin/python3


def list_division(list_1, list_2, list_length):
    new_list = []

    # For some reason result was being converted to a float data type
    # This caused errors with the testers
    result = int(0)

    for i in range(list_length):
        try:
            result = list_1[i] / list_2[i]
        except ZeroDivisionError:
            print('division by 0')
        except TypeError:
            print('wrong type')
        except IndexError:
            print('out of range')
        finally:
            new_list.append(result)

    return new_list
