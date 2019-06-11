"""Core logic for the wordsearch module."""


# [-Imports:Python-]
import random
import string
import pathlib

# [-Imports:Project-]
from wordsearch import helpers


# [-Public-]
def generate_graph(*, num_rows, num_cols):
    """
    Generate a list of lists with the following properties:

    * The container list has a length of num_rows
    * The internal lists have a length of num_cols
    * The internal lists' elements are strings that have a length of 1
    * The strings are only comprised of lowercase letters
    # Example: [["a", "b", "c"], ["d", "e", "f"], ["g", "h", "i"]]
    """
    graph = []
    for _ in range(num_rows):
        new_row = [random.choice(string.ascii_lowercase) for _ in range(num_cols)]
        graph.append(new_row)
    return graph


def display_graph(graph):
    """Print the graph."""
    output_string = "\n".join([" ".join(row) for row in graph])
    print(output_string)


def get_known_words(dictionary_filename):
    """Get the known words from the given dictionary file."""
    dictionary_file_path = pathlib.Path(dictionary_filename)
    return dictionary_file_path.read_text().lower().split()


def find_words(graph, *, known_words):
    """Returns a set of the words found in the word search."""
    found_horizontal_words = helpers.find_horizontal_words(
        graph, known_words=known_words
    )
    found_vertical_words = helpers.find_vertical_words(graph, known_words=known_words)
    found_diagonal_words = helpers.find_diagonal_words(graph, known_words=known_words)
    return set(found_horizontal_words + found_vertical_words + found_diagonal_words)


def display_results(found_words):
    """Print all the found words."""
    output_string = "\n".join(found_words)
    print(output_string)
