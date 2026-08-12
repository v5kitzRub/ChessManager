from commands.base import BaseCommand
from commands.context import Context


class TournamentAdvanceRoundCmd(BaseCommand):
    """ store curr tournament obj, execute start/advance in tournament, return context screen """
    def __init__(self, tournament):
        self.tournament = tournament

    def execute(self):
        if not self.tournament.is_started:
            self.tournament.start()
        else:
            self.tournament.advance_round()

        return Context("tournament-view", tournament=self.tournament)
