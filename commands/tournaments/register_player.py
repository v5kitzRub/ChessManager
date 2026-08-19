from commands.base import BaseCommand
from commands.context import Context


class TournamentRegisterPlayerCmd(BaseCommand):
    """
    store curr tournament obj, chessid
    execute register_player in tournament, return context screen
    """
    def __init__(self, tournament, chess_id):
        # current tournament instance
        self.tournament = tournament
        # input chessid
        self.chess_id = chess_id

    def execute(self):
        # register player in tournament given chessid
        self.tournament.register_player(self.chess_id)
        # return to tournament view
        return Context("tournament-view", tournament=self.tournament)
