#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 25 07:31:16 2020

@author: avni_aaron
"""


def fib(n):
    if n == 0 or n == 1:
        return 1
    return fib(n-1) + fib(n-2)

def answer(total_lambs):
    max_lst = []
    min_lst = []
    i = 0
    while sum(max_lst) >= total_lambs:
        max_lst.append(2**i)
        i += 1
    i = 0
    while sum(min_lst) >= total_lambs:
        min_lst.append(fib(i))
        i += 1
    # max_lst.pop(-1)
    # min_lst.pop(-1)
    return len(min_lst) - len(max_lst)
