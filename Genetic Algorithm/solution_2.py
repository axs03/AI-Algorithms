#!/usr/bin/env python
# coding: utf-8


# ## Imports


from utils_2 import *
import math
import random
import bisect


# ## Genetic Algorithm

# In[9]:


def genetic_algorithm(problem, f_thres, ngen=1000):
    """
    Returns a tuple (i, sol) 
    where
      - i  : number of generations computed
      - sol: best chromosome found
    """
    population = problem.init_population()
    sol = problem.fittest(population, f_thres)
    if sol is not None:
        return 0, sol
    
    for i in range(ngen):
        population = problem.next_generation(population)
        sol = problem.fittest(population, f_thres)

        if sol is not None:
              return i, sol
        
    sol = problem.fittest(population)
    return ngen, sol


# ## N-Queens Problem

# In[4]:


class NQueensProblem(GeneticProblem):
    def __init__(self, n, g_bases, g_len, m_prob):
        try:
            self.n = n # population size
            self.g_bases= list(g_bases) # domain of each gene in chromosome
            if g_len == len(g_bases):
                self.g_len = g_len # length of chromosome
            self.m_prob = m_prob # mutation prob
            
        except ValueError as ve:
            print(f"Length does not match: {ve}")          
     
    
    def init_population(self):
        return [tuple(random.randrange(0, self.g_len) for _ in range(self.g_len)) for _ in range(self.n)]
            
 
    def next_generation(self, population):
        new_population = self.init_population()

        crossed = [self.crossover(new_population[chrom], population[chrom]) for chrom in range(0, self.n)]
        new_generation = [self.mutate(crossed[chrom]) for chrom in range(0, self.n)]
            
        return new_generation


    def mutate(self, chrom):
        chrom = list(chrom)
        p = random.uniform(0, 1)

        if p > self.m_prob:
            return tuple(chrom)
        
        i = random.randint(0, self.g_len - 1) # random index, -1 makes sure g_len is exlusive of range

        chrom[i] = self.g_bases[i]

        return tuple(chrom)
    
    

    def crossover(self, chrom1, chrom2):
        chrom1, chrom2 = list(chrom1), list(chrom2)
        i = random.randint(0, self.g_len - 1) # random index, -1 makes sure g_len is exlusive of range

        offspring = chrom1[:i] + chrom2[i:]
        return tuple(offspring)


    def fitness_fn(self, chrom):
        fitness = self.__non_attacking_pairs(chrom)
        return fitness if fitness >= 0 else 0

        
    def __non_attacking_pairs(self, chrom):
        # Helper for finding if queens have conflict
        def __conflict(row1, col1, row2, col2):
            return row1 == row2 or col1 == col2 or abs(row1-row2) == abs(col1-col2)
        
        attacking_pairs = 0
        max_fitness = math.comb(self.g_len, 2) # for fitness function

        # checking all pairs
        for c1 in range(0,self.g_len):
            r1 = chrom[c1]
            for c2 in range(c1 + 1, self.g_len):
                r2 = chrom[c2]
                
                if __conflict(r1, c1, r2, c2):
                    attacking_pairs += 1
        
        return max_fitness - attacking_pairs # non attacking pairs
    
    
    def select(self, m, population):
        res = []

        # used for prob of selection of chromosome
        population_fitness = sorted([self.fitness_fn(chrom_fitness) for chrom_fitness in population]) # sorted prob distr list, and its sum
        population_fitness_sum = sum(population_fitness)

        pop_prob_distr = [] # normal prob distr list, dont really need this but use for debugging
        pop_cum_prob_distr = [] # cumulative distr list

        cumulative_sum = 0
        for fitness in population_fitness:
            chrom_probability = fitness / population_fitness_sum
            pop_prob_distr.append(chrom_probability)

            cumulative_sum += chrom_probability
            pop_cum_prob_distr.append(cumulative_sum)

        if pop_cum_prob_distr[-1] != 1:
            return []
        
        for _ in range(0, m):
            p = random.uniform(0, 1)
            idx = bisect.bisect_left(pop_cum_prob_distr, p) # insertion index
            res.append(population[idx])

        return res


    def fittest(self, population, f_thres=None):
        fitnesses = list(map(self.fitness_fn, population))
        if f_thres == None:
            max_idx =  max(range(0, len(fitnesses)), key=fitnesses.__getitem__)
            return population[max_idx]
        
        elif f_thres != None:
            # temp = []
            # for fit in range(0, len(fitnesses)):
            #     if fitnesses[fit] >= f_thres:
            #         temp.append(fit)
                
            # max_idx = max(temp, key=fitnesses.__getitem__)
            
            max_idx = max((fit for fit in range(len(fitnesses)) if fitnesses[fit] >= f_thres), key=fitnesses.__getitem__, default=None)
            if max_idx != None:
                return population[max_idx]
            
        return None

        


# In[5]:


# p  = NQueensProblem(5, range(8), 8, 0.2)

# population = [(5,4,0,2,1,1,4,3), (1,4,5,2,0,1,5,7), (0,2,7,4,6,0,4,5), (6,3,5,5,2,3,1,0), (6,5,1,7,7,2,2,3)]


# map1 = list(map(p.fitness_fn, population))

# print(map1)

# print(p.fittest(population, 23))


# print(p.select(0, population))
# print(p.select(2, population))
# print(p.select(10, population))



# print(p.mutate((4,4,4,2,6,6,4,3)))





# ## Function Optimaization f(x,y) = x sin(4x) + 1.1 y sin(2y)

# In[6]:


class FunctionProblem(GeneticProblem):
    def __init__(self, n, g_bases, g_len, m_prob):
        try:
            self.n = n
            if g_len == 2:
                self.g_len = 2

            self.g_bases = g_bases
            self.m_prob = m_prob

        except ValueError as ve:
            print(f"There is an error: {ve}")


    def init_population(self):
        return [tuple(random.randrange(0, self.g_len) for _ in range(self.g_len)) for _ in range(self.n)]


    def next_generation(self, population):
        population = sorted(population, key=self.fitness_fn)
        best_half = population[:len(population) // 2] # getting the front half i.e the 'better half'

        next_half = []
        for _ in range(0, len(best_half)):
            crossed_chrom = self.crossover(random.choice(best_half), random.choice(best_half))
            mutated_chrom = self.mutate(crossed_chrom)
            next_half.append(mutated_chrom)

        return best_half + next_half
        
        
    def mutate(self, chrom):
        chrom = list(chrom)
        p = random.uniform(0, 1)

        if p > self.m_prob:
            return tuple(chrom)
        
        i = random.randint(0, self.g_len - 1) # random index, -1 makes sure g_len is exlusive of range

        # replace chrom[i] with rand floating point number
        chrom[i] = random.uniform(0, self.g_bases[i])

        return tuple(chrom)
        

    def crossover(self, chrom1, chrom2):
        chrom1, chrom2 = list(chrom1), list(chrom2)
        i = random.randint(0, self.g_len - 1) # choosing x or y to interpolate
        alpha = random.uniform(0, 1) # rand floating point alpha

        # choosing to interpolate component
        interpolated_component = ((1 - alpha) * chrom1[i]) + (alpha * chrom2[i])

        offspring = chrom1[:] # copy of chrom1
        offspring[i] = interpolated_component # changing to interpolated component

        return tuple(offspring)

    
    def fitness_fn(self, chrom):
        fitness = (chrom[0] * math.sin(4 * chrom[0])) + (1.1 * chrom[1] * math.sin(2 * chrom[1]))
        return fitness
    

    def select(self, m, population):
        population_ranked = sorted(population, key=self.fitness_fn)
        # population_ranked = sorted([self.fitness_fn(chrom_fitness) for chrom_fitness in population])

        element_prob_distr = [self.__calculate_prob_distr(chrom_idx, len(population_ranked)) for chrom_idx in range(1, len(population_ranked) + 1)]
        cumulative_prob_distr = [sum(element_prob_distr[:i]) for i in range(1, len(element_prob_distr) + 1)]

        res = []
        # Selecting m chromosomes 
        for _ in range(0, m):
            p = random.uniform(0, 1)
            idx = bisect.bisect_left(cumulative_prob_distr, p) # insertion index
            res.append(population[idx])

        return res


    # Helper for select
    def __calculate_prob_distr(self, rank, total):
        sum_idxs = sum(range(0, total + 1))

        return ((total + 1) - rank) / sum_idxs
        

    def fittest(self, population, f_thres=None):
        fitnesses = list(map(self.fitness_fn, population))
        if f_thres == None:
            min_idx =  min(range(0, len(fitnesses)), key=fitnesses.__getitem__) # using min since lowest fitness is best?
            return population[min_idx]
        
        elif f_thres != None:
            # temp = []
            # for fit in range(0, len(fitnesses)):
            #     if fitnesses[fit] >= f_thres:
            #         temp.append(fit)
                
            # max_idx = max(temp, key=fitnesses.__getitem__)
            
            min_idx = max((fit for fit in range(len(fitnesses)) if fitnesses[fit] <= f_thres), key=fitnesses.__getitem__, default=None)
            
            if min_idx != None:
                return population[min_idx]
            
        return None


# In[7]:


# p = FunctionProblem(6, (5,5), 2, 0.2)

# population = [(2.066938780637087, 1.650998608284147), (0.7928608069345605, 1.678831697303177), (3.685189771001436, 1.4280879354988107),(3.860362372295962, 1.0789325520768145), (4.673003350118171, 4.780722998076655),(2.5701433643372247, 4.9078727479819335)]
# population = [(2.066938780637087, 1.650998608284147),
# (3.860362372295962, 1.0789325520768145),
# (2.5701433643372247, 4.9078727479819335),
# (4.673003350118171, 4.780722998076655),
# (3.685189771001436, 1.4280879354988107),
# (0.7928608069345605, 1.678831697303177)]

# print(list(map(p.fitness_fn, population)))

# best_half = list(map(p.fitness_fn, population))
# print(best_half)

# print(p.fittest(population, f_thres=-5.0))

# p.select(2, population)


# In[ ]:


# p = NQueensProblem(10, (1,2,3,4), 4, 0.2)
# i, sol = genetic_algorithm(p, f_thres=6, ngen=1000)

# p = NQueensProblem(100, (0,1,2,3,4,5,6,7), 8, 0.2)
# i, sol = genetic_algorithm(q, f_thres=28, ngen=1000)

# p = FunctionProblem(12, (10,10), 2, 0.2)
# i, sol = genetic_algorithm(p, f_thres=-18, ngen=1000)

# p = FunctionProblem(20, (10,10), 2, 0.2)
# i, sol = genetic_algorithm(p, f_thres=-18.5519, ngen=1000)

# print(i, sol)
# print(p.fitness_fn(sol))


# In[ ]:




