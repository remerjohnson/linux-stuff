# coding: utf-8

import os

f1 = open('cv_list.txt', 'r')

f2 = open('cv_list_stripped.txt', 'w')

good_list = []

for line in f1:
    line = line.strip()
    good_list.append(line)
    continue


# print good_list

for line in good_list:
    f2.write(line+'\n')
    continue

f2.close()
