from . import pairing
from .match import Match
from .round import Round
from utils import read_json, write_json


class Tournament:
    DATE_FORMAT = "%d-%m-%Y"

    def __init__(
        self,
        name,
        venue,
        date_from,
        date_to,
        number_of_rounds=4,
        players=None,
        rounds=None,
        current_round=None,
        completed=False,
        filepath=None,
    ):
        if not name:
            raise ValueError("Tournament Must Have Name")

        self.name = name
        self.venue = venue
        self.date_from = date_from
        self.date_to = date_to
        self.number_of_rounds = number_of_rounds
        self.players = players or []
        self.rounds = rounds or []
        self.current_round = current_round
        self.completed = completed
        self.filepath = filepath

    def __str__(self):
        return f"<Tournament: {self.name}>"

    # -------- tournament property
    @property
    def is_started(self):
        return len(self.rounds) > 0

    @property
    def current_round_obj(self):
        """The Round currently being played, or None if not started yet."""
        if not self.rounds:
            return None
        return self.rounds[-1]

    def points(self):
        """Return a dict mapping chess_id -> total tournament points."""
        totals = {player: 0 for player in self.players}
        for round_ in self.rounds:
            for match in round_:
                if not match.completed:
                    continue
                totals[match.player1] += match.points_for(match.player1)
                totals[match.player2] += match.points_for(match.player2)
        return totals

    def ranked_players(self):
        """Players sorted by points descending, for report display."""
        totals = self.points()
        return sorted(self.players, key=lambda p: totals[p], reverse=True)

    # -------- register player
    def register_player(self, chess_id):
        if self.is_started:
            raise RuntimeError("Unable to register after tournament started")
        if chess_id in self.players:
            raise ValueError(f"{chess_id}: is already registered for this tournament")

        self.players.append(chess_id)
        self.save()

    # -------- rounds process
    def start(self):
        """Generate and save the first round (random pairing)."""
        if self.is_started:
            raise RuntimeError("Tournament has already started.")
        if len(self.players) < 2:
            raise RuntimeError("At least two players must be registered to start.")

        pairs = pairing.generate_first_round_pairs(self.players)
        self._add_round(pairs)
        self.current_round = 1
        self.save()

    def record_result(self, match, winner=None):
        """Set the result for matchup"""
        if self.current_round_obj is None or match not in self.current_round_obj:
            raise RuntimeError("That match is not part of the current round.")

        match.set_result(winner)
        self.save()

    def advance_round(self):
        """
        Close out the current round and either start the next one or,
        if this was the last round, mark the tournament as completed.
        """
        current = self.current_round_obj
        if current is None:
            raise RuntimeError("Tournament has not started yet.")
        if not current.is_complete:
            raise RuntimeError("All matches in the current round must have a result first.")

        if self.current_round >= self.number_of_rounds:
            self.completed = True
            self.current_round = None
            self.save()
            return

        already_played = pairing.match_history(self.rounds)
        pairs = pairing.generate_next_round_pairs(self.players, self.points(), already_played)
        self._add_round(pairs)
        self.current_round += 1
        self.save()

    def _add_round(self, pairs):
        matches = [Match(p1, p2) for p1, p2 in pairs]
        self.rounds.append(Round(matches))

    # -------- load/ save serialized into json file
    def serialize(self):
        """ format for .json """
        return {
            "name": self.name,
            "venue": self.venue,
            "dates": {"from": self.date_from, "to": self.date_to},
            "number_of_rounds": self.number_of_rounds,
            "current_round": self.current_round,
            "completed": self.completed,
            "players": self.players,
            "rounds": [r.serialize() for r in self.rounds],
        }

    def save(self):
        write_json(self.filepath, self.serialize())

    @classmethod
    def load(cls, filepath):
        """ rebuild from .json """
        data = read_json(filepath)
        return cls(
            name=data["name"],
            venue=data["venue"],
            date_from=data["dates"]["from"],
            date_to=data["dates"]["to"],
            number_of_rounds=data["number_of_rounds"],
            players=data.get("players", []),
            rounds=[Round.from_list(r) for r in data.get("rounds", [])],
            current_round=data.get("current_round"),
            completed=data.get("completed", False),
            filepath=filepath,
        )
