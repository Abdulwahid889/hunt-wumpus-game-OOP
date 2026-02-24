# You do not have to use the below Player class, but it's quite a bit of
# useful code, so using it will save you some time :)

from copy import deepcopy

from coordinates import Coordinates

class Player:
    _coordinates: Coordinates # Player's current location in the forest
    _previous_coordinates: Coordinates # Previous location in the forest

    _num_blueberries_eaten: int # Goes up when the player eats a blueberry bush
    _thirsty: bool # Becomes False when the player drinks from the pond

    _won: bool # Records whether the player has won the game yet
    _lost: bool # Records whether the player has lost the game yet

    def __init__(self) -> None:
        # Start out in bottom-left: row 4, column 0
        self._coordinates = Coordinates(4, 0)
        self._previous_coordinates = Coordinates(4, 0)
        self._num_blueberries_eaten = 0
        self._thirsty = True
        self._won = False
        self._lost = False

    # Pass 'left', 'right', 'up', or 'down' (all lowercase) to this method
    # to cause the player to move in the specified direction. Make sure to
    # call the can_move() method below first to see whether the player CAN
    # move in the specified direction
    def move(self, direction: str) -> None:
        # Copy current location to previous location. A copy is necessary,
        # as opposed to simple assignment, or else both attributes will
        # reference the same object.
        self._previous_coordinates = deepcopy(self._coordinates)
        if direction == 'left':
            self._coordinates.column -= 1
        if direction == 'right':
            self._coordinates.column += 1
        if direction == 'up':
            self._coordinates.row -= 1
        if direction == 'down':
            self._coordinates.row += 1

    # Pass 'left', 'right', 'up', or 'down' to determine whether the player
    # CAN move in the specified direction (returns False if the movement
    # would cause them to move beyond the edge of the game board)
    def can_move(self, direction: str) -> bool:
        if direction == 'left':
            return self._coordinates.column > 0
        elif direction == 'right':
            return self._coordinates.column < 4
        elif direction == 'up':
            return self._coordinates.row > 0
        else:
            return self._coordinates.row < 4

    # Getter for player's current location
    def get_coordinates(self) -> Coordinates:
        return self._coordinates

    # Call this method whenever the player eats a blueberry bush
    def eat(self) -> None:
        self._num_blueberries_eaten += 1

    # Call this method when the player drinks from the pond
    def drink(self) -> None:
        self._thirsty = False

    # Getter for self._thirsty
    def is_thirsty(self) -> bool:
        return self._thirsty

    # Returns True if the player hasn't yet eaten 2 blueberry bushes
    def is_hungry(self) -> bool:
        return self._num_blueberries_eaten < 2

    # Getter for self._won
    def has_won(self) -> bool:
        return self._won

    # Getter for self._lost
    def has_lost(self) -> bool:
        return self._lost

    # Sets self._won to True. Call this method when the player makes it back
    # to the DeerHerd if they've eaten two blueberry bushes and drank from the
    # pond (i.e., if is_thirsty() and is_hungry() both return False)
    def win(self) -> None:
        self._won = True

    # Sets self._lost to True. Call this method when the player encounters 
    # a given BearDen for the second time
    def lose(self) -> None:
        self._lost = True

    # Moves the player back to their previous position just before their most
    # recent movement. Call this method when the player encounters a given
    # BearDen for the first time.
    def move_back(self) -> None:
        self._coordinates = deepcopy(self._previous_coordinates)
