from .match import Match


class Round:
    """ round obj is list of matchup instances """

    def __init__(self, matches=None):
        # list of current matchup obj for current round
        self.matches = matches or []

    def __iter__(self):
        # loop matches from round
        return iter(self.matches)

    def __len__(self):
        # len(round) returns number of matchups per round
        return len(self.matches)

    @property
    def is_complete(self):
        """ round is complete once every match in it has a result """
        return bool(self.matches) and all(m.completed for m in self.matches)

    def pending_matches(self):
        """ list matched not competed """
        return [m for m in self.matches if not m.completed]

    def serialize(self):
        """ format for .json """
        return [m.serialize() for m in self.matches]

    @classmethod
    def from_list(cls, data):
        """ rebuild from .json """
        return cls([Match.from_dict(m) for m in data])
