import constants
from game.scripting.action import Action


class HandleGrowthAction(Action):
    """
    An event action that makes the game more difficult.

    The responsibility of HandleGrowthAction is to add extra tails to cycles over time

    Attributes:
        _timer keeps track of when to grow cycles tails.
    """

    def __init__(self):
        """Constructs a new HandleGrowthAction.

        Args:
            self._timer keeps track of when to grow cycles tails.
            self._wait_time determines the time interval for cycle growth
        """
        self._timer = 0
        self._wait_time = constants.GROW_TAIL_WAIT

    def execute(self, cast, script):
        """Executes the handle growth action.

        Args:
            cast (Cast): The cast of Actors in the game.
            script (Script): The script of Actions in the game.
        """
        # this is executed every frame during do updates phase of game loop
        # run timer and every once and a while add tails to cycles

        cycles = cast.get_actors("cycles")

        if(cycles[0].get_is_dead() == True):

            # if the cycles are dead, reset the wait time
            self._wait_time = constants.GROW_TAIL_WAIT

        else:

            # count each step
            self._timer += 1

            # when wait time is reached
            if self._timer > self._wait_time:

                # reset count
                self._timer = 0

                #  grow tails
                for cycle in cycles:
                    cycle.grow_tail(1)

                # make the wait times faster over time, but not less than 20
                if self._wait_time > 20:
                    self._wait_time -= 1
