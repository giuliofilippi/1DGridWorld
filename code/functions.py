# base imports
import numpy as np
import torch
import torch.nn as nn

# map
def bit_map(x):
    """
    Maps binary values to {-1, 1}.

    Parameters:
    - x: Binary value (0 or 1) to be mapped.

    Returns:
    - int: Mapped value, -1 if x is 0, 1 if x is 1.

    Raises:
    - ValueError: If x is not a valid binary value (neither 0 nor 1).
    """
    if x == 0:
        return -1
    elif x == 1:
        return 1
    else:
        raise ValueError("Invalid binary value. Expected 0 or 1.")

# get local data matrix
def local_matrix(vector, radius):
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

# random initial config
def random_initial_config(length, p, size=1):
    """
    Generates random vectors with a specified length and proportion of -1 entries.

    Parameters:
    - length (int): Length of the random vectors.
    - proportion_minus_one (float): Proportion of -1 entries in the vectors. Should be between 0 and 1.
    - num_vectors (int): Number of random vectors to generate. Default is 1.

    Returns:
    - numpy.ndarray or list of numpy.ndarray: Random vectors with the specified properties.
    """
    if not (0 <= p <= 1):
        raise ValueError("Proportion must be between 0 and 1.")

    # Calculate the number of -1 entries in each vector
    num_minus_one = int(p * length)

    # Generate random vectors
    vectors = [np.random.choice([-1, 1], size=length, replace=True, p=[p, 1 - p])
               for _ in range(size)]

    return vectors if size > 1 else vectors[0]