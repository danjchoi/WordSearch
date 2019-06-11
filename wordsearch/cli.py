"""Generate and solve a word search graph."""


# [-Imports:Third Party-]
import click

# [-Imports:Project-]
from wordsearch import core


# [-Internals-]
def _check_grid_dimensions(*, grid_height, grid_width):
    """Raise a ValueError if either grid_height or grid_width is 0 or less."""
    if grid_height <= 0:
        raise ValueError(
            f"GRID_HEIGHT must be greater than 0. It was set to {grid_height}."
        )
    if grid_width <= 0:
        raise ValueError(
            f"GRID_WIDTH must be greater than 0. It was set to {grid_width}."
        )


# [-Public-]
@click.command()
@click.argument("dictionary_filename", type=click.Path(exists=True))
@click.argument("grid_height", type=int)
@click.argument("grid_width", type=int)
def cli(dictionary_filename, grid_height, grid_width):
    """Generate and solve a word search graph given a list of known words."""
    _check_grid_dimensions(grid_height=grid_height, grid_width=grid_width)
    graph = core.generate_graph(num_rows=grid_height, num_cols=grid_width)
    core.display_graph(graph)
    known_words = core.get_known_words(dictionary_filename)
    found_words = core.find_words(graph, known_words=known_words)
    core.display_results(found_words)
