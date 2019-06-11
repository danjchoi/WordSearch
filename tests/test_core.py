"""Unit tests for the core module."""


# [-Imports:Python-]
import string

# [-Imports:Project-]
from wordsearch import core


# [-Internals-]
def _graph_is_valid(graph, *, num_rows, num_cols):
    """
    Return True if the graph is valid.

    Valid has the following constraints:
    * There are num_rows rows
    * There are num_cols columns
    * Each item in the grid is a lowercase letter
    """
    if len(graph) != num_rows:
        return False
    for row in graph:
        if len(row) != num_cols:
            return False
        row_string = "".join(row)
        if not row_string.isalpha() or not row_string.islower():
            return False
    return True


# [-Public-]
def test_square_graph():
    """Test that a square graph is valid."""
    # Given
    num_rows = 10
    num_cols = 10

    # When
    graph = core.generate_graph(num_rows=num_rows, num_cols=num_cols)

    # Then
    assert _graph_is_valid(graph, num_rows=num_rows, num_cols=num_cols)


def test_tall_graph():
    """Test that a graph with more rows than columns is valid."""
    # Given
    num_rows = 10
    num_cols = 1

    # When
    graph = core.generate_graph(num_rows=num_rows, num_cols=num_cols)

    # Then
    assert _graph_is_valid(graph, num_rows=num_rows, num_cols=num_cols)


def test_wide_graph():
    """Test that a graph with more columns than rows is valid."""
    # Given
    num_rows = 1
    num_cols = 10

    # When
    graph = core.generate_graph(num_rows=num_rows, num_cols=num_cols)

    # Then
    assert _graph_is_valid(graph, num_rows=num_rows, num_cols=num_cols)


def test_graph_no_words():
    """Test that no words are found in a graph with no words."""
    # Given
    graph = [["x", "x", "x"], ["x", "x", "x"], ["x", "x", "x"]]
    known_words = ["a", "quick", "brown", "fox"]
    expected_found_words = set()

    # When
    found_words = core.find_words(graph, known_words=known_words)

    # Then
    assert found_words == expected_found_words


def test_graph_several_words():
    """Test that all words are found in a graph with several words."""
    # Given
    graph = [["t", "a", "b"], ["k", "o", "o"], ["o", "l", "p"]]
    known_words = ["a", "boo", "boop", "bop", "cat", "dog", "cool", "pot", "tab", "top"]
    expected_found_words = set(["a", "boo", "bop", "pot", "tab", "top"])

    # When
    found_words = core.find_words(graph, known_words=known_words)

    # Then
    assert found_words == expected_found_words
