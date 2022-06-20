import constants
from game.casting.actor import Actor
from game.scripting.action import Action
from game.shared.point import Point


class HandleCollisionsAction(Action):
    """
    An update action that handles interactions between the actors.

    The responsibility of HandleCollisionsAction is to handle the situation when the snake collides
    with the food, or the snake collides with its segments, or the game is over.

    Attributes:
        _is_game_over (boolean): Whether or not the game is over.
    """

    def __init__(self, keyboard_service):
        """Constructs a new HandleCollisionsAction."""

        self._keyboard_service = keyboard_service

        self._is_game_over = False
        self._who_won = ""

    def execute(self, cast, script):
        """Executes the handle collisions action.

        Args:
            cast (Cast): The cast of Actors in the game.
            script (Script): The script of Actions in the game.
        """
        if not self._is_game_over:
            self._handle_snakes_collision(cast)
            self._handle_segment_collision(cast)
            self._handle_game_over(cast)
        else:
            if self._keyboard_service.is_key_down('y'):
                # reset game over variable
                self._is_game_over = False
                # remove game over message
                cast.remove_actor("messages", cast.get_first_actor("messages"))
                # reset snake bodies
                snakes = cast.get_actors("snakes")
                for snake in snakes:
                    snake._reset_body()

    def _return_player_color(self, value, reverse=False):
        """Returns the color of the snake that won

        Args:
            cast (Cast): The cast of Actors in the game.
            value (string): either "first" or "second" so we know which player won
            reverse (bool): default is False. Returns the opposite players color when True
        """
        color_list = ["Green", "Red"]
        if value == "first":
            color = 0
        else:
            color = 1
        if reverse:
            color = 1 - color
        return color_list[color]

    def _handle_snakes_collision(self, cast):
        """Sets the game over flag if a snake head collides with a segment from another snake.

        Args:
            cast (Cast): The cast of Actors in the game.
        """
        snakes = cast.get_actors("snakes")

        # for every snake
        for snake in snakes:
            head = snake.get_segments()[0]
            # loop through every other snake
            for other in snakes:
                # make sure its not ourselves
                if other != snake:
                    for segment in other.get_segments():
                        # for every segment in this other snake
                        if head.get_position().equals(segment.get_position()):
                            # if head collides with any, game over
                            self._is_game_over = True
                            # assign winner to the other player
                            self._who_won = self._return_player_color(
                                other.get_player())

    def _handle_segment_collision(self, cast):
        """Sets the game over flag if the snake collides with one of its segments.

        Args:
            cast (Cast): The cast of Actors in the game.
        """
        snakes = cast.get_actors("snakes")
        for snake in snakes:
            head = snake.get_segments()[0]
            segments = snake.get_segments()[1:]

            for segment in segments:
                if head.get_position().equals(segment.get_position()):
                    # if snake hit itself, the other player wins
                    self._who_won = self._return_player_color(
                        snake.get_player(), True)
                    # end game
                    self._is_game_over = True

    def _handle_game_over(self, cast):
        """Shows the 'game over' message and turns the snake and food white if the game is over.

        Args:
            cast (Cast): The cast of Actors in the game.
        """
        if self._is_game_over:

            snakes = cast.get_actors("snakes")

            x = int(constants.MAX_X / 2)
            y = int(constants.MAX_Y / 2)
            position = Point(x, y)

            message = Actor()
            message.set_text(
                f"Game Over!\n {self._who_won.capitalize()} player won the game.\n\n Press 'Y' to play again! ")
            message.set_position(position)
            cast.add_actor("messages", message)

            # turn all segments of all snakes white
            for snake in snakes:
                segments = snake.get_segments()
                for index, segment in enumerate(segments):
                    # leave one colored spot to identify which is which
                    if index != 1:
                        segment.set_color(constants.WHITE)
