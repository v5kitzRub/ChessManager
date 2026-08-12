from ..base_screen import BaseScreen
from models import build_player_index
from commands.tournaments import TournamentEnterResultCmd
from commands import NoopCmd


class TournamentEnterResults(BaseScreen):
    """ screen displayed when entering matchup results """
    def __init__(self, tournament):
        self.tournament = tournament
        self.player_index = build_player_index()

    def _label(self, chess_id):
        player = self.player_index.get(chess_id)
        return player.name if player else chess_id

    def display(self):
        round_ = self.tournament.current_round_obj
        print("##", self.tournament.name, "- round", self.tournament.current_round, "results")
        for idx, match in enumerate(round_, 1):
            status = "done" if match.completed else "pending"
            print(f"{idx}. {self._label(match.player1)} vs {self._label(match.player2)} [{status}]")

    def get_command(self):
        round_ = self.tournament.current_round_obj
        pending = round_.pending_matches()

        if not pending:
            print("All results for this round have been entered.")
            return self._back_command()

        match = pending[0]
        print(f"Result for {self._label(match.player1)} (1) vs {self._label(match.player2)} (2):")
        print("Type 1 if player 1 won, 2 if player 2 won, or D for a draw.")

        while True:
            value = self.input_string().upper()
            if value == "1":
                return TournamentEnterResultCmd(self.tournament, match, winner=match.player1)
            elif value == "2":
                return TournamentEnterResultCmd(self.tournament, match, winner=match.player2)
            elif value == "D":
                return TournamentEnterResultCmd(self.tournament, match, winner=None)

    def _back_command(self):
        return NoopCmd("tournament-view", tournament=self.tournament)
