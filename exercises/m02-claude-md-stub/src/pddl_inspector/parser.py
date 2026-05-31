"""Parsing utilities for PDDL-like predicate and state strings.

The grammar handled here is intentionally simple: a state is a whitespace-
separated sequence of predicates, and each predicate is `(name arg1 arg2 ...)`.
No types, no negation, no quantifiers.
"""

from __future__ import annotations

import re
from pddl_inspector.state import Predicate, State

# Matches `(name arg1 arg2 ...)` with at least the name.
_PREDICATE_RE = re.compile(r"\(\s*([\w-]+)((?:\s+[\w-]+)*)\s*\)")


def parse_predicate(text: str) -> Predicate:
    """Parse a single predicate string like '(on a b)' into a Predicate.

    Raises ValueError on malformed input. Whitespace around args is tolerated.
    """
    text = text.strip()
    match = _PREDICATE_RE.fullmatch(text)
    if not match:
        raise ValueError(f"malformed predicate: {text!r}")
    name = match.group(1)
    args_str = match.group(2).strip()
    args = tuple(args_str.split()) if args_str else ()
    return Predicate(name=name, args=args)


def parse_state(text: str) -> State:
    """Parse a state string consisting of zero or more predicates.

    Predicates are separated by whitespace. The result is a State whose
    predicates are stored in declaration order (no deduplication here).
    """
    predicates = []
    for match in _PREDICATE_RE.finditer(text):
        full = match.group(0)
        predicates.append(parse_predicate(full))
    return State(predicates=tuple(predicates))
