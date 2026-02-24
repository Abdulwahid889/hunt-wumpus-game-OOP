# A Coordinates object represents a row, column pair. That is, it represents
# a specific space on the simulation grid. row=0 designates the top row.
# row=4 designates the bottom row. column=0 designates the leftmost column.
# column=4 designates the rightmost column.
class Coordinates:
    # This attribute records a row index in the simulation grid. 0 corresponds
    # to the top row in the grid. 4 corresponds to the bottom row.
    row: int
    
    # This attribute records a column index in the simulation grid. 0
    # corresponds to the leftmost column in the grid. 4 corresponds to the
    # rightmost column.
    column: int

    def __init__(self, row: int, column: int) -> None:
        self.row = row
        self.column = column
