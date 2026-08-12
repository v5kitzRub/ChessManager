from .club_manager import ClubManager


def build_player_index(club_manager=None):
    """ index dict maps chess_id to player ref clubs """
    club_manager = club_manager or ClubManager()
    index = {}
    for club in club_manager.clubs:
        for player in club.players:
            index[player.chess_id] = player
    return index


def find_player(chess_id, club_manager=None):
    """ Return the Player with this chess_id None if not found """
    return build_player_index(club_manager).get(chess_id)
