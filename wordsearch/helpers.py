"""A library of helper functions for the core module."""


# [-Internals-]
def _get_horizontal_strings(graph):
    """Get a list of strings running horizontally in the graph."""
    horizontal_strings = []
    for row in graph:
        horizontal_strings.append("".join(row))
    return horizontal_strings


def _get_vertical_strings(graph):
    """Get a list of strings running vertically in the graph."""
    vertical_strings = []
    for col in range(len(graph[0])):
        vertical_strings.append("".join(row[col] for row in graph))
    return vertical_strings


def _get_diagonal_string(graph, *, row_start, col_start, row_step, col_step):
    """Get the string of a diagonal given a starting point and the intended row and column steps."""
    diagonal_string = ""
    current_row = row_start
    current_col = col_start
    while (
        current_row < len(graph)
        and current_col < len(graph[current_row])
        and 0 <= current_col
    ):
        diagonal_string += graph[current_row][current_col]
        current_row += row_step
        current_col += col_step
    return diagonal_string


def _get_northwest_diagonal_strings(graph):
    """Get a list of strings running diagonally from NW to SE."""
    row_step = 1
    col_step = 1
    diagonal_strings = []
    # Center diagonal
    # oxx
    # xox
    # xxo
    diagonal_strings.append(
        _get_diagonal_string(
            graph, row_start=0, col_start=0, row_step=row_step, col_step=row_step
        )
    )
    # Diagonals below center diagonal
    # xxx
    # oxx
    # oox
    for row_start in range(1, len(graph)):
        diagonal_strings.append(
            _get_diagonal_string(
                graph,
                row_start=row_start,
                col_start=0,
                row_step=row_step,
                col_step=col_step,
            )
        )
    # Diagonals above center diagonal
    # xoo
    # xxo
    # xxx
    for col_start in range(1, len(graph[0])):
        diagonal_strings.append(
            _get_diagonal_string(
                graph,
                row_start=0,
                col_start=col_start,
                row_step=row_step,
                col_step=col_step,
            )
        )
    return diagonal_strings


def _get_northeast_diagonal_strings(graph):
    """Get a list of strings running diagonally from NE to SW."""
    row_step = 1
    col_step = -1
    diagonal_strings = []
    # Center diagonal
    # xxo
    # xox
    # oxx
    diagonal_strings.append(
        _get_diagonal_string(
            graph,
            row_start=0,
            col_start=len(graph[0]) - 1,
            row_step=row_step,
            col_step=col_step,
        )
    )
    # Diagonals below center diagonal
    # xxx
    # xxo
    # xoo
    for row_start in range(1, len(graph)):
        diagonal_strings.append(
            _get_diagonal_string(
                graph,
                row_start=row_start,
                col_start=len(graph[0]) - 1,
                row_step=row_step,
                col_step=col_step,
            )
        )
    # Diagonals above center diagonal
    # oox
    # oxx
    # xxx
    for col_start in range(len(graph[0]) - 2, -1, -1):
        diagonal_strings.append(
            _get_diagonal_string(
                graph,
                row_start=0,
                col_start=col_start,
                row_step=row_step,
                col_step=col_step,
            )
        )
    return diagonal_strings


def _find_known_words_in_strings(strings_to_look_at, *, known_words):
    """Return all known words found in the strings and their reversed counterparts in strings_to_look_at."""
    found_words = []
    for this_string in strings_to_look_at:
        this_string_reversed = "".join(reversed(this_string))
        for word in known_words:
            if word not in found_words and (
                word in this_string or word in this_string_reversed
            ):
                found_words.append(word)
    return found_words


# [-Public-]
def find_horizontal_words(graph, *, known_words):
    """Find all instances of words in known_words that occur in rows."""
    strings_to_look_at = _get_horizontal_strings(graph)
    found_words = _find_known_words_in_strings(
        strings_to_look_at, known_words=known_words
    )
    return found_words


def find_vertical_words(graph, *, known_words):
    """Find all instances of words in known_words that occur in columns."""
    strings_to_look_at = _get_vertical_strings(graph)
    found_words = _find_known_words_in_strings(
        strings_to_look_at, known_words=known_words
    )
    return found_words


def find_diagonal_words(graph, *, known_words):
    """Find all instances of words in known_words that occur in diagonals."""
    strings_to_look_at = _get_northwest_diagonal_strings(graph)
    strings_to_look_at += _get_northeast_diagonal_strings(graph)
    found_words = _find_known_words_in_strings(
        strings_to_look_at, known_words=known_words
    )
    return found_words
