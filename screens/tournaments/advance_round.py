from ..base_screen import BaseScreen
from commands import NoopCmd
from commands.tournaments import TournamentAdvanceRoundCmd


class TournamentAdvanceRound(BaseScreen):
    """ display screen when advancing to next round or starting tournament """
    def __init__(self, tournament):
        # current tournament instance
        self.tournament = tournament

    def display(self):
        if not self.tournament.is_started:
            print("This will start the tournament and generate round 1 pairings:")
        else:
            print(f"This will close round {self.tournament.current_round} and move to the next round.")

    def get_command(self):
        if not self.tournament.is_started:
            prompt = "Are you sure you want to start the tournament"
        else:
            prompt = "Are you sure you want to advance to the next round"

        confirm = self.input_string(prompt=f"{prompt} (y/n)").strip().upper()

        if confirm != "Y":
            print("Tournament Paused")
            return NoopCmd("tournament-view", tournament=self.tournament)

        return TournamentAdvanceRoundCmd(self.tournament)
