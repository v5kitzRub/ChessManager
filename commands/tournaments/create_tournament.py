from commands.base import BaseCommand
from models import TournamentManager
from commands.context import Context


class TournamentCreateCmd(BaseCommand):
    """ store curr input data, execute create with data in tournament_manager, return tournament context screen """
    def __init__(self, name, venue, date_from, date_to, number_of_rounds):
        self.name = name
        self.venue = venue
        self.date_from = date_from
        self.date_to = date_to
        self.number_of_rounds = number_of_rounds

    def execute(self):
        # loads tournaments.json list
        manager = TournamentManager()
        # create tournament and add to list with other tournaments
        tournament = manager.create(
            name=self.name,
            venue=self.venue,
            date_from=self.date_from,
            date_to=self.date_to,
            number_of_rounds=self.number_of_rounds,
        )
        # return to new tournament view
        return Context("tournament-view", tournament=tournament)
