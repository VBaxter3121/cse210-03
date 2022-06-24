class TerminalService():
    """
    Handles terminal operations, displaying text or reading input.

    Attributes:
        parachutes (list): A list of the parachute "drawings".
    """

    def __init__(self):
        """
        Constructs a new TerminalService class instance.

        Args:
            self (TerminalService): An instance of TerminalService.
        """

    def outputText(self, string):
        """
        Prints a given string to the terminal.

        Args:
            self (TerminalService): An instance of TerminalService.
            string (string): A string to print to the console.
        """
        print(string)

    def playerInput(self, string):
        """
        Obtains an input from the player based on a prompt.

        Args:
            self (TerminalService): An instance of TerminalService.
            string (string): A string to use as a prompt.
        """
        return input(string).lower()