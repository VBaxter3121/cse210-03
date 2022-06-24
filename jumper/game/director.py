from game.terminal_service import TerminalService
from game.puzzler import Puzzler
from game.guesser import Guesser
from game.parachutes import Parachutes

class Director:
    """
    Directs the sequence of the game.

    Attributes:
        terminalService (TerminalService): Gets and displays information on the terminal.
        puzzler (Puzzler): Chooses the word to guess.
        guesser (Guesser): Guesses letters and keeps track of previous guesses.
        isPlaying (boolean): Shows if the game is still running or not.
    """

    def __init__(self):
        """
        Constructs a new Director class instance.

        Args:
            self (Director): An instance of Director.
        """
        self._terminalService = TerminalService()
        self._puzzler = Puzzler()
        self._guesser = Guesser()
        self._parachutes = Parachutes()
        self._isPlaying = True

    def start_game(self):
        """
        Begins the gameplay loop.

        Args:
            self (Director): An instance of Director.
        """
        self._puzzler.choose_word()
        self._guesser.update_word(self._puzzler.chosenWord)
        self._do_outputs()

        while self._isPlaying:
            self._get_inputs()
            self._do_updates()
            self._do_outputs()
        
        if "_" not in self._guesser.wordProgress:
            self._terminalService.outputText("Congratulations, you have won!")
        else:
            self._terminalService.outputText("You have lost!")

    def _get_inputs(self):
        """
        Obtains a player input (guess), checks that it hasn't previously been guessed, and appends it to the appropriate list.

        Args:
            self (Director): An instance of Director.
        """
        repeat = True
        while repeat == True:
            guess = self._terminalService.playerInput("Please guess a letter: ")
            repeat = self._guesser.guess_repeat(guess)
            if repeat == True:
                self._terminalService.outputText("Invalid guess. Please choose another letter.\n")
        
        self._guesser.compare_guess(guess, self._puzzler.chosenWord)

    def _do_updates(self):
        """
        Updates the amount of the word dicovered and the progress of the parachute.

        Args:
            self (Director): An instance of Director.
        """
        self._guesser.update_word(self._puzzler.chosenWord)
        self._isPlaying = self._guesser.keep_guessing()
    
    def _do_outputs(self):
        """
        Prints the current state of the word to be guessed, and the parachute.

        Args:
            self (Director): An instance of Director.
        """
        self._terminalService.outputText(self._parachutes.choose_parachute(len(self._guesser._incorrectGuesses)))
        self._terminalService.outputText(self._guesser.wordProgress)