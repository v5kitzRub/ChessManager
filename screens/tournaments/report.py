from ..base_screen import BaseScreen
from models import build_player_index
from commands import NoopCmd


class TournamentReport(BaseScreen):
    """ report screen displays standings and each round results/matchups for a tournament """
    def __init__(self, tournament):
        self.tournament = tournament
        self.player_index = build_player_index()

    def _label(self, chess_id):
        player = self.player_index.get(chess_id)
        return player.name if player else chess_id

    def display(self):
        t = self.tournament
        print("##", t.name, "- report")
        print("Venue:", t.venue, "|", t.date_from, "-", t.date_to)
        print()

        print("### Standings")
        points = t.points()
        for rank, chess_id in enumerate(t.ranked_players(), 1):
            print(f"{rank}. {self._label(chess_id)} - {points[chess_id]} pt(s)")
        print()

        print("### Rounds")
        for round_num, round_ in enumerate(t.rounds, 1):
            print(f"Round {round_num}:")
            for match in round_:
                if not match.completed:
                    result = "not played"
                elif match.is_draw:
                    result = "draw"
                else:
                    result = f"{self._label(match.winner)} won"
                print(f"  - {self._label(match.player1)} vs {self._label(match.player2)}: {result}")

    def get_command(self):
        print("Type B to go back.")
        self.input_string()
        return NoopCmd("tournament-view", tournament=self.tournament)
