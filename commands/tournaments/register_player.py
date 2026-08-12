from commands.base import BaseCommand
from commands.context import Context


class TournamentRegisterPlayerCmd(BaseCommand):
    """
    store curr tournament obj, chessid
    execute register_player in tournament, return context screen
    """
    def __init__(self, tournament, chess_id):
        self.tournament = tournament
        self.chess_id = chess_id

    def execute(self):
        self.tournament.register_player(self.chess_id)
        return Context("tournament-view", tournament=self.tournament)
