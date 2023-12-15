# imports
import numpy as np
from scipy.stats import truncnorm

# functions imports
from functions import random_initial_config

# uniform dataset
def generate_uniform_dataset(num_samples, vector_length):
    dataset = []

    for _ in range(num_samples):
        # Uniform probability of -1
        prob = np.random.random()
        # Generate a random vector with -1 and 1
        random_vector = random_initial_config(vector_length, prob)
        # Determine the label based on the proportion
        label = np.ones(vector_length) if prob <= 0.5 else -1 * np.ones(vector_length)
        # Append the pair to the dataset
        dataset.append((random_vector, label))

    return dataset

# truncated normal dataset
def generate_normal_dataset(num_samples, vector_length, mean=0.5, sigma=0.1):
    dataset = []

    # Set up the truncated normal distribution
    lower_bound, upper_bound = 0, 1
    a, b = (lower_bound - mean) / sigma, (upper_bound - mean) / sigma
    truncated_normal = truncnorm(a, b, loc=mean, scale=sigma)

    for _ in range(num_samples):
        # Sample probability p from the truncated normal distribution
        prob = truncated_normal.rvs()
        # Generate a random vector with -1 and 1
        random_vector = random_initial_config(vector_length, prob)
        # Determine the label based on the proportion
        label = np.ones(vector_length) if prob <= 0.5 else -1 * np.ones(vector_length)
        # Append the pair to the dataset
        dataset.append((random_vector, label))

    return dataset