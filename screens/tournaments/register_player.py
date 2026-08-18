from ..base_screen import BaseScreen
from commands import NoopCmd
from models import build_player_index
from commands.tournaments import TournamentRegisterPlayerCmd


class TournamentRegisterPlayer(BaseScreen):
    """ screen to register an existing club player into tournament by search or list"""
    def __init__(self, tournament):
        self.tournament = tournament
        self.player_index = build_player_index()

    def display(self):
        print("##", self.tournament.name, "- register a player")
        print("Already registered:")
        if not self.tournament.players:
            print(" - (No registered players)")
        for chess_id in self.tournament.players:
            player = self.player_index.get(chess_id)
            label = player.name if player else chess_id
            print(" -", label, f"({chess_id})")

    def get_command(self):
        while True:
            print("Type 'L' to view the list of all available players.")
            print("Type 'N' to search for a player by name.")
            print("Type 'I' to search for a player by Chess ID.")
            print("Type 'B' to go back to the tournament view.")

            choice = self.input_string().upper()

            if choice == "B":
                return NoopCmd("tournament-view", tournament=self.tournament)
            elif choice == "L":
                command = self._select_player(self._available_players())
                if command:
                    return command
            elif choice == "N":
                command = self._search_by_name()
                if command:
                    return command
            elif choice == "I":
                command = self._search_by_chess_id()
                if command:
                    return command
            else:
                print("Invalid option.")

    def _available_players(self):
        """ all club players not yet registered in this tournament sorted by name."""
        players = [
            player
            for chess_id, player in self.player_index.items()
            if chess_id not in self.tournament.players
        ]
        return sorted(players, key=lambda p: p.name.lower())

    def _search_by_name(self):
        query = self.input_string(prompt="Name contains", empty=True)
        matches = [p for p in self._available_players() if query.lower() in p.name.lower()]
        if not matches:
            print("No available players found matching that name.")
            return None
        return self._select_player(matches)

    def _search_by_chess_id(self):
        chess_id = self.input_chess_id(prompt="Player Chess ID")
        if chess_id not in self.player_index:
            print("No player with that Chess ID was found in any club.")
            return None
        if chess_id in self.tournament.players:
            print("That player is already registered in this tournament.")
            return None
        return TournamentRegisterPlayerCmd(self.tournament, chess_id)

    def _select_player(self, players):
        """ displays a numbered list of players and lets the user pick one to register """
        if not players:
            print("No available players to register.")
            return None

        for idx, player in enumerate(players, 1):
            print(idx, player.name, f"({player.chess_id})")
        print("Enter a number to register that player or 'B' to go back.")

        while True:
            value = self.input_string()
            if value.upper() == "B":
                return None
            if value.isdigit() and 1 <= int(value) <= len(players):
                player = players[int(value) - 1]
                return TournamentRegisterPlayerCmd(self.tournament, player.chess_id)
            print("Invalid selection.")
