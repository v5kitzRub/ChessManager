from ..base_screen import BaseScreen
from models import build_player_index
from commands.tournaments import TournamentRegisterPlayerCmd


class TournamentRegisterPlayer(BaseScreen):
    """ screen to register an existing club player into tournament by Chess ID """
    def __init__(self, tournament):
        self.tournament = tournament
        self.player_index = build_player_index()

    def display(self):
        print("##", self.tournament.name, "- register a player")
        print("Enter the Chess ID of a player from any club.")
        print("Already registered:")
        for chess_id in self.tournament.players:
            player = self.player_index.get(chess_id)
            label = player.name if player else chess_id
            print(" -", label, f"({chess_id})")

    def get_command(self):
        while True:
            chess_id = self.input_chess_id(prompt="Player Chess ID")

            if chess_id not in self.player_index:
                print("No player with that Chess ID was found in any club.")
                continue
            if chess_id in self.tournament.players:
                print("That player is already registered in this tournament.")
                continue

            return TournamentRegisterPlayerCmd(self.tournament, chess_id)
