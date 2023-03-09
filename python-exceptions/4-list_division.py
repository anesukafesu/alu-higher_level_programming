#!/usr/bin/python3


def list_division(list_1, list_2, list_length):
    new_list = []

    for i in range(list_length):
        result = 0
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
