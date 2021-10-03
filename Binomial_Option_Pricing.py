import numpy as np
import pandas as pd
import math
def Bino_Tree(S, u, d, period):
    ''
    'S: initial price at time 0'
    'u: up factor'
    'd: down factor'
    'period: number of partition period, not that this is also the dimension of price matrix, \'' \
    'real period = arg(period) - 1'
    sample_tree = np.zeros([period, period])
    for i in range(period):
        for j in range(i+1): #run to i (including i)
            sample_tree[i][j] = S * (u**j) * (d**(i-j))
    return sample_tree

price_tree = Bino_Tree(S =20 , u = 1.1, d= 0.9,period= 3)
# print(price_tree)

def Bino_Pricing(tree_price, u, d ,delta_t , r, K, type = True):
    ''
    'tree price'
    'u: up factor'
    'd: down factor'
    'delta_t = real_period/n'
    'n: partition num'
    'r: annual risk free rate'
    'K: strike price'
    'true: call option, false: put option'
    neural_proba = (math.exp(r*delta_t) - d)/ (u-d)
    neural_proba = round(neural_proba,4)
    dimension = len(tree_price[0])
    option_tree = np.zeros([dimension, dimension])
    if type == True: #true : call option
        option_tree[dimension-1] = [max(tree_price[dimension-1][j] - K,0) for j in range(dimension)]
    else:            #false: put option
        option_tree[dimension - 1] = [max(K-tree_price[dimension - 1][j], 0) for j in range(dimension)]
    for i in reversed(range(dimension-1)): #from bottom to top #excluding last row
        for j in range(i+1): #including i index
            option_tree[i][j] = ((1-neural_proba)*option_tree[i+1][j] + (neural_proba)*option_tree[i+1][j+1])/math.exp(r*delta_t)
            option_tree[i][j] = round(option_tree[i][j], 4)
    return option_tree

# print(Bino_Pricing(tree_price=price_tree , u = 1.1,d = 0.9, delta_t=0.25, r = 0.12, K= 21, type = False))


def Bino_Tree_CRR(S, sigma, delta_t , period ):
    ''
    'S: initial price at time 0'
    'u: up factor'
    'd: down factor'
    'period: number of partition period, not that this is also the dimension of price matrix, \'' \
    'real period = arg(period) - 1'
    'n: partition num'
    'delta_t = real_period/n'
    'sigma: annual volatilies'
    u = math.exp(sigma*delta_t)
    d = math.exp(-sigma*delta_t)
    sample_tree = np.zeros([period, period])
    for i in range(period):
        for j in range(i+1): #run to i (including i)
            sample_tree[i][j] = S * (u**j) * (d**(i-j))
    return sample_tree


def Bino_Pricing_CRR(tree_price, sigma, delta_t, r, K, type=True):
    ''
    'tree price'
    'sigma: annual volatilities'
    'delta_t = real_period/n'
    'n: partition num'
    'r: annual risk free rate'
    'K: strike price'
    'true: call option, false: put option'
    u = math.exp(sigma*delta_t)
    print(u)
    d = math.exp(-sigma*delta_t)
    print(d)
    neural_proba = (math.exp(r * delta_t) - d) / (u - d)
    neural_proba = round(neural_proba, 4)
    print(neural_proba)
    dimension = len(tree_price[0])
    option_tree = np.zeros([dimension, dimension])
    if type == True:  # true : call option
        option_tree[dimension - 1] = [max(tree_price[dimension - 1][j] - K, 0) for j in range(dimension)]
    else:  # false: put option
        option_tree[dimension - 1] = [max(K - tree_price[dimension - 1][j], 0) for j in range(dimension)]
    for i in reversed(range(dimension - 1)):  # from bottom to top #excluding last row
        for j in range(i + 1):  # including i index
            option_tree[i][j] = ((1 - neural_proba) * option_tree[i + 1][j] + (neural_proba) * option_tree[i + 1][j + 1]) / math.exp(r * delta_t)
            option_tree[i][j] = round(option_tree[i][j], 4)
    return option_tree

#note: period: dimension cua matrix, real_period = arg(period) -1
tree_price_CRR = (Bino_Tree_CRR(S = 30 , sigma = 0.3, delta_t= 1, period = 4))
print(tree_price_CRR)
pricing = Bino_Pricing_CRR(tree_price=tree_price_CRR, sigma= 0.3, delta_t=1 , r=0.05, K =29, type = False )
print(pricing)