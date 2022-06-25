from game.scripting.action import Action


class DrawActorsAction(Action):
    """
    An output action that draws all the actors.

    The responsibility of DrawActorsAction is to draw all the actors.

    Attributes:
        _video_service (VideoService): An instance of VideoService.
    """

    def __init__(self, video_service):
        """Constructs a new DrawActorsAction using the specified VideoService.

        Args:
            video_service (VideoService): An instance of VideoService.
        """
        self._video_service = video_service

    def execute(self, cast, script):
        """Executes the draw actors action.

        Args:
            cast (Cast): The cast of Actors in the game.
            script (Script): The script of Actions in the game.
        """

        # get snake segments
        snakes = cast.get_actors("snakes")
        segments = []
        for snake in snakes:
            segments += snake.get_segments()
        # get score and messages
        score = cast.get_actors("scores")
        messages = cast.get_actors("messages")
        # draw
        self._video_service.clear_buffer()
        self._video_service.draw_actors(segments)
        self._video_service.draw_actors(score)
        self._video_service.draw_actors(messages, True)
        self._video_service.flush_buffer()
