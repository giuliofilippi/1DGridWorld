# sys
import sys
sys.path.append('code')

# base imports
import numpy as np
from torch import nn

# class imports
from classes import Lattice
from functions import random_initial_config
from display import render

# Lattice
init_conf = random_initial_config(101, 0.5, 1)
lattice = Lattice(101, 3, init_conf)

# Dummy neural network model for testing
dummy_model = nn.Sequential(
    nn.Linear(7, 7),
    nn.Sigmoid(),
    nn.Linear(7, 1)
)

# Perform a forward pass
lattice.forward_pass(dummy_model, num_iter=100)
print(lattice.memory)
render(lattice.memory)