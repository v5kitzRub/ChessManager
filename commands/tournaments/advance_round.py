from commands.base import BaseCommand
from commands.context import Context


class TournamentAdvanceRoundCmd(BaseCommand):
    """ store curr tournament obj, execute start/advance in tournament, return context screen """
    def __init__(self, tournament):
        # current tournament instance
        self.tournament = tournament

    def execute(self):
        if not self.tournament.is_started:
            # start in tournament
            self.tournament.start()
        else:
            # advance round in tournament
            self.tournament.advance_round()

        # return to tournament view
        return Context("tournament-view", tournament=self.tournament)
