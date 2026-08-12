from pathlib import Path
from .tournament import Tournament
from utils import iter_json_files
import json
from datetime import datetime


class TournamentManager:
    """
    Loads tournament .json file from 'data_folder'
    Mirrors models.club_manager.ClubManager to create
    """
    def __init__(self, data_folder="P3-Application-Developer-Skills-Bootcamp/data/tournaments"):
        self.data_folder = Path(data_folder)
        self.tournaments = []
        for filepath in iter_json_files(self.data_folder):
            try:
                self.tournaments.append(Tournament.load(filepath))
            except (json.JSONDecodeError, KeyError):
                print(filepath, "is not a valid tournament file.")

    def create(self, name, venue, date_from, date_to, number_of_rounds=4):
        filepath = self.data_folder / (name.replace(" ", "") + ".json")
        tournament = Tournament(
            name=name,
            venue=venue,
            date_from=date_from,
            date_to=date_to,
            number_of_rounds=number_of_rounds,
            filepath=filepath,
        )
        tournament.save()
        self.tournaments.append(tournament)
        return tournament

    def in_progress(self):
        """ tournaments started but not completed """
        return [t for t in self.tournaments if t.is_started and not t.completed]

    def sorted_by_start_date(self):
        """ tournaments sorted by descending start date recent/upcoming first """
        return sorted(
            self.tournaments,
            key=lambda t: datetime.strptime(t.date_from, Tournament.DATE_FORMAT),
            reverse=True,
        )
