# base imports
import numpy as np
import torch

# function imports
from functions import local_matrix, bit_map

# Lattice class
class Lattice:
    """
    Represents a 1D lattice environment.

    Attributes:
    - length: Length of the lattice.
    - state: 1D array representing the state of the lattice.

    Methods:
    - __init__: Initializes a new instance of the Lattice class.
    """

    def __init__(self, length, radius, initial_state=None):
        """
        Initializes a new instance of the Lattice class.

        Parameters:
        - length: Length of the lattice.
        - initial_state: Initial state of the lattice (optional).
        """
        self.length = length
        self.radius = radius
        self.state = np.ones(length, dtype=int)
        self.memory = [self.state]

        if initial_state is not None:
            if len(initial_state) == length:
                self.state = np.array(initial_state)
                self.memory = [self.state]
            else:
                raise ValueError("Length of initial_state must match the length of the lattice.")
            
    def forward_pass(self, model, num_iter):
        """
        Perform a forward pass through a model for a specified number of iterations.

        Parameters:
        - length (int): The length of the input vector.
        - radius (int): The radius for extracting the local neighborhood.
        - model (torch.nn.Module): The neural network model.
        - num_iter (int): The number of iterations to perform.

        Returns:
        None
        """
        for _ in range(num_iter):
            local_data_mat = local_matrix(self.state, radius=self.radius)
            new_state = np.zeros(self.length)
            for i in range(self.length):
                # input must be torch tensor
                input = torch.tensor(local_data_mat[i]).float()
                # threshold at 0 and map to -1, 1
                new_state[i] = bit_map(model(input) > 0) 
            self.memory.append(new_state)
            self.state = new_state

