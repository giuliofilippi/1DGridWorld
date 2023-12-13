# imports
import numpy as np
from scipy.stats import truncnorm

# uniform dataset
def generate_uniform_dataset(num_samples, vector_length):
    dataset = []

    for _ in range(num_samples):
        # Uniform probability of -1
        prob = np.random.random()

        # Generate a random vector with -1 and 1
        random_vector = np.random.choice([-1, 1], size=vector_length, replace=True, p=[prob, 1-prob])

        # Calculate the proportion of -1 in the vector
        proportion_minus_one = np.sum(random_vector == -1) / vector_length

        # Determine the label based on the proportion
        label = np.ones(vector_length) if proportion_minus_one <= 0.5 else -1 * np.ones(vector_length)

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
        probability = truncated_normal.rvs()

        # Generate a random vector with -1 and 1 based on the sampled probability
        random_vector = np.random.choice([-1, 1], size=vector_length, replace=True, p=[probability, 1 - probability])

        # Calculate the proportion of -1 in the vector
        proportion_minus_one = np.sum(random_vector == -1) / vector_length

        # Determine the label based on the proportion
        label = np.ones(vector_length) if proportion_minus_one <= 0.5 else -1 * np.ones(vector_length)

        # Append the pair to the dataset
        dataset.append((random_vector, label))

    return dataset

# visualize truncated normal
'''
mean = 0.5
sigma = 0.1
lower_bound, upper_bound = 0, 1
a, b = (lower_bound - mean) / sigma, (upper_bound - mean) / sigma
truncated_normal = truncnorm(a, b, loc=mean, scale=sigma)
x = np.linspace(0,1,100)
dist=truncnorm(a, b,loc=0.5, scale = 0.1)
plt.plot(x, dist.pdf(x), 'k-', lw=2, label='normalised truncated Gaussian')
plt.show()
'''