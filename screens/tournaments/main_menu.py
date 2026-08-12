from ..base_screen import BaseScreen
from commands import ExitCmd, NoopCmd


class TournamentMainMenu(BaseScreen):
    """ display list of tournaments sorted by descending start date or no tournaments """
    def __init__(self, tournaments):
        self.tournaments = tournaments

    def display(self):
        if not self.tournaments:
            print("No tournaments yet.")

        # loop list and print tournament in format
        for idx, tournament in enumerate(self.tournaments, 1):
            status = "completed" if tournament.completed else "in progress" if tournament.is_started else "not started"
            print(f"{idx}. {tournament.name} ({tournament.date_from} - {tournament.date_to}) [{status}]")

    def get_command(self):
        while True:
            print("Type C to create a tournament or a tournament number to view/manage it.")
            print("Type X to exit.")
            value = self.input_string()
            if value.isdigit():
                value = int(value)
                if value in range(1, len(self.tournaments) + 1):
                    return NoopCmd("tournament-view", tournament=self.tournaments[value - 1])
            elif value.upper() == "C":
                return NoopCmd("tournament-create")
            elif value.upper() == "X":
                return ExitCmd()
