# Contributing

Thanks for helping improve this skill. Contributions that make the diligence methodology sharper, the question banks more complete, or the templates more usable are all welcome.

## Ground rules

- `SKILL.md` must stay compliant with the [Agent Skills spec](https://agentskills.io/specification): valid frontmatter, body under 500 lines, file references one level deep using relative paths.
- Keep `SKILL.md` lean. Detailed material belongs in `references/`; reusable output formats belong in `templates/`.
- The skill must never encourage turning unknowns into confident conclusions. Any new guidance should preserve the evidence/inference/unknown/contradiction discipline.
- No real company data, personal data, or secrets in examples. Examples must be clearly fictional.

## Workflow

1. Fork and create a feature branch.
2. Make your change.
3. Run the validator:

   ```bash
   python3 -m pip install pyyaml
   python3 scripts/validate_skill.py
   ```

4. Update `CHANGELOG.md` under an `Unreleased` heading.
5. Open a PR describing what changed and why. CI must pass.

## What makes a good contribution

- New key questions for a module, with a short rationale.
- New red-team checks that catch a real failure pattern in AI startup evaluation.
- Template improvements that make outputs easier to fill in or compare across deals.
- Validator improvements that catch spec violations earlier.

## What we will likely reject

- Generic prompt-engineering advice unrelated to diligence.
- Changes that make the skill assert conclusions without evidence.
- Large reorganizations without a clear usability win.
