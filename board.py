class Ship(object):
    """
    Class will represent a ship. Contains 4 methods: first to initialize all variables and also to
    get all positions occupied by ship, second to return this list of points occupied by the ship,
    third to return the orientationof the ship, finally fourth to apply a hit to the ship and check
    if ship has been sunk.
    """

    def __init__(self, length, position, orientation):
        """
        Receives length of the ship(int), position(a coordinate in (row, column) format),
        and an orientation (either `h`, horizontal, or `v`, vertical) as parameters. Then
        funtion will create a list of every point the ship is occupying by using the given
        position and orientation, and will also define two other variables, hit_count which
        will keep track of how many hits the ship has suffered, and is_sunk which will tell
        if ship has been sunk or not. Returns None.
        """
        self.length = length
        self.orientation = orientation

        L1 = []
        if type(position) != tuple:  # checking for other data types so different action can be taken
            nospace = position.replace(',', ' ').split()
            tup_0 = (int(nospace[0]), int(nospace[1]))
        else:
            tup_0 = position  # initial position of ship
        L1.append(tup_0)

        if self.orientation == 'h':
            row = tup_0[0]
            col = tup_0[1]
            for num in range(self.length - 1):  # will get all points occupied by ship
                col += 1
                position_tup = (row, col)
                L1.append(position_tup)

        elif self.orientation == 'v':
            row = int(position[0])
            col = int(position[1])
            for num in range(self.length - 1):  # will get all points occupied by ship
                row += 1
                position_tup = (row, col)
                L1.append(position_tup)

        self.position = L1
        self.hit_count = 0
        self.is_sunk = False


    def get_positions(self):
        """
        Function receives only self as parameter, and returns the list containing
        all points occupied by the ship.
        """
        return self.position


    def get_orientation(self):
        """
        Function receives only self as parameter, and returns the orientation of the ship.
        """
        return self.orientation


    def apply_hit(self):
        """
        Function receives only self as parameter. The method will apply a hit to the ship
        and will then check if the ship has sunk. Returns None.
        """
        self.hit_count += 1
        if self.hit_count == self.length:  # if all points of ship have been hit then ship has sunk
            self.is_sunk = True

class Board(object):
    """
    Class will represent the board of each player. Contains 5 methods: first to intialize all
    variables, second to place ship on the board, third to apply a guess the player has made and
    checking if a ship was hit or not, fourth to validate if the place the player wants to put the
    ship is valid, then finally fifth to provide a more readable board output for the players.
    """

    def __init__(self, size):
        """
        Receives self(object) and size of the board(int) as parameters. Method will
        also initialize a list of lists that represents the board by given size number of empty
        spaces(str) in each list and given size number of lists with empty spaces. Finally, it
        will initialize a list that will contain all ships placed by player.
        """
        self.size = int(size)
        self.board = []
        for i in range(size):  # board will have size amount of lists with size amount of empty strings in each.
            L1 = []
            for i in range(size):
                blank = " "
                L1.append(blank)
            self.board.append(L1)
        self.ships = []


    def place_ship(self, ship):
        """
        Receives self and ship(both objects) as parameters. Will place a ship in all
        the points the ship will occupy, and finally it will update the board and the
        ships list. Returns None.
        """
        x = ship.get_positions()
        for item in x:
            row = int(item[0])
            col = int(item[1])
            self.board[row][col] = "S"
        self.ships.append(ship)  # append the object to the list so later methods are accessible



    def apply_guess(self, guess):
        """
        Receives self(object) and guess(tuple) as parameters. Will apply the player's
        guess and check if the player hit a ship or not, if it is a hit player will be
        notified and board will be updated to `H`, and if player has missed, player also
        will be notified and board will be updated to `M`. Returns None.
        """
        row = int(guess[0])
        col = int(guess[1])
        i = 0
        for ship in self.ships:
            if guess in ship.position:  # if there is a ship where player guessed
                ship.apply_hit()
                i += 1

        if i > 0:
            self.board[row][col] = 'H'
            print("Hit!")

        else:
            self.board[row][col] = 'M'
            print("Miss!")

    def validate_ship_coordinates(self, ship):
        """
        Receives two objects as parameters, ship and self. will validate if the location
        where the player wants to place the ship is valid. Method also handles errors so
        program won't crash with innapropriate input. Returns None
        """
        valid_spot = 0
        for item in ship.get_positions():
            row = int(item[0])
            col = int(item[1])
            try:
                spot = self.board[row][col]
                if spot == ' ':
                    valid_spot += 1
                else:
                    e = "Ship coordinates are already taken!"
                    raise RuntimeError(e)
            except IndexError:
                e = "Ship coordinates are out of bounds!"
                raise RuntimeError(e)

    def __str__(self):
        """
        Receives self as parameter. Method used to set up displayable board for better user
        quality and better readability. Returns the string board where every point of the board
        will be placed in parentheses.
        """
        board = ""
        for row in self.board:  # readable board output
            for point in row:
                y = '[{}]'.format(point)
                board += y
            board += '\n'
        return board
