from commands.base import BaseCommand
from models import TournamentManager
from commands.context import Context


class TournamentListCmd(BaseCommand):

    def execute(self):
        """
        use manager to load and build tournaments from .json
        sorted_by_start_date in tournament_manager
        """
        manager = TournamentManager()
        in_progress = manager.in_progress()

        # if only one tournamnet return to tournament context screen
        if len(in_progress) == 1:
            return Context("tournament-view", tournament=in_progress[0])

        #  1 > list sorted tournaments return to main menu context screen
        tournaments = manager.sorted_by_start_date()
        return Context("tournament-main-menu", tournaments=tournaments)
