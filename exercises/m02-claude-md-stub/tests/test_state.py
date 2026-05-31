"""Tests for state-level operations."""

from pddl_inspector import parse_predicate


def test_state_contains_predicate(blocks_state):
    pred = parse_predicate("(on a b)")
    assert blocks_state.contains(pred)


def test_state_does_not_contain_missing_predicate(blocks_state):
    pred = parse_predicate("(on c a)")
    assert not blocks_state.contains(pred)


def test_predicate_names(blocks_state):
    assert blocks_state.predicate_names() == {"on", "clear"}


def test_empty_state_contains_nothing(empty_state):
    pred = parse_predicate("(on a b)")
    assert not empty_state.contains(pred)
