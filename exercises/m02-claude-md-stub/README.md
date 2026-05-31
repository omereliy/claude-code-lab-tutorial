# pddl_inspector

Small Python utilities for working with simplified PDDL-like states and predicates.

## Install

```bash
pip install -e .
```

## Test

```bash
pytest
```

## Example

```python
from pddl_inspector import parse_state, parse_predicate

state = parse_state("(on a b) (on b c) (clear a)")
print(state.predicates)
```

See `examples/` for sample state files.
