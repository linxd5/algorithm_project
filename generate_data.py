#!/usr/bin/env python
# coding=utf-8

# 自己生成 0-1 背包问题
# 问题规模 N 1000，物体重量 weight 范围 1-100，价值 value 范围 1-100
# 重量与价值无关，背包容量设置为物体总重量的二分之一。


import random

def generate_data(data_file):
    N, C = 1000, 0
    weight, value = [], []
    sum_weight = 0

    for i in range(N):
        weight.append(str(random.randint(1, 100)))
        value.append(str(random.randint(1, 100)))
        sum_weight += int(value[i])

    C = int(sum_weight/2)

    with open(data_file, 'w') as f_write:
        f_write.write(str(N) + ' ' + str(C) + '\n')
        f_write.write('0 ' + ' '.join(weight) + '\n')
        f_write.write('0 ' + ' '.join(value) + '\n')


if __name__ == '__main__':
    data_file = 'data'
    generate_data(data_file)
