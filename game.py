from board import Ship,Board #important for the project

## Uncomment the following lines when you are ready to do input/output tests!
## Make sure to uncomment when submitting to Codio.
import sys
def input( prompt=None ):
   if prompt != None:
       print( prompt, end="" )
   aaa_str = sys.stdin.readline()
   aaa_str = aaa_str.rstrip( "\n" )
   print( aaa_str )
   return aaa_str


class Player(object):
    """
    Class will represent a player. Contains 4 methods: one to initialize all
    variables needed, another to check if the player's guess is valid or not,
    then one to get this guess from the player, then finally one to get what
    initial location and orientation for each ship the player wants.
    """
    def __init__(self, name, board, ship_list):
        """
        Receives self, name(name of player), board(object), and ship_list(all
        ships the player has) as parameters. Will initialize all parameters and
        additionally an empty list where all guesses will be stored
        """
        self.name = name
        self.board = board
        self.guesses = []
        self.ship_list = ship_list

    def validate_guess(self, guess):
        """
        Receives self and a guess(tuple) as parameters. Using the list of
        guesses it will check if guess has already been made and if the guess
        is a valid position in the board, while also handling any errors that
        could be thrown by a invalid guess. Returns None.
        """
        try:
            if guess in self.guesses:
                e = 'This guess has already been made!'
                raise RuntimeError(e)
        except IndexError:
            e = 'Guess is not a valid location!'
            raise RuntimeError(e)

    def get_player_guess(self):
        """
        Receives only self as parameter. Ask user for a guess, then use
        validate_guess to check if guess is valid, if not program will reprompt
        until valid. Returns the guess (tuple).
        """
        x = True
        while x:
            guess_str = input('Enter your guess: ')
            guess_list = guess_str.replace(',', '').split()
            guess_tup = (int(guess_list[0]), int(guess_list[1]))
            try:
                self.validate_guess(guess_tup)
                x = False
            except RuntimeError as e:
                print(e)
        return guess_tup

    def set_all_ships(self):
        """
        Receives only self as parameter. Ask player the initial position and the orientation for each
        ship, after gathering input will create an instance from class Ship for every size of ship, then
        validate the ship position and if no errors are raised will place the ships. If errors are thrown,
        then message error will be printed and user will be reprompted until valid input is given. Returns None.
        """
        for size in self.ship_list:
            x = True
            while x:
                coordinate = input(f'Enter the coordinates of the ship of size {size}: ')
                orientation = input(f'Enter the orientation of the ship of size {size}: ')
                ship = Ship(size, coordinate, orientation)  # create instance for every ship

                try:
                    self.board.validate_ship_coordinates(ship)
                    x = False
                except RuntimeError as e:
                    print(e)
            self.board.place_ship(ship)


class BattleshipGame(object):
    """
    Class will represent the Battleship game. Will contain 4 methods: one to initialize all variables,
    another to check if there is a winner, one to display both player's board in an organizes way, then
    finally one that will control the whole game and dictate what players will do.
    """

    def __init__(self, player1, player2):
        """
        Receives and initializes two objects (player1 and player2). Returns None.
        """
        self.player1 = player1
        self.player2 = player2

    def check_game_over(self):
        """
        Receives self as a parameter. Will check if any player has all their ships sunk. If
        so, then the opposing player's name will be returned. And if both players still have
        ships then will return an empty string.
        """

        if all(ship.is_sunk for ship in self.player1.board.ships):  # if all of player1's ships have been sunk
            return self.player2.name  # then player2 wins
        elif all(ship.is_sunk for ship in self.player2.board.ships):  # if all of player2's ships have been sunk
            return self.player1.name  # then player1 wins
        else:
            return ''

    def display(self):
        """
        Receives self as the only parameter. Will then print both players' boards.
        Returns None.
        """
        print(f"{self.player1.name}'s board:" )
        print(self.player1.board)
        #print()
        print(f"{self.player2.name}'s board:")
        print(self.player2.board)

    def play(self):
        """
        Receivesself as its only parameter. Will request both players to put all their ships
        on the board by using the set_all_ships method. Then until there's either a winner or
        the player inputs 'q' when asked if they want to keep playing, program will first print
        each players' board then ask for a guess, after every guess program will check if there's
        a winner, if there is one message will be printed. Returns None
        """

        self.player1.set_all_ships()  # player1 will place all ships on board

        self.player2.set_all_ships()  # player2 will place all ships on board

        command = ''
        while command != 'q':
            self.display()  # display both boards before every turn

            print(f"{self.player1.name}'s turn.")
            guess_p1 = self.player1.get_player_guess()  # get a guess from player
            self.player2.board.apply_guess(guess_p1)  # validate guess

            winner = self.check_game_over()  # check if there is a winner
            if winner != '':
                print(f'{winner} wins!')
                break

            print(f"{self.player2.name}'s turn.")
            guess_p2 = self.player2.get_player_guess()
            self.player1.board.apply_guess(guess_p2)

            winner = self.check_game_over()
            if winner != '':
                print(f'{winner} wins!')
                break

            command = input('Continue playing?: ').lower()



