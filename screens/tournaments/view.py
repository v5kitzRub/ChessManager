from ..base_screen import BaseScreen
from commands.tournaments import TournamentListCmd
from commands import ExitCmd, NoopCmd


class TournamentView(BaseScreen):
    """ main screen for a single tournament """
    def __init__(self, tournament):
        self.tournament = tournament

    def display(self):
        t = self.tournament
        print("##", t.name)
        print("Venue:", t.venue)
        print("Dates:", t.date_from, "-", t.date_to)
        print("Players registered:", len(t.players))
        print("Rounds:", f"{t.current_round or 0}/{t.number_of_rounds}")
        if t.completed:
            print("Status: COMPLETED")
        elif t.is_started:
            print("Status: round", t.current_round, "in progress")
        else:
            print("Status: not started")

    def get_command(self):
        t = self.tournament
        while True:
            if t.completed:
                print("Type R to view the final report.")
            else:
                if not t.is_started:
                    print("Type P to register a player.")
                    print("Type S to start the tournament (first round).")
                else:
                    if t.current_round_obj and not t.current_round_obj.is_complete:
                        print("Type E to enter results for the current round.")
                    else:
                        print("Type N to move to the next round (or finish the tournament).")
                    print("Type R to view the report so far.")
            print("Type B to go back to the tournament list.")
            print("Type X to exit.")

            value = self.input_string().upper()

            if value == "B":
                return TournamentListCmd()
            elif value == "X":
                return ExitCmd()
            elif value == "P" and not t.is_started:
                return NoopCmd("tournament-register-player", tournament=t)
            elif value == "S" and not t.is_started:
                return NoopCmd("tournament-advance-round", tournament=t)
            elif value == "E" and t.is_started and not t.completed:
                return NoopCmd("tournament-enter-results", tournament=t)
            elif value == "N" and t.is_started and not t.completed:
                return NoopCmd("tournament-advance-round", tournament=t)
            elif value == "R" and (t.is_started or t.completed):
                return NoopCmd("tournament-report", tournament=t)
