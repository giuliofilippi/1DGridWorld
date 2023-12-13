# sys
import sys
sys.path.append('code')

# base imports
import numpy as np

# class imports
from classes import Lattice
from display import render

#f
def f(x):
    if x == 0:
        return -1
    else:
        return 1

# lattice viz
initial_state = (np.random.random(101)>0.5)*1
initial_state = [f(x) for x in initial_state]
print (initial_state)
l = Lattice(101, initial_state=initial_state)
render([l.state]*300)