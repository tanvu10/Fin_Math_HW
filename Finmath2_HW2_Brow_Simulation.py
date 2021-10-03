import numpy as np
from numpy import random
import matplotlib.pyplot as plt
from scipy.stats import norm


#simulation for 1 k_step playing
def simulation(step):
    random_list = []
    for i in range(step+1):
        if i == 0:
            random_list.append(0)
        else:
            random_list.append(0 + random.normal(loc = 0, scale = 1, size =1 ) + random_list[i-1])
    return random_list

v1 = simulation(1000)
plt.plot(v1)
plt.show()


#n time playing simulation to calculate probability
def proba_k_step(step, time_simu):
    proba_list = []
    for i in range(time_simu):
        proba_list.append(simulation(step)[-1])
    plt.hist(np.array(proba_list), bins = 30)
    plt.show()
    proba = len([j for j in proba_list if j >0])/len(proba_list)
    print(proba)

#probability from simulation
proba_k_step(10, 100000)
#probability from formula:
# print(1- norm.cdf(-3/np.sqrt(10)))