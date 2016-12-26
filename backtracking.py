#!/usr/bin/env python
# coding=utf-8

from load_data import load_data
import logging, time

logging.basicConfig(format='%(levelname)s : %(message)s', level=logging.INFO)

def arr2str(arr):
    return ' '.join([str(item) for item in arr])

def backtracking(data_file):
    n, m, w, p = load_data(data_file)
    w, p = w[1:], p[1:]

    # 物体按价值重量比的非增顺序排序
    wp = [[i, w[i], p[i], p[i]/w[i]] for i in range(n)]
    sorted_wp = sorted(wp, key=lambda x : x[3], reverse=True)

    w_cur = p_cur = p_total = 0
    point = -1
    part_solu, full_solu = [0 for i in range(n)], [0 for i in range(n)]

    while True:
        
        # 求当前节点的上界
        w_est, p_est = w_cur, p_cur
        for i in range(point+1, n):
            if w_est + sorted_wp[i][1] <= m:
                w_est += sorted_wp[i][1]
                p_est += sorted_wp[i][2]
            else:
                p_est += (m-w_est)*sorted_wp[i][3]
                break
        logging.debug("\n\n当前节点的上界: %.1f    当前上限: %.1f" %(p_est, p_total))
        
       
        # 如果节点的上界大于当前上限，一直装入物品直到不能装入为止
        if p_est > p_total:
            
            for i in range(point+1, n):
                point += 1
                if w_cur + sorted_wp[i][1] <= m:
                    w_cur += sorted_wp[i][1]
                    p_cur += sorted_wp[i][2]
                    part_solu[point] = 1
                    
                elif point < n:
                    part_solu[point] = 0
                    break
            if point == n-1 and p_cur > p_total:
                p_total = p_cur
                full_solu = part_solu[:]    
          
        
            logging.debug("节点的上界大于当前上限")
            logging.debug("一直装入物品直到不能装入为止: %s" %arr2str(part_solu[:point+1]))
        
        # 如果节点的上界小于当前上限，将最近装入的一个物品抛弃掉 
        else:
            while ((point>=0) and (part_solu[point]==0)):
                point -= 1
            if (point < 0):
                logging.debug("背包的物体: %s" %arr2str(full_solu))
                logging.debug("背包的价值: %d" %p_total)
                logging.debug("程序结束")
                return p_total, full_solu
            else:
                part_solu[point] = 0
                w_cur -= sorted_wp[point][1]
                p_cur -= sorted_wp[point][2]
            logging.debug("节点的上界小于当前上限")
            logging.debug("抛弃最近装入的一个物品: %s" %arr2str(part_solu[:point+1]))

if __name__ == '__main__':
    begin = time.time()
    data_file = 'data'
    p, s1 = backtracking(data_file)
    end = time.time()
    logging.info('装入背包的总价值为: %d' %p)
    logging.info('Using %.4fs' %(end-begin))

