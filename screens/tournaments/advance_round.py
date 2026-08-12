from ..base_screen import BaseScreen
from commands.tournaments import TournamentAdvanceRoundCmd


class TournamentAdvanceRound(BaseScreen):
    """ display screen when advancing to next round or starting tournament """
    def __init__(self, tournament):
        self.tournament = tournament

    def display(self):
        if not self.tournament.is_started:
            print("Starting the tournament - generating round 1 pairings...")
        else:
            print("Moving to the next round...")

    def get_command(self):
        return TournamentAdvanceRoundCmd(self.tournament)
