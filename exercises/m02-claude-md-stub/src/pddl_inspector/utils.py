"""Small helpers. Add cautiously — some of these get used in unexpected places."""

from __future__ import annotations

from pddl_inspector.parser import parse_predicate
from pddl_inspector.state import Predicate


def normalize_predicate_text(text: str) -> str:
    """Collapse whitespace in a predicate string so '( on a   b )' == '(on a b)'."""
    return " ".join(text.split())


def predicates_from_text(text: str) -> list[Predicate]:
    """Parse a whitespace-separated list of predicate texts into Predicate objects.

    Reuses parse_predicate from the parser module. If you find yourself parsing
    predicate strings anywhere else, use this or parse_predicate — do not roll
    your own regex.
    """
    return [parse_predicate(chunk) for chunk in _split_predicates(text)]


def _split_predicates(text: str) -> list[str]:
    """Split a string into top-level parenthesized chunks."""
    chunks: list[str] = []
    depth = 0
    start = -1
    for i, ch in enumerate(text):
        if ch == "(":
            if depth == 0:
                start = i
            depth += 1
        elif ch == ")":
            depth -= 1
            if depth == 0 and start >= 0:
                chunks.append(text[start : i + 1])
                start = -1
    return chunks
