# Workshop


def build_initial_field(rows_count, columns_count):
    return [[None] * columns_count for _ in range(rows_count)]


def print_field(field):
    [print(row) for row in field]


def print_winner(player):
    print(f'Player {player} wins!')


def get_player_move(player):
    player_move_str = input(f'Player {player}, please choose a column: ')
    player_move = int(player_move_str)
    return player_move - 1


def apply_player_move_gen(max_row, columns_count, player):
    free_bottom_row_indices = [max_row] * columns_count

    def apply_player_move_internal(field, player_move):
        print(free_bottom_row_indices)

    return apply_player_move_internal


def is_win_condition(field):
    pass


def play(field):
    current_player, other_player = 1, 2
    while 1:
        player_move = get_player_move(current_player)
        apply_player_move(field, player_move)

        if is_win_condition(field):
            break
        else:
            current_player, other_player = other_player, current_player

    print_winner(current_player)


field = build_initial_field(6, 7)
play(field)

# -2:44:43




















