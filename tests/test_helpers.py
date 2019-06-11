"""Unit tests for the helpers library."""


# [-Imports:Project-]
from wordsearch import core
from wordsearch import helpers


# [-Tests-]
def test_forwards_horizontal_word():
    """Test that a horizontal word spelled forwards can be found."""
    # Given
    graph = [["t", "o", "p"], ["x", "x", "x"], ["x", "x", "x"]]
    known_words = ["top", "foo", "bar"]

    # When
    found_words = helpers.find_horizontal_words(graph, known_words=known_words)

    # Then
    assert found_words == ["top"]


def test_backwards_horizontal_word():
    """Test that a horizontal word spelled backwards can be found."""
    # Given
    graph = [["p", "o", "t"], ["x", "x", "x"], ["x", "x", "x"]]
    known_words = ["top", "foo", "bar"]

    # When
    found_words = helpers.find_horizontal_words(graph, known_words=known_words)

    # Then
    assert found_words == ["top"]


def test_forwards_and_backwards_horizontal_word():
    """Test that words spelled forwards and backwards can be found simultaneously, even if they're in the same row."""
    # Given
    graph = [["t", "o", "p"], ["x", "x", "x"], ["x", "x", "x"]]
    known_words = ["top", "pot", "foo", "bar"]

    # When
    found_words = helpers.find_horizontal_words(graph, known_words=known_words)
    found_words.sort()

    # Then
    assert found_words == ["pot", "top"]


def test_down_vertical_word():
    """Test that a vertical word spelled down can be found."""
    # Given
    graph = [["t", "x", "x"], ["o", "x", "x"], ["p", "x", "x"]]
    known_words = ["top", "foo", "bar"]

    # When
    found_words = helpers.find_vertical_words(graph, known_words=known_words)

    # Then
    assert found_words == ["top"]


def test_up_vertical_word():
    """Test that a vertical word spelled up can be found."""
    # Given
    graph = [["p", "x", "x"], ["o", "x", "x"], ["t", "x", "x"]]
    known_words = ["top", "foo", "bar"]

    # When
    found_words = helpers.find_vertical_words(graph, known_words=known_words)

    # Then
    assert found_words == ["top"]


def test_up_and_down_vertical_word():
    """Test that words spelled up and down can be found simultaneously, even if they're in the same column."""
    # Given
    graph = [["t", "x", "x"], ["o", "x", "x"], ["p", "x", "x"]]
    known_words = ["top", "pot", "foo", "bar"]

    # When
    found_words = helpers.find_vertical_words(graph, known_words=known_words)
    found_words.sort()

    # Then
    assert found_words == ["pot", "top"]


def test_forwards_northwest_diagonal_word():
    """Test that a northwest diagonal word spelled forwards can be found."""
    # Given
    graph = [["t", "x", "x"], ["x", "o", "x"], ["x", "x", "p"]]
    known_words = ["top", "foo", "bar"]

    # When
    found_words = helpers.find_diagonal_words(graph, known_words=known_words)

    # Then
    assert found_words == ["top"]


def test_backwards_northwest_diagonal_word():
    """Test that a northwest diagonal word spelled backwards can be found."""
    # Given
    graph = [["p", "x", "x"], ["x", "o", "x"], ["x", "x", "t"]]
    known_words = ["top", "foo", "bar"]

    # When
    found_words = helpers.find_diagonal_words(graph, known_words=known_words)

    # Then
    assert found_words == ["top"]


def test_forwards_and_backwards_northwest_diagonal_word():
    """Test that words spelled forwards and backwards can be found simultaneously, even if they're in the same northwest diagonal."""
    # Given
    graph = [["t", "x", "x"], ["x", "o", "x"], ["x", "x", "p"]]
    known_words = ["top", "pot", "foo", "bar"]

    # When
    found_words = helpers.find_diagonal_words(graph, known_words=known_words)
    found_words.sort()

    # Then
    assert found_words == ["pot", "top"]


def test_forwards_northeast_diagonal_word():
    """Test that a northeast diagonal word spelled forwards can be found."""
    graph = [["x", "x", "t"], ["x", "o", "x"], ["p", "x", "x"]]
    known_words = ["top", "foo", "bar"]

    # When
    found_words = helpers.find_diagonal_words(graph, known_words=known_words)

    # Then
    assert found_words == ["top"]


def test_backwards_northeast_diagonal_word():
    """Test that a northeast diagonal word spelled backwards can be found."""
    graph = [["x", "x", "p"], ["x", "o", "x"], ["t", "x", "x"]]
    known_words = ["top", "foo", "bar"]

    # When
    found_words = helpers.find_diagonal_words(graph, known_words=known_words)

    # Then
    assert found_words == ["top"]


def test_forwards_and_backwards_northeast_diagonal_word():
    """Test that words spelled forwards and backwards can be found simultaneously, even if they're in the same northeast diagonal."""
    graph = [["x", "x", "t"], ["x", "o", "x"], ["p", "x", "x"]]
    known_words = ["top", "pot", "foo", "bar"]

    # When
    found_words = helpers.find_diagonal_words(graph, known_words=known_words)
    found_words.sort()

    # Then
    assert found_words == ["pot", "top"]
