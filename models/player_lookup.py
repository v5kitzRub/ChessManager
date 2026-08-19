from .club_manager import ClubManager


def build_player_index(club_manager=None):
    """ index dict maps chess_id to player ref clubs """
    # use clubmanager
    club_manager = club_manager or ClubManager()
    index = {}
    # loop each club loaded from clubmanager
    for club in club_manager.clubs:
        # loop each player in each club
        for player in club.players:
            # map chess id to player obj
            index[player.chess_id] = player
    return index


def find_player(chess_id, club_manager=None):
    """ Return the Player with this chess_id None if not found """
    # build player club roster by index match chessid
    return build_player_index(club_manager).get(chess_id)
