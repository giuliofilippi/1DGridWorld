# imports
import numpy as np

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

    def __init__(self, length, initial_state=None):
        """
        Initializes a new instance of the Lattice class.

        Parameters:
        - length: Length of the lattice.
        - initial_state: Initial state of the lattice (optional).
        """
        self.length = length
        self.state = np.ones(length, dtype=int)  # You can modify the dtype according to your needs

        if initial_state is not None:
            if len(initial_state) == length:
                self.state = np.array(initial_state)
            else:
                raise ValueError("Length of initial_state must match the length of the lattice.")
