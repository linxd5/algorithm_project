#!/usr/bin/env python
# coding=utf-8

# 输入: 物体的个数n，背包的容量m，物体的重量w[]和物体的价值p[]
# 输出：装入背包的物体 x[]，背包中物体的价值 v

# 物品编号：1-n

from load_data import load_data
import logging, time
import random

logging.basicConfig(format='%(levelname)s : %(message)s', level=logging.INFO)

n, m, w, p = load_data('data')
w, p = w[1:], p[1:]

pop_num = 1000   # 种群中个体的数量
population, fitness = [], []
best_indi, best_fitn = [], 0   # 保留最好的个体，使得结果至少不会越来越差
epoch = 30
crossover_prob = 0.5
mutation_prob = 0.1


def cal_value(individual):
    temp_sum = 0
    for i in range(n):
        temp_sum += individual[i] * p[i]
    return temp_sum

def cal_weight(individual):
    temp_sum = 0
    for i in range(n):
        temp_sum += individual[i] * w[i]
    return temp_sum


def max_fitness():
    temp_max, temp_num = 0, 0
    for i in range(pop_num):
        if cal_value(population[i]) > temp_max:
            temp_max = cal_value(population[i])
            temp_num = i
            
    return temp_max, temp_num

def initial_pop():
    
    global best_fitn
    global best_indi
    temp_num = 0
    while True:
        temp_individual = [round(random.uniform(0, 1), 0) for i in range(n)]
        temp_weight = cal_weight(temp_individual)
        temp_value = cal_value(temp_individual)
        if temp_weight <= m:
            population.append(temp_individual)
            fitness.append(temp_value)
            
            if temp_value > best_fitn:
                best_indi = temp_individual
                best_fitn = temp_value
            temp_num += 1
            if temp_num >= pop_num:
                break


def select():
    
    global population
    global fitness
    global best_fitn
    global best_indi
    
    fitness_sum, upper_bound = 0, []
    for i in range(pop_num):
        fitness_sum += fitness[i]
        if fitness[i] > best_fitn:
            best_fitn = fitness[i]
            best_indi = population[i]
    upper_bound.append(fitness[0]/fitness_sum)
    for i in range(1, pop_num):
        upper_bound.append(upper_bound[i-1]+fitness[i]/fitness_sum)
        
    # 依据轮盘度算法产生新个体
    new_population, new_fitness = [], []
    new_population.append(best_indi)
    new_fitness.append(best_fitn)
    for i in range(1, pop_num):
        temp_num = random.uniform(0, 1)
        for j in range(pop_num):
            if temp_num < upper_bound[j]:
                new_population.append(population[j])
                new_fitness.append(fitness[j])
                break
    
    population, fitness = new_population[:], new_fitness[:]
                


def crossover():
    for i in range(pop_num):
        if random.uniform(0, 1) <= crossover_prob:
            while True:
                j = random.randint(0, pop_num-1)
                point = random.randint(0, n-1)
                temp_indi1 = population[i][:point] + population[j][point:]
                temp_indi2 = population[j][:point] + population[i][point:]
                if cal_weight(temp_indi1) <= m and cal_weight(temp_indi2) <= m:
                    population[i], population[j] = temp_indi1[:], temp_indi2[:]
                    fitness[i], fitness[j] = cal_value(population[i]), cal_value(population[j])
                    break
            
        
def mutation():
    for i in range(pop_num):
        if random.uniform(0, 1) <= mutation_prob:
            point = random.randint(0, n-1)
            temp_indi = population[i][:]
            temp_indi[point] = 1 - temp_indi[point]
            if cal_weight(temp_indi) <= m:
                population[i] = temp_indi[:]
                fitness[i] = cal_value(temp_indi)


def genetic_algorithm():

    # 产生初始种群
    initial_pop()

    for i in range(epoch):
        select()
        crossover()
        mutation()

        temp_max, temp_num = max_fitness()
        print(temp_max)
    
    temp_max, temp_num = max_fitness()

    return temp_max, population[temp_num]

    

if __name__ == '__main__':
    begin = time.time()
    temp_max, temp_indi = genetic_algorithm()
    end = time.time()
    print('++++ Max: ', temp_max)
    print('Using %.4fs' %(end-begin))


