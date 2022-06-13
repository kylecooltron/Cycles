import constants
from game.scripting.action import Action


class HandleGrowthAction(Action):
    """
    An event action that makes the game more difficult.

    The responsibility of HandleGrowthAction is to add extra tails to snakes over time

    Attributes:
        _timer keeps track of when to grow snakes tails.
    """

    def __init__(self):
        """Constructs a new HandleGrowthAction.

        Args:
            self._timer keeps track of when to grow snakes tails.
        """
        self._timer = 0

    def execute(self, cast, script):
        """Executes the handle growth action.

        Args:
            cast (Cast): The cast of Actors in the game.
            script (Script): The script of Actions in the game.
        """
        # this is executed every frame during do updates phase of game loop
        # run timer and every once and a while add tails to snakes
