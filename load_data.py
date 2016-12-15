#!/usr/bin/env python
# coding=utf-8

# 输入数据 data 的格式是：
# 第一行：物体的个数、背包的容量（空格分割）
# 第二行：物体i的重量（空格分割）
# 第三行：物体i的价值（空格分割）
# 
# 返回值：
# 物体的个数 n、背包的容量 m
# 物体的重量 w[]、物体的价值 v[]

def load_data(file_name):
    with open(file_name) as f_read:
        temp_line = f_read.readline().split()
        n, m = int(temp_line[0]), int(temp_line[1])
        w = [int(item) for item in f_read.readline().split()]
        v = [int(item) for item in f_read.readline().split()]

        return n, m, w, v

if __name__ == '__main__':
    file_name = 'data'
    load_data(file_name)
