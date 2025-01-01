########################################################
#
# Practice Search Algorithms 2
#
########################################################

########################################################
# Import
########################################################

from utils_practice_2 import *
import math
import random



# Add your imports here if used






################################################################
# 1. Genetic Algorithm
################################################################


def genetic_algorithm(problem, f_thres, ngen=1000):
    """
    Returns a tuple (i, sol) 
    where
      - i  : number of generations computed
      - sol: best chromosome found
    """
    pass

  

################################################################
# 2. NQueens Problem
################################################################


class NQueensProblem(GeneticProblem):
    def __init__(self, n, g_bases, g_len, m_prob):
        pass
    
    def init_population(self):
        pass
 
    def next_generation(self, population):
        pass

    def mutate(self, chrom):
        pass
    
    def crossover(self, chrom1, chrom2):
        pass

    def fitness_fn(self, chrom):
        pass
    
    def select(self, m, population):
        pass
    
    def fittest(self, population, f_thres=None):
        pass




        
################################################################
# 3. Function Optimaization f(x,y) = x sin(4x) + 1.1 y sin(2y)
################################################################


class FunctionProblem(GeneticProblem):
    def __init__(self, n, g_bases, g_len, m_prob):
        pass

    def init_population(self):
        pass

    def next_generation(self, population):
        pass
        
    def mutate(self, chrom):
        pass
        
    def crossover(self, chrom1, chrom2):
        pass
    
    def fitness_fn(self, chrom):
        pass
    
    def select(self, m, population):
        pass

    def fittest(self, population, f_thres=None):
        pass


