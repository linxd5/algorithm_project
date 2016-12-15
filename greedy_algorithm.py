#!/usr/bin/env python
# coding=utf-8

# 输入: 物体的个数n，背包的容量m，物体的重量w[]和物体的价值p[]
# 输出：装入背包的物体 x[]，背包中物体的价值 v

from load_data import load_data
import operator, logging, time

logging.basicConfig(format='%(levelname)s : %(message)s', level=logging.INFO)

def greedy_algorithm(data_file):
    n, m, w, v = load_data(data_file)

    # 计算每个物体的性价比并按照由大到小的顺序进行排序
    ppr = {}
    for i in range(1, n+1):
        ppr[i] = v[i] / w[i]
    sorted_ppr = sorted(ppr.items(), key=operator.itemgetter(1), reverse=True)

    logging.info("一共有%d个物品，背包重量为%d" %(n, m))

    # 每次贪心地装入性价比最高的物体，直到装不下为止
    current_w, current_v, x = 0, 0, []
    for (k, ppr) in sorted_ppr:
        logging.debug("Object %d:  w: %d  v: %d  ppr: %.4f" %(k, w[k], v[k], ppr))
        if current_w + w[k] <= m:
            current_w += w[k]
            current_v += v[k]
            x.append(k)

    return x, current_v

if __name__ == '__main__':
    begin = time.time()
    data_file = 'data'
    x, v = greedy_algorithm(data_file)
    end = time.time()

    temp_str = ''
    for item in x:
        temp_str += str(item) + ' '

    # logging.info('装入背包的物体为: %s  总价值为: %d' %(temp_str, v))
    logging.info('装入背包的总价值为: %d' %v)
    logging.info('Using %.4fs' % (end-begin))
