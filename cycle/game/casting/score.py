from game.casting.actor import Actor
from game.shared.point import Point
import constants


class Score(Actor):
    """
    A record of points made or lost. 

    The responsibility of Score is to keep track of the points the player has earned by eating food.
    It contains methods for adding and getting points. Client should use get_text() to get a string 
    representation of the points earned.

    Attributes:
        _points (int): The points earned in the game.
        _player (string): Which player this score belongs to "first" or "second"
    """

    def __init__(self, player):
        super().__init__()
        self._points = 0
        self._player = player
        self.add_points(0)
        self.init_position(self._player)

    def get_player(self):
        return self._player

    def init_position(self, player):
        """Sets score display to corners of screen based on player variable

        Args:
            player (string): Which player this score belongs to
        """
        if self._player == "first":
            self.set_position(
                Point(2 * constants.CELL_SIZE, constants.CELL_SIZE))

        if self._player == "second":
            self.set_position(
                Point(constants.MAX_X - 8 * constants.CELL_SIZE, constants.CELL_SIZE))

    def add_points(self, points):
        """Adds the given points to the score's total points.

        Args:
            points (int): The points to add.
        """
        self._points += points

        # check to see which player this score belongs to so we display it correctly
        if self._player == "first":
            self.set_text(f"Green Score: {self._points}")

        if self._player == "second":
            self.set_text(f"Red Score: {self._points}")
