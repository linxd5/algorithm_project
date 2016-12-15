#!/usr/bin/env python
# coding=utf-8

# 输入: 物体的个数n，背包的容量m，物体的重量w[]和物体的价值p[]
# 输出：装入背包的物体 x[]，背包中物体的价值 v

from load_data import load_data
import logging, time

logging.basicConfig(format='%(levelname)s : %(message)s', level=logging.INFO)

def dp_algorithm(data_file):
    n, m, w, p = load_data(data_file)
    optp = [[0 for i in range(m+1)] for j in range(n+1)]

    for i in range(1, n+1):
        for j in range(1, m+1):
            optp[i][j] = optp[i-1][j]
            if j >= w[i] and optp[i-1][j-w[i]]+p[i] > optp[i-1][j]:
                optp[i][j] = optp[i-1][j-w[i]]+p[i]

    """
    for i in range(n+1):
        for j in range(m+1):
            print(optp[i][j], end=" ")
        print('\n')
    """
    max = 0
    for i in range(n+1):
        for j in range(m+1):
            if optp[i][j] > max:
                max = optp[i][j]

    return optp, max

if __name__ == '__main__':
    begin = time.time()
    data_file = 'data'
    optp, max = dp_algorithm(data_file)
    end = time.time()
    print('++++ Max: ', max)
    print('Using %.4fs' %(end-begin))


