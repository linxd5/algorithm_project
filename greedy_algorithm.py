#!/usr/bin/env python
# coding=utf-8

# 输入: 物体的个数N，背包的容量C，物体的重量weight[]和物体的价值value[]
# 输出：装入背包的物体 x[]，背包中物体的价值 v

from load_data import load_data
import operator, logging

logging.basicConfig(format='%(levelname)s : %(message)s', level=logging.INFO)

def greedy_algorithm(data_file):
    N, C, weight, value = load_data(data_file)

    # 计算每个物体的性价比并按照由大到小的顺序进行排序
    ppr = {}
    for i in range(N):
        ppr[i] = value[i] / weight[i]
    sorted_ppr = sorted(ppr.items(), key=operator.itemgetter(1), reverse=True)

    logging.info("一共有%d个物品，背包重量为%f" %(N, C))
    for (k, v) in sorted_ppr:
        logging.info("Object %d:  weight: %f  value: %f  ppr: %f" %(k, weight[k], value[k], v))


    # 每次贪心地装入性价比最高的物体，直到装不下为止
    current_weight, current_value, x = 0, 0, []
    for (k, v) in sorted_ppr:
        logging.debug("Object %d:  weight: %f  value: %f  ppr: %f" %(k, weight[k], value[k], v))
        if current_weight + weight[k] <= C:
            current_weight += weight[k]
            current_value += value[k]
            x.append(k)
        else:
            break

    return x, current_value

if __name__ == '__main__':
    data_file = 'data'
    x, value = greedy_algorithm(data_file)

    temp_str = ''
    for item in x:
        temp_str += str(item) + ' '

    logging.info('装入背包的物体为: %s  总价值为: %f' %(temp_str, value))
