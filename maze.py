"""Implemention of the Maze ADT using a 2-D array."""

from arrays import Array2D
from lliststack import Stack
#import tkinter as tk
#from visualizer import run


class Maze:
    """Define constants to represent contents of the maze cells."""
    MAZE_WALL = "*"
    PATH_TOKEN = "x"
    TRIED_TOKEN = "o"

    def __init__(self, num_rows, num_cols):
        """Creates a maze object with all cells marked as open."""
        #print(num_rows, num_cols)
        self._maze_cells = Array2D(num_rows, num_cols)
        self._start_cell = None
        self._exit_cell = None

    def num_rows(self):
        """Returns the number of rows in the maze."""
        return self._maze_cells.num_rows()

    def num_cols(self):
        """Returns the number of columns in the maze."""
        return self._maze_cells.num_cols()

    def set_wall(self, row, col):
        """Fills the indicated cell with a "wall" marker."""
        assert row >= 0 and row < self.num_rows() and \
               col >= 0 and col < self.num_cols(), f"Cell index out of range."
        self._maze_cells[row, col] = self.MAZE_WALL

    def set_start(self, row, col):
        """Sets the starting cell position."""
        assert row >= 0 and row < self.num_rows() and \
               col >= 0 and col < self.num_cols(), "Cell index out of range."
        self._start_cell = _CellPosition(row, col)

    def set_exit(self, row, col):
        """Sets the exit cell position."""
        assert row >= 0 and row < self.num_rows() and \
               col >= 0 and col < self.num_cols(), "Cell index out of range."
        self._exit_cell = _CellPosition(row, col)


    def find_path(self):
        """
        Attempts to solve the maze by finding a path from the starting cell
        to the exit. Returns True if a path is found and False otherwise.
        """
        # Create an empty stack
        stack = Stack()
        # Push the starting state onto the stack
        stack.push(self._start_cell)
        # self.display_list = []
        # While the stack is not empty
        visited_stack =  Stack()
        while not stack.is_empty():
        #   Pop the stack and examine the state
            # self.display_list.append(str(self))
            state = stack.pop()
            if self._exit_found(state.row, state.col):
                coords_list = []
                probe = visited_stack.pop()
                self._mark_path(self._exit_cell.row, self._exit_cell.col)
                # self.display_list.append(str(self))
                while not visited_stack.is_empty():# and len(visited_stack) != 1:
                    prev = visited_stack.peek()
                    if probe._adjacent(prev):
                        coords_list.append(probe)
                        probe = visited_stack.pop()

                    else:
                        visited_stack.pop()
                for i in coords_list:
                    self._mark_path(i.row, i.col)
                    # self.display_list.append(str(self))
                self._mark_path(self._start_cell.row, self._start_cell.col)

                # self.display_list.append(str(self))
                #run(# self.display_list)
                return True

        #   Else if the state has not been visited previously
            elif self._maze_cells[state.row, state.col] != self.TRIED_TOKEN:
        #       Mark the state as visited
                visited_stack.push(_CellPosition(state.row, state.col))
                self._mark_tried(state.row, state.col)
        #       Push onto the stack all unvisited adjacent states
                if self._valid_move(state.row, state.col - 1) \
                   and self._maze_cells[state.row, state.col - 1] != self.TRIED_TOKEN:

                    stack.push(_CellPosition(state.row, state.col - 1))
                    # print("left")
                if self._valid_move(state.row + 1, state.col) \
                   and self._maze_cells[state.row + 1, state.col] != self.TRIED_TOKEN:

                    stack.push(_CellPosition(state.row + 1, state.col))
                    # print("down")
                if self._valid_move(state.row, state.col + 1) \
                   and self._maze_cells[state.row, state.col + 1] != self.TRIED_TOKEN:

                    stack.push(_CellPosition(state.row, state.col + 1))
                    # print("right")
                if self._valid_move(state.row - 1, state.col) \
                   and self._maze_cells[state.row - 1, state.col] != self.TRIED_TOKEN:

                    stack.push(_CellPosition(state.row - 1, state.col))
                    # print("up")



            ## print(self, "\n")


        # Return UNSUCCESSFUL CONCLUSION
        return False


    def reset(self):
        """Resets the maze by removing all "path" and "tried" tokens."""
        for i in range(self.num_rows()):
            for j in range(self.num_cols()):
                cell = self._maze_cells[i, j]
                if cell == "*":
                    pass
                else:
                    self._maze_cells[i, j] = None

    def __str__(self):
        """Returns a text-based representation of the maze."""
        str_lst = []
        for i in range(self.num_rows()):
            strng = ""
            for j in range(self.num_cols()):
                try:
                    cell = self._maze_cells[i, j]
                except IndexError:
                    print(i, j)
                if cell == "*":
                    strng += "* "
                elif cell == None:
                    strng += "- " # change for _ later
                elif cell == "o":
                    strng += "o "
                elif cell == "x":
                    strng += "x "
            str_lst.append(strng)

        ## print((self._maze_cells))
        return "\n".join(str_lst)


    def _valid_move(self, row, col):
        """Returns True if the given cell position is a valid move."""
        return row >= 0 and row < self.num_rows() \
               and col >= 0 and col < self.num_cols() \
               and self._maze_cells[row, col] is None

    def _exit_found(self, row, col):
        """Helper method to determine if the exit was found."""
        return row == self._exit_cell.row and col == self._exit_cell.col

    def _mark_tried(self, row, col):
        """Drops a "tried" token at the given cell."""
        self._maze_cells[row, col] = self.TRIED_TOKEN

    def _mark_path(self, row, col):
        """Drops a "path" token at the given cell."""
        self._maze_cells[row, col] = self.PATH_TOKEN



class _CellPosition(object):
    """Private storage class for holding a cell position."""
    def __init__(self, row, col):
        self.row = row
        self.col = col
    def _adjacent(self, __o):
        row, col = __o.row, __o.col
        return (self.row, self.col) in \
                                [(row, col - 1),
                                 (row + 1, col),
                                 (row, col + 1),
                                 (row - 1, col)]

