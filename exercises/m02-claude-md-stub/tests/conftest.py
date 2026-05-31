"""Shared pytest fixtures for pddl_inspector tests.

New tests should use these fixtures where applicable rather than rebuilding
states inline. If you need a state that isn't here, add a fixture.
"""

import pytest

from pddl_inspector import parse_state


@pytest.fixture
def blocks_state():
    """A small blocksworld state: a on b on c, a is clear."""
    return parse_state("(on a b) (on b c) (clear a)")


@pytest.fixture
def empty_state():
    return parse_state("")


@pytest.fixture
def single_predicate_state():
    return parse_state("(holding x)")
