class Match:
    def __init__(self, player1, player2, completed=False, winner=None):
        self.player1 = player1
        self.player2 = player2
        self.completed = completed
        self.winner = winner

    def __str__(self):
        # format for return
        return f"{self.player1} vs {self.player2}"

    @property
    def players(self):
        return (self.player1, self.player2)

    @property
    def is_draw(self):
        # draws when matchups completed and no winner
        return self.completed and self.winner is None

    def has_player(self, chess_id):
        # return matchup players chessid
        return chess_id in self.players

    def set_result(self, winner=None):
        """ matchup result """
        # matchup result must be player of current matchup
        if winner is not None and winner not in self.players:
            raise ValueError(f"{winner} is not a player in this match")

        # store winner none if draw
        self.winner = winner
        # set matchup as completed
        self.completed = True

    def points_for(self, chess_id):
        """ matchup points payout """
        # matchup not completed
        if not self.has_player(chess_id) or not self.completed:
            return 0
        # no winner is draw
        if self.winner is None:
            return 0.5
        # winner chessid recieves 1 point, loser 0
        return 1 if self.winner == chess_id else 0

    def serialize(self):
        """ format for .json """
        return {
            "players": [self.player1, self.player2],
            "completed": self.completed,
            "winner": self.winner,
        }

    @classmethod
    def from_dict(cls, data):
        """ rebuild match from .json """
        player1, player2 = data["players"]
        return cls(
            player1,
            player2,
            completed=data.get("completed", False),
            winner=data.get("winner"),
        )
