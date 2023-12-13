# base imports
import numpy as np
import torch
import torch.nn as nn

# get local data matrix
def local_neighborhood_matrix(vector, radius):
    """
    Extracts the local neighborhood of each element in a vector with periodic boundary conditions.

    Parameters:
    - vector (numpy.ndarray): The input vector.
    - radius (int): The radius of the local neighborhood.

    Returns:
    - numpy.ndarray: A 2D array where each row corresponds to a neighborhood.
    """
    length = len(vector)
    neighborhoods = []

    for i in range(length):
        # Create an index array for the local neighborhood
        neighbors_indices = (np.arange(-radius, radius + 1) + i) % length

        # Extract values from the vector using the index array
        neighborhood_values = vector[neighbors_indices]

        # append to list of neighbourhoods
        neighborhoods.append(neighborhood_values)

    return np.array(neighborhoods)