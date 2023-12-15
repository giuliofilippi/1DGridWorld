# base imports
import numpy as np
import torch.nn as nn

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
    
    # vectors
    vectors = []

    # Calculate the number of -1 entries in each vector
    num_minus_one = int(p * length)

    # Generate random vectors
    for _ in range(size):
        vec = np.ones(length)
        indices = np.random.choice(range(length), size=num_minus_one, replace=False)
        vec[indices] = -1
        vectors.append(vec)

    return vectors if size > 1 else vectors[0]