import pandas as pd
import random
import numpy as np
import math


population_size = 10
x_lim = 100
y_lim = 100
period = 3 # days
random.seed(122)

population = pd.DataFrame(columns=['id', 'x', 'y', 'infection_status', 'connected_to', 'infected_by', 'symptomatic', 'moment_of_infection'])
for i in range(0,population_size):
    x = random.randint(1,x_lim)
    y = random.randint(1,y_lim)
    population = population.append({'id': i+1, 'x': x, 'y': y,  'infection_status': 0, 'connected_to': random.randint(1,3), 'infected_by':0, 'symptomatic':0, 'moment_of_infection':0}, ignore_index=True)


def euclid(col, refx, refy):
    #print (col.x, col.y, refx, refy)
    return (col.x - refx)**2 + (col.y - refy)**2

def infect(col):
    return col.x * col.y

def infect2(population, row, period):
    print (row)

    pop_s = population[population.infection_status == 0].reindex()
    dist = (pop_s[['x', 'y']] - np.array([row.x,row.y])).pow(2).sum(1).pow(0.5)
    prob = 1-1/(1+np.exp(-0.5 * dist + 35/2))
    event = random.randint(0,100)/100
    print (prob)
    event_bool_list = prob > event
    print (list(event_bool_list))
    indices = (np.where(list(event_bool_list))[0])
    print (event)
    #indices = list((dist[dist < 35]).keys())
    print (dist)
    print (indices)
    pop_new = population
    pop_new.loc[indices, 'infection_status'] = 1
    pop_new.loc[indices, 'infected_by'] = row.id
    print ('infected by:')
    print (pop_new.loc[indices, 'infected_by'])# = row.id

    pop_new.loc[indices, 'moment_of_infection'] = period

    print (pop_new)
    return (pop_new)

#population[['x','y']] = population[['x','y']].apply(euclid, axis=1)

#print (population)
time_sim = []
time_sim.append(population)

#print(population[['x','y']].apply(euclid, args=(34,35), axis=1))
random_infection_index = random.randint(0,population_size-1)
population.loc[random_infection_index,'infection_status'] = 1 # seed random initial infection
population.loc[random_infection_index,'infected_by'] = population.iloc[random_infection_index]['id']
print (population)

infection_count = []
for time in range(0, period):
    population_newly_infected = population[(population.infection_status == 1) & (population.moment_of_infection >= period-1)].reindex(axis=1)
    print (population_newly_infected)
    for index, row in population_newly_infected.iterrows():
        population_newly_infected = infect2(population, row, period)
    infection_count.append(population_newly_infected['infection_status'].sum())
print ('-- End --')
print (infection_count)

    #print (population)
#     for index, row in population.iterrows():
#
#     time_sim.append()
