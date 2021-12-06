#!/usr/bin/python3


def list_division(my_list_1, my_list_2, list_length):
    result = []
    for i in range(list_length):
        try:
            c = my_list_1[i] / my_list_2[i]
        except ZeroDivisionError:
            print("division by 0")
            c = 0
            continue
        except (TypeError, ValueError):
            print("wrong type")
            c = 0
            continue
        except IndexError:
            print("out of range")
            c = 0
            continue
        finally:
            result.append(c)
    return result
