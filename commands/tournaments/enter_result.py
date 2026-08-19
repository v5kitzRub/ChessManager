from commands.base import BaseCommand
from commands.context import Context


class TournamentEnterResultCmd(BaseCommand):
    """
    store curr tournament obj, match instance, winner chessid
    execute record_results in tournament, return context screen
    """
    def __init__(self, tournament, match, winner=None):
        # current tournament instance
        self.tournament = tournament
        # current matchup obj
        self.match = match
        # winning player chessid or none if draw
        self.winner = winner

    def execute(self):
        # record result in tournament given matchup and winner
        self.tournament.record_result(self.match, winner=self.winner)
        # stay on enter results screen until all matchups have retuslts
        return Context("tournament-enter-results", tournament=self.tournament)
