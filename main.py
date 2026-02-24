from blueberrybush import BlueberryBush
from deerherd import DeerHerd
from bearden import BearDen
from player import Player

FOREST_SIZE = 5


def create_forest() -> list[list[ForestPatch]]:
    """Create a 5x5 forest grid of empty ForestPatch objects."""999
    forest: list[list[ForestPatch]] = []
    for _ in range(FOREST_SIZE):
        row: list[forestPatch] = []
        for _ in range(FOREST_SIZE):
            row.append(forestPatch())
        forest.append(row)
    return forest


def place_fixed_events(forest: list[list[ForestPatch]]) -> None:
    """Place the pond, blueberry bushes, and deer herd in fixed positions."""
    forest[0][0].set_event(BlueberryBush())
    forest[0][FOREST_SIZE - 1].set_event(Pond())
    forest[FOREST_SIZE - 1][FOREST_SIZE - 1].set_event(BlueberryBush())
    forest[FOREST_SIZE - 1][0].set_event(DeerHerd())


def place_bear_dens(forest: list[list[ForestPatch]]) -> None:
    """Place three bear dens in random empty forest patches."""
    empty_positions: list[tuple[int, int]] = []
    for row in range(FOREST_SIZE):
        for col in range(FOREST_SIZE):
            if forest[row][col].is_empty():
                empty_positions.append((row, col))
    bear_positions = random.sample(empty_positions, 3)
    for row, col in bear_positions:
        forest[row][col].set_event(BearDen())


def print_forest(forest: list[list[ForestPatch]], player: Player) -> None:
    """Print the forest grid with the player's position."""
    print("-" * (FOREST_SIZE * 3 + 1))
    for row in range(FOREST_SIZE):
        row_str = "|"
        for col in range(FOREST_SIZE):
            coords = player.get_coordinates()
            if coords.row == row and coords.column == col:
                player_char = "*"
            else:
                player_char = " "
            event_char = forest[row][col].get_symbol()
            row_str += player_char + event_char + "|"
        print(row_str)
        print("-" * (FOREST_SIZE * 3 + 1))


def main() -> None:
    # TODO Remove pass below, and write your main function here.
    # Remember to obey the course's style and design guide. Don't put too
    # much code here.
    forest = create_forest()
    place_fixed_events(forest)
    place_bear_dens(forest)
    player = Player()
    print_forest(forest, player)


if _name_ == '_main_':
    main()