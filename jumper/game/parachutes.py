class Parachutes():
    """
    Returns a picture of a parachute based upon the number of incorrect guesses made.

    Attributes:
        parachutes (list): A list of the parachute pictures.
    """

    def __init__(self):
        """
        Constructs a new Parachutes class instance.

        Args:
            self (Parachutes): An instance of Parachutes.
        """
        self._parachutes = [
"""
  ___
 /___\\
 \\   /
  \\ /
   O
  /|\\
  / \\

^^^^^^^
""",
"""
  _ _
 /___\\
 \\   /
  \\ /
   O
  /|\\
  / \\

^^^^^^^
""",
"""
     
 /___\\
 \\   /
  \\ /
   O
  /|\\
  / \\

^^^^^^^
""",
"""

  ___
 \\   /
  \\ /
   O
  /|\\
  / \\

^^^^^^^
""",
"""

  _ _ 
 \\   /
  \\ /
   O
  /|\\
  / \\

^^^^^^^
""",
"""


 \\   /
  \\ /
   O
  /|\\
  / \\

^^^^^^^
""",
"""



  \\ /
   O
  /|\\
  / \\

^^^^^^^
""",
"""




   X
  /|\\
  / \\

^^^^^^^
"""]

    def choose_parachute(self, parachute):
        """
        Returns the parachute drawing based upon the number of incorrect guesses made.

        Args:
            self (Parachutes): An instance of Parachutes.
            parachute (int): The number of incorrect guesses made.
        """
        return self._parachutes[parachute - 1]