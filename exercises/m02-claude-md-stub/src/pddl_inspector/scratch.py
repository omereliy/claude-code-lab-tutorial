# scratch.py: experimental goal-checker prototype.
# Status: abandoned. Was exploring a camelCase API style. Do not extend.
# Kept around because some experiments still import goalSatisfies; will
# delete once those are migrated.

from pddl_inspector.state import State, Predicate


def goalSatisfies(currentState, goalPreds):
    # quick-and-dirty check, no validation
    for g in goalPreds:
        if g not in currentState.predicates:
            return False
    return True


def buildGoalFromText(text):
    # half-finished: doesn't actually parse, just splits on spaces
    parts = text.split()
    # TODO: rewrite using the real parser
    return [Predicate(name=p, args=()) for p in parts]
