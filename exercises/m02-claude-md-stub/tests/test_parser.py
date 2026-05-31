"""Tests for the parser module."""

import pytest

from pddl_inspector import parse_predicate, parse_state


def test_parse_predicate_with_args():
    pred = parse_predicate("(on a b)")
    assert pred.name == "on"
    assert pred.args == ("a", "b")


def test_parse_predicate_no_args():
    pred = parse_predicate("(clear)")
    assert pred.name == "clear"
    assert pred.args == ()


def test_parse_predicate_tolerates_whitespace():
    pred = parse_predicate("(  on   a  b  )")
    assert pred.name == "on"
    assert pred.args == ("a", "b")


def test_parse_predicate_malformed_raises():
    with pytest.raises(ValueError):
        parse_predicate("on a b")


def test_parse_state_multiple_predicates(blocks_state):
    assert len(blocks_state.predicates) == 3
    assert blocks_state.predicates[0].name == "on"


def test_parse_state_empty(empty_state):
    assert empty_state.predicates == ()
