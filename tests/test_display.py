# sys
import sys
sys.path.append('code')

# base imports
import numpy as np


# class imports
from classes import Lattice
from display import render
from functions import random_initial_config

# lattice viz
initial_state = random_initial_config(101, 0.5, 1)
print (initial_state)
l = Lattice(101, 5, initial_state=initial_state)
render([l.state]*300)