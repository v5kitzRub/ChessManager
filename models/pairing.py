"""
Matchmaking rules, implementing matchmaking.md
"""
import random


def generate_first_round_pairs(players):
    """ random shuffle players list in (1v2)(3v4) """
    # copy players list
    shuffled = list(players)
    # random order players
    random.shuffle(shuffled)
    # pair players grouped by 2
    return list(zip(shuffled[0::2], shuffled[1::2]))


def rank_players(players, points):
    """
    groups dict maps chess_id to total tournament points so far

    Returns players sorted by points descending. Players tied
    are shuffled randomly
    """
    # group players by point total
    groups = {}
    for player in players:
        # append player into matching points group
        groups.setdefault(points[player], []).append(player)

    ranked = []
    # loop each group by points highest to lowest
    for score in sorted(groups, reverse=True):
        group = groups[score]
        # players with similar score are random shuffled
        random.shuffle(group)
        # append shuffled group to ranking
        ranked.extend(group)
    return ranked


def generate_next_round_pairs(players, points, already_played):
    """
    already_played: set of frozenset pairs that have
    already faced each other in a previous round

    If every remaining player has already been played the next available
    player is used anyway rather than leaving someone unpaired
    """
    # ordered players by points highest to lowest
    remaining = rank_players(players, points)
    pairs = []

    # while players still in remaining
    while remaining:
        # take highest point player as p1
        player1 = remaining.pop(0)
        # if odd players unable to pair
        if not remaining:
            break
        # loop next remaining players not played vs p1 if none set index0
        opponent_index = next(
            (
                idx
                for idx, player2 in enumerate(remaining)
                if frozenset((player1, player2)) not in already_played
            ),
            0,
        )
        # take chosen opponent player as p2
        player2 = remaining.pop(opponent_index)
        # append players to pairs list
        pairs.append((player1, player2))
    return pairs


def match_history(rounds):
    """ set for pairs of players that completed matchups """
    # build set of frozensets, for players faced each other
    played = set()
    for round_ in rounds:
        for match in round_:
            # save order independent records of played history
            played.add(frozenset(match.players))
    return played
