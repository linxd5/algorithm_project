#!/usr/bin/env python
# coding=utf-8

# 输入: 物体的个数n，背包的容量m，物体的重量w[]和物体的价值p[]
# 输出：装入背包的物体 x[]，背包中物体的价值 v

# 物品编号：1-n

from load_data import load_data
import logging, time
from heapq import heappop, heappush

logging.basicConfig(format='%(levelname)s : %(message)s', level=logging.INFO)


def bb_algorithm(data_file):
    n, m, w, p = load_data(data_file)

    # 把物品按照性价比进行排序
    wp = [[i, w[i], p[i], p[i]/(w[i]*1.0)] for i in range(1, n+1)]
    sorted_wp = sorted(wp, key=lambda x : x[3], reverse=True)

    """
    分界限界的每一步都是选择放入或者不放入某个物体
    假设现在进行到第 j 步。
    如果背包被塞爆了，那么上界为0，也就是说这个解是无效的了。
    如果背包没有被塞满，我们的上界是这样计算的：
        往背包中依次放入剩下的物品中性价比最高的物品，直到不能再放入下一个为止。
        这时候，我们放入下一个物品的一部分，这就是在当前状态下背包所能装入物品的最大价值了。
    """
    def bound(curr_w, curr_p, j):
        if curr_w > m:
            return 0
        else:
            temp_w, temp_p = curr_w, curr_p
            while j < n and temp_w + sorted_wp[j][1] <= m:
                temp_w, temp_p, j = temp_w + sorted_wp[j][1], temp_p + sorted_wp[j][2], j + 1
            if j < n:
                temp_p += (m - temp_w) * sorted_wp[j][2] / (sorted_wp[j][1] * 1.0)
            return temp_p


    h = [(0, 0, 0, -1, [])]  # 分别代表上界、重量、价值、深度和加入节点集合
    while h:
        f_b, f_w, f_p, f_j, f_s1  = heappop(h)

        if f_j == n-1:
            return f_p, f_s1

        # 不加入 sorted_ppr 中的第 j+1 个节点
        not_w, not_p, not_j = f_w, f_p, f_j+1
        not_b, not_s1 = bound(not_w, not_p, not_j+1), f_s1
        heappush(h, (-not_b, not_w, not_p, not_j, not_s1))

        # 加入 sorted_ppr 中的第 j+1 个节点 
        in_w, in_p, in_j = f_w + sorted_wp[f_j+1][1], f_p + sorted_wp[f_j+1][2], f_j + 1
        in_b, in_s1 = bound(in_w, in_p, in_j+1), f_s1 + [sorted_wp[f_j+1][0]]
        heappush(h, (-in_b, in_w, in_p, in_j, in_s1))


if __name__ == '__main__':
    begin = time.time()
    data_file = 'data'
    p, s1 = bb_algorithm(data_file)
    end = time.time()
    print('++++ Max: ', p)
    # print('++++ s1: ', s1)
    print('Using %.4fs' %(end-begin))


