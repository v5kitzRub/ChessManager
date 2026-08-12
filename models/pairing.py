"""
Matchmaking rules, implementing matchmaking.md
"""
import random


def generate_first_round_pairs(players):
    """ random shuffle players list in (1v2)(3v4) """
    shuffled = list(players)
    random.shuffle(shuffled)
    return list(zip(shuffled[0::2], shuffled[1::2]))


def rank_players(players, points):
    """
    groups dict maps chess_id to total tournament points so far

    Returns players sorted by points descending. Players tied
    are shuffled randomly
    """
    groups = {}
    for player in players:
        groups.setdefault(points[player], []).append(player)

    ranked = []
    for score in sorted(groups, reverse=True):
        group = groups[score]
        random.shuffle(group)
        ranked.extend(group)
    return ranked


def generate_next_round_pairs(players, points, already_played):
    """
    already_played: set of frozenset pairs that have
    already faced each other in a previous round

    If every remaining player has already been played the next available
    player is used anyway rather than leaving someone unpaired
    """
    remaining = rank_players(players, points)
    pairs = []

    while remaining:
        player1 = remaining.pop(0)
        if not remaining:
            break
        opponent_index = next(
            (
                idx
                for idx, player2 in enumerate(remaining)
                if frozenset((player1, player2)) not in already_played
            ),
            0,
        )
        player2 = remaining.pop(opponent_index)
        pairs.append((player1, player2))
    return pairs


def match_history(rounds):
    """ set for pairs of players that completed matchups """
    played = set()
    for round_ in rounds:
        for match in round_:
            played.add(frozenset(match.players))
    return played
