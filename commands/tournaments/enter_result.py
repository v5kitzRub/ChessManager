from commands.base import BaseCommand
from commands.context import Context


class TournamentEnterResultCmd(BaseCommand):
    """
    store curr tournament obj, match instance, winner chessid
    execute record_results in tournament, return context screen
    """
    def __init__(self, tournament, match, winner=None):
        self.tournament = tournament
        self.match = match
        self.winner = winner

    def execute(self):
        self.tournament.record_result(self.match, winner=self.winner)
        return Context("tournament-enter-results", tournament=self.tournament)
