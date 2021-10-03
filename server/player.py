from .player_action import PlayerAction
from .player_base import PlayerBase
from .player_judge import PlayerJudge


class Player(PlayerAction, PlayerBase, PlayerJudge):
    pass
