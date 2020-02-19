#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
# compare.py

import sys
def main(version1, version2):
    v1 = version1.split(".")
    v2 = version2.split(".")
    lv1, lv2 = len(v1), len(v2)
    i, j = 0, 0
    
    while i < lv1 and j < lv2:
        # int 去掉字符串格式数字前的0
        n1, n2 = int(v1[i]), int(v2[j])
        if n1 < n2:
            return -1
        elif n1 > n2:
            return 1
        i += 1
        j += 1

    if lv1 == lv2 and n1 == n2:
        return 0

    if lv1 > lv2:
        while i < lv1 and int(v1[i]) == 0:
            i += 1
        if i == lv1:
            return 0
        else:
            return 1

    if lv1 < lv2:
        while j < lv2 and int(v2[j]) == 0:
            j += 1
        if j == lv2:
            return 0
        else:
            return -1
        return -1
if __name__ == '__main__':
    if len(sys.argv) < 3:
        print('usage: python {} v1 v2'.format(sys.argv[0]))
        sys.exit(1)
    print(main(sys.argv[1], sys.argv[2]))
