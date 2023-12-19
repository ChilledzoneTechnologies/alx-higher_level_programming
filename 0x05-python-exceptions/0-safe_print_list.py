#!/usr/bin/python3


def safe_print_list(my_list=[], x=0):
    m = 0
    try:
        for i in my_list[0:x]:
            m += 1
            print('{}'.format(i), end='')
        print()
        return (m)
    except ValueError:
        print('Error')
