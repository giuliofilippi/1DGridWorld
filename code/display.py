# imports
import matplotlib.pyplot as plt

# render
def render(matrix):
    """
    Visualizes a 2D lattice matrix.

    Parameters:
    - matrix: 2D matrix representing the lattice.
    """
    plt.imshow(matrix, cmap='gray', vmin=-1, vmax=1)
    plt.axis('off')  # Turn off the axes
    plt.show()

    plt.show()