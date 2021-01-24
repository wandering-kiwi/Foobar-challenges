#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Aug 20 20:24:06 2020

@author: avni_aaron
"""
import numpy as np
def solution(src, dest):
    move_lst = np.array([0, 0, 0, 0])
    move_set = [6, 10, 15, 17]
    src_x = int(src / 8)
    src_y = src % 8
    dest_x = int(dest / 8)
    dest_y = dest % 8
    right = np.array([1, 1, -1, 0])
    down = np.array([1, 0, -1, 1])
    left = [-1, -1, 1, 0]
    up = [-1, 0, 1, -1]
    simplify = np.array([[2, 2, -1, 1], [2, 2, 1, -1], [-2, -2, 1, -1], [-2, -2, -1, 1]])
    for i in range(dest_x - src_x):
        move_lst = move_lst + down
    for j in range(dest_y - src_y):
        move_lst = move_lst + right
    if move_lst[0] > 0:
        simplify = simplify[2:4]
    else:
        simplify = simplify[:2]
    if move_lst[2] > 0:
        simplify = simplify[1]
    else:
        simplify = simplify[0]
    return sum(abs(move_lst + simplify))
    
    
    
    
'''  
    
    
    if src % 8 < 2:
        # move_lst[0] = -
        # move_lst[1] = +
        if src % 8 == 0:
            # move_lst[2] = - 
            pass
            
    elif src % 8 > 5:
        # move_lst[0] = +
        # move_lst[1] = -
        if src % 8 == 7:
            # move_lst[2] = +
            pass
    if int(src / 8) < 2:
        # move_lst[2] = +
        # move_lst[3"""] = +
        if int(src / 8) == 0:
            # move_lst[0] = +
            # move_lst[1] = +
            pass
        
 0  1  2  3  4  5  6  7
 8  9 10 11 12 13 14 15
16 17 18 19 20 21 22 23
24 25 26 27 28 29 30 31
32 33 34 35 36 37 38 39
40 41 42 43 44 45 46 47
48 49 50 51 52 53 54 55
56 57 58 59 60 61 62 63

move_lst = np.array([1, 1, 1, 1])
move_set = np.array([6, 10, 15, 17])
print(sum(move_lst * move_set))
'''
print(solution(0, 63))