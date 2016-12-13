#!/usr/bin/env python
# coding=utf-8

# 输入数据 data 的格式是：
# 第一行：物体的个数、背包的容量（空格分割）
# 第二行：物体i的重量（空格分割）
# 第三行：物体i的价值（空格分割）
# 
# 返回值：
# 物体的个数 N、背包的容量 C
# 物体的重量 weight[]、物体的价值 value[]

def load_data(file_name):
    with open(file_name) as f_read:
        temp_line = f_read.readline().split()
        N, C = int(temp_line[0]), float(temp_line[1])
        weight = [float(item) for item in f_read.readline().split()]
        value = [float(item) for item in f_read.readline().split()]

        return N, C, weight, value

if __name__ == '__main__':
    file_name = 'data'
    load_data(file_name)
