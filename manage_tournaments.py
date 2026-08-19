from commands.tournaments import TournamentListCmd
from screens.tournaments import (
    TournamentMainMenu,
    TournamentCreate,
    TournamentView,
    TournamentRegisterPlayer,
    TournamentAdvanceRound,
    TournamentEnterResults,
    TournamentReport,
)


class TournamentApp:
    """The main controller for the tournament management program."""

    # map screen name to screen class
    SCREENS = {
        "tournament-main-menu": TournamentMainMenu,
        "tournament-create": TournamentCreate,
        "tournament-view": TournamentView,
        "tournament-register-player": TournamentRegisterPlayer,
        "tournament-advance-round": TournamentAdvanceRound,
        "tournament-enter-results": TournamentEnterResults,
        "tournament-report": TournamentReport,
        "exit": False,
    }

    def __init__(self):
        # load tournaments, sets start screen
        command = TournamentListCmd()
        # returns context screen
        self.context = command()

    # program loop
    def run(self):
        # while current context screen = true, loop
        while self.context.run:
            # match current screen contexrt with screen class
            screen = self.SCREENS[self.context.screen]
            try:
                command = screen(**self.context.kwargs).run()
                self.context = command()
            except KeyboardInterrupt:
                print("Bye!")
                self.context.run = False


if __name__ == "__main__":
    app = TournamentApp()
    app.run()
