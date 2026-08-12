from ..base_screen import BaseScreen
from datetime import datetime
from commands.tournaments import TournamentCreateCmd


class TournamentCreate(BaseScreen):
    """ screen displayed when creating a new tournament """
    display = "## Create tournament"

    def input_date(self, prompt):
        """ mirrors BaseScreen.input_birthday """
        while True:
            value = self.input_string(prompt=prompt)
            try:
                datetime.strptime(value, "%d-%m-%Y")
                return value
            except ValueError:
                print("Please provide a valid date (dd-mm-yyyy)!")

    def get_command(self):
        name = self.input_string("Tournament name", empty=True)
        venue = self.input_string("Venue", empty=True)
        date_from = self.input_date("Start date (dd-mm-yyyy)")
        date_to = self.input_date("End date (dd-mm-yyyy)")

        while True:
            rounds = self.input_string("Number of rounds", default="4")
            if rounds.isdigit() and int(rounds) > 0:
                rounds = int(rounds)
                break
            print("Please enter a positive whole number.")

        return TournamentCreateCmd(name, venue, date_from, date_to, rounds)
