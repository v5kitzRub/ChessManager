class Match:
    def __init__(self, player1, player2, completed=False, winner=None):
        self.player1 = player1
        self.player2 = player2
        self.completed = completed
        self.winner = winner

    def __str__(self):
        return f"{self.player1} vs {self.player2}"

    @property
    def players(self):
        return (self.player1, self.player2)

    @property
    def is_draw(self):
        return self.completed and self.winner is None

    def has_player(self, chess_id):
        return chess_id in self.players

    def set_result(self, winner=None):
        """ matchup result """
        if winner is not None and winner not in self.players:
            raise ValueError(f"{winner} is not a player in this match")

        self.winner = winner
        self.completed = True

    def points_for(self, chess_id):
        """ matchup points payout """
        if not self.has_player(chess_id) or not self.completed:
            return 0
        if self.winner is None:
            return 0.5
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
