
game_is_not_over = True
player_whose_turn_it_is = 1

board_state = [None] * 9  # row-major order

difficulty_weights = {
    "easy": (
        [1, 1, 1, 2, 2, 2],  # player 1 twice as likely to roll 4-6 as 1-3
        [2, 2, 2, 1, 1, 1],  # player 2 twice as likely to roll 1-3 as 4-6
    ),  
    "normal": (None, None),  # dice are not weighted
    "hard": (
        [2, 2, 2, 1, 1, 1],  # player 1 twice as likely to roll 1-3 as 4-6
        [1, 1, 1, 2, 2, 2],  # player 2 twice as likely to roll 4-6 as 1-3
    ),
}


def game_is_over(board_state):
    return None not in board_state


def normalize(ls):
    """Normalizes the values in `ls` so they sum up to 1."""
    total = sum(ls)
    return [x / total for x in ls]


def dice_roll(weighting=None):
    """Roll a standard six-sided die, optionally weighted."""
    weighting = normalize(weighting)
    rolled_value = None  # TODO: roll the die
    return rolled_value


def next_player(active_player):
    """Return who has the next turn."""
    if active_player == 0:
        return 1
    elif active_player == 1:
        return 0
    else:
        return None  # TODO: randomly select


def player_takes_their_turn(board_state, active_player):
    roll = dice_roll()

    return board_state, next_player(active_player)


active_player = None
while game_is_active:
    active_player = next_player(active_player)
    (board_state, active_player) = player_takes_their_turn(board_state, active_player)
    game_is_active = not game_is_over(board_state)





    
