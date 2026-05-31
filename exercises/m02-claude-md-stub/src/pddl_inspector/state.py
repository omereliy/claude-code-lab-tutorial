"""State and Predicate data types."""

from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class Predicate:
    name: str
    args: tuple[str, ...] = ()

    def __str__(self) -> str:
        if not self.args:
            return f"({self.name})"
        return f"({self.name} {' '.join(self.args)})"


@dataclass(frozen=True)
class State:
    predicates: tuple[Predicate, ...] = ()

    def contains(self, predicate: Predicate) -> bool:
        return predicate in self.predicates

    def predicate_names(self) -> set[str]:
        return {p.name for p in self.predicates}
