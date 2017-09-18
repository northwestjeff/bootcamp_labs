"""
# Lab: Decorators

##### Goal

Write a Python Decorator that will tell us how long a function took to execute.

##### Instructions

Use pythons time module to calculate the time it took a function to execute.
"""

import timeit
import random
import statistics
import datetime
import time



def timing(func, *args):
    def wrapper(args):
        start = time.time()
        some_var = func(args)
        end = time.time()
        delta = end - start
        # print("\n\n\n")
        # print("this took {} seconds.".format(delta))
        return some_var, delta #how to have this come after the running the function.
    return wrapper


# my_list = [1, random.randint(1, 15), 3, 1, 5, 1, 17, random.randint(1,15)]

# @timing
# def average_within_list(my_list):
#     avg_num = statistics.mean(my_list)
#     return avg_num

#
# if __name__ == '__main__':
#     avg_num = average_within_list(my_list)
#     print(avg_num)
