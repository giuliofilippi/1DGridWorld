# imports
import matplotlib.pyplot as plt
import numpy as np

# render
def render(matrix):
    """
    Visualizes a 2D lattice matrix with borders.

    Parameters:
    - matrix: 2D matrix representing the lattice.
    """
    matrix = np.array(matrix)

    # Create a new figure and axis
    fig, ax = plt.subplots()

    # Set the borders without ticks and tick labels
    for spine in ax.spines.values():
        spine.set_visible(True)
        spine.set_linewidth(2)  # Set the border linewidth to your preference

    # Plot the matrix using imshow
    ax.imshow(matrix, cmap='gray', vmin=-1, vmax=1)

    # Turn off the axes ticks and labels
    ax.set_xticks([])
    ax.set_yticks([])

    plt.show()


    plt.show()