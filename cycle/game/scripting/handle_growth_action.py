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
            self._wait_time determines the time interval for snake growth
        """
        self._timer = 0
        self._wait_time = 100

    def execute(self, cast, script):
        """Executes the handle growth action.

        Args:
            cast (Cast): The cast of Actors in the game.
            script (Script): The script of Actions in the game.
        """
        # this is executed every frame during do updates phase of game loop
        # run timer and every once and a while add tails to snakes

        self._timer += 1

        if self._timer > self._wait_time:
            snakes = cast.get_actors("snakes")
            
            for snake in snakes:
                snake.grow_tail(1)

            self._wait_time -= 1
            self._timer = 0
        