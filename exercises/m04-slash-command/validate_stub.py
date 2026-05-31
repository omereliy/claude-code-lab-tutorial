#!/usr/bin/env python3
"""A STUB PDDL domain "validator" for the Module 4 exercise.

This is NOT a real validator. It does just enough lightweight checking to
produce realistic, messy output modeled on the categories a real PDDL validator
reports (syntax / type-hierarchy / undeclared predicate / predicate arity).

The output is intentionally ugly: unsorted, mixed severities, duplicated lines,
no grouping. That mess is the point — your /validate-domain command's job is to
turn it into a grouped, prioritized summary.

Usage:
    python validate_stub.py examples/blocks.pddl
"""

import re
import sys

PDDL_KEYWORDS = {
    "and", "or", "not", "when", "forall", "exists", "imply",
    "increase", "decrease", "assign", "=", ">", "<", ">=", "<=",
}
# 'object' is the implicit root type; treat it as always declared.
IMPLICIT_TYPES = {"object"}


def find_section(text, name):
    """Return the parenthesized body of (:name ...), or '' if absent."""
    i = text.find("(:" + name)
    if i == -1:
        return ""
    depth, start = 0, i
    for j in range(i, len(text)):
        if text[j] == "(":
            depth += 1
        elif text[j] == ")":
            depth -= 1
            if depth == 0:
                return text[start : j + 1]
    return text[start:]


def main():
    if len(sys.argv) < 2:
        print("usage: python validate_stub.py <path-to-domain.pddl>")
        sys.exit(2)

    path = sys.argv[1]
    try:
        with open(path, encoding="utf-8") as fh:
            raw = fh.read()
    except OSError as exc:
        print(f"ERROR: cannot read {path}: {exc}")
        sys.exit(2)

    # Strip comments (from ';' to end of line) for analysis.
    text = re.sub(r";[^\n]*", "", raw)

    findings = []  # (severity, category, message) — appended in discovery order

    print(f"[pyval-stub] checking {path}")

    # --- syntax: paren balance --------------------------------------------
    bal = text.count("(") - text.count(")")
    if bal != 0:
        findings.append(("ERROR", "syntax",
                         f"unbalanced parentheses (off by {bal})"))

    # --- declared types ----------------------------------------------------
    types_body = find_section(text, "types")
    declared_types = set(IMPLICIT_TYPES)
    for tok in re.findall(r"[\w-]+", types_body.replace("(:types", "")):
        if tok != "-":
            declared_types.add(tok)

    # --- declared predicates + arity --------------------------------------
    preds = {}  # name -> arity
    preds_body = find_section(text, "predicates")
    for m in re.finditer(r"\(\s*([\w-]+)((?:\s+\?[\w-]+(?:\s*-\s*[\w-]+)?)*)\s*\)",
                         preds_body):
        name = m.group(1)
        arity = len(re.findall(r"\?[\w-]+", m.group(2)))
        preds[name] = arity
    findings.append(("note", "info",
                     f"{len(preds)} predicate(s) declared, "
                     f"{len(declared_types - IMPLICIT_TYPES)} type(s) declared"))

    # --- per-action checks -------------------------------------------------
    for am in re.finditer(r"\(:action\s+([\w-]+)(.*?)(?=\(:action|\Z)",
                          text, re.DOTALL):
        action = am.group(1)
        body = am.group(2)

        params = find_section_inline(body, "parameters")
        # parameter types
        for pm in re.finditer(r"\?[\w-]+\s*-\s*([\w-]+)", params):
            t = pm.group(1)
            if t not in declared_types:
                findings.append(("ERROR", "type-hierarchy",
                                 f"type '{t}' (parameter in action "
                                 f"'{action}') is not declared in :types"))

        # predicate usages in everything except the parameters block
        rest = body.replace(params, " ", 1)
        for um in re.finditer(r"\(\s*([\w-]+)((?:\s+[\w?-]+)*)\s*\)", rest):
            name = um.group(1)
            if name in PDDL_KEYWORDS or name.startswith(":"):
                continue
            used_arity = len(um.group(2).split())
            if name not in preds:
                findings.append(("warn", "undeclared-predicate",
                                 f"predicate '{name}' used in action "
                                 f"'{action}' is not declared in :predicates"))
            elif used_arity != preds[name]:
                findings.append(("ERROR", "predicate-arity",
                                 f"predicate '{name}' used with {used_arity} "
                                 f"arg(s) in action '{action}'; declared "
                                 f"arity {preds[name]}"))

    # Inject a realistic duplicate (real tools double-report across passes).
    for f in list(findings):
        if f[1] == "predicate-arity":
            findings.append(f)
            break

    # --- emit, deliberately unsorted --------------------------------------
    errs = sum(1 for s, _, _ in findings if s == "ERROR")
    warns = sum(1 for s, _, _ in findings if s.lower() == "warn")
    for sev, cat, msg in findings:
        print(f"{sev}: [{cat}] {msg}")
    print(f"[pyval-stub] done — {errs} error(s), {warns} warning(s) "
          f"(unsorted, may contain duplicates)")
    sys.exit(1 if errs else 0)


def find_section_inline(text, name):
    """Like find_section but for a bare ':name (...)' (no leading paren)."""
    i = text.find(":" + name)
    if i == -1:
        return ""
    p = text.find("(", i)
    if p == -1:
        return ""
    depth, start = 0, p
    for j in range(p, len(text)):
        if text[j] == "(":
            depth += 1
        elif text[j] == ")":
            depth -= 1
            if depth == 0:
                return text[start : j + 1]
    return text[start:]


if __name__ == "__main__":
    main()
