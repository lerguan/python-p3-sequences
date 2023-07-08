#!/usr/bin/env python3

def print_fibonacci(length):
    fibonacci_list = []
    for i in range(length):
        if i < 2:
            fibonacci_list.append(i)
        else:
            fibonacci_list.append(fibonacci_list[i-1] + fibonacci_list [i-2])
    print(fibonacci_list)
    pass