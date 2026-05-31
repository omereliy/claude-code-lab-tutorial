# Claude Code for Research — Workshop

A hands-on workshop for researchers at the SPL Lab (BGU) on using Claude Code
effectively for research codebases, algorithm reimplementation, and reproducible
experiments.

**Status:** Module 2 fully built. Modules 0, 1, 3–6 specified for production.
See `COURSE_SPEC.md` and `AGENT_HANDOFF.md`.

## Audience

MSc, PhD, and research assistants working in classical planning, heuristic
search, MARL/MAPF, and DRL. The exercises lean PDDL-flavored but the techniques
generalize.

## Structure

- `COURSE_SPEC.md` — master course specification.
- `AGENT_HANDOFF.md` — instructions for producing the remaining modules.
- `docs/` — MkDocs site source. One markdown file per module.
- `docs/teacher-notes/` — instructor-facing notes, excluded from main nav.
- `exercises/` — stub repos and exercise scaffolding.
- `mkdocs.yml` — site config.
- `.github/workflows/deploy.yml` — GitHub Pages deploy workflow.

## Local preview

```bash
pip install mkdocs-material
mkdocs serve
```

Visit `http://localhost:8000`.

## Contributing

If you're producing additional modules, read `AGENT_HANDOFF.md` first. Match the
style of `docs/module-02-claude-md.md` and `docs/teacher-notes/module-02.md`.

## License

(To be set by Omer when published.)
