#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    resultList = []
    for i in my_list:
        resultList.append(i % 2 == 0)
    return resultList
