################################################################################
# Computer Project #8
#
#   Ship class -- deals with all components related to individual ships.
#
#   Board Class -- deals with all the components related to each player's board.
#
#   Player Class -- deals with all the attributes related to a player.
#
#   BattleshipGame Class -- deals with the attributes of the game itself.
#
#   Main -- brings all the classes together and allows players to play the game.
#
#
################################################################################


from board import Ship, Board #important for the project
from game import Player, BattleshipGame #important for the project


def main():
    board_size = 5  # board's dimension is 5x5
    ship_list = [5, 4, 3, 3, 2]  # all ships the player's have
    b1 = Board(board_size)  # initialize an instance of Board for Player 1
    p1 = Player('Player 1', b1, ship_list)
    # initialize an instance of Player for Player 1 and its board.

    b2 = Board(board_size)  # initialize an instance of Board for Player 2
    p2 = Player('Player 2', b2, ship_list)
    # initialize an instance of Player for Player 2 and its board

    game1 = BattleshipGame(p1, p2)
    # initialize an instance of BattleshipGame with both players
    game1.play()  # play method will allow players to play the game

if __name__ == "__main__":
    main()