# Full Project Audit

Use this when the user asks for a full project audit, whole-book review, complete file review, phase review, finale readiness check, or asks to "全面审查 / 全书体检 / 检查所有项目文件".

This protocol is broader than `chapter-review-protocol.md` and `state-health-check.md`. Do not replace it with a single-chapter review or dynamic-state repair unless the user narrows the request.

## Audit Scope

Audit the project as a file system, not only as prose.

Required standard sources:

- `00-project-overview.md`
- `01-theme-and-proposition.md`
- `02-worldbuilding.md`
- `03-cast-bible.md`
- `04-relationship-map.md`
- `05-main-plotlines.md`
- `06-foreshadow-ledger.md`
- `07-chapter-roadmap.md`
- `08-dynamic-state.md`
- `09-style-guide.md`
- `chapters/`
- `control-cards/`
- `logs/writing-log.md`

Conditional sources:

- `review/reports/` when it exists
- project-local mechanics calibration files
- retrieval maps, graph notes, or sidecars when the project uses them
- synopsis, volume summaries, or phase review files when present

Ignore scratch files, temporary drafts, and obsolete alternates unless the user asks to audit history.

## Audit Modes

Choose the smallest mode that honestly satisfies the user request.

- `inventory`: list files, missing files, naming mismatches, duplicate or orphaned artifacts.
- `consistency`: compare current canon across roadmap, dynamic state, chapters, control cards, relationship map, plotlines, foreshadow ledger, world rules, and log.
- `quality`: evaluate outline health, character continuity, line heat, foreshadow load, style-guide compliance, chapter rhythm, and repeated failure patterns.
- `readiness`: decide whether the project is ready for marathon continuation, volume finale, major rewrite, publication-oriented revision, or ending.
- `full`: run inventory, consistency, quality, and readiness.

If the user says "全面审查" without narrowing the scope, use `full`.

## Required Procedure

1. Build a file inventory.
   - Record which standard files exist.
   - Count accepted chapter manuscripts.
   - Count persisted control cards.
   - Note missing, duplicated, orphaned, empty, stale, or oddly named files.
2. Establish latest accepted canon.
   - Identify latest accepted chapter from `chapters/`, `07-chapter-roadmap.md`, `08-dynamic-state.md`, review reports, and writing log.
   - Flag disagreement instead of choosing silently.
3. Compare cross-file truth.
   - protagonist and major cast state
   - relationship state
   - active plotlines
   - foreshadow status
   - world rules and mechanics
   - current location, time, public knowledge, and unresolved obligations
4. Audit chapter-control alignment.
   - every accepted chapter should have one matching control card unless the project predates control cards
   - titles and numbers should match across chapter file, control card, roadmap, and review report
   - control cards should not contain unexecuted tasks treated as canon
5. Audit drift and heat.
   - cold plotlines
   - missing recurring characters or relationships
   - overdue foreshadow
   - emotional debts not repriced
   - relationship jumps without bridges
   - world-rule or mechanics drift
6. Audit prose and style at project scale.
   - repeated AI shell patterns
   - analysis-tone drift
   - over-professionalized or unexplained jargon
   - paragraph-mode drift
   - style-module overmixing
   - chapter endings repeating the same move
7. Decide readiness.
   - continue as-is
   - continue after minor repairs
   - pause marathon and repair canon first
   - rewrite a specific chapter or phase
   - rebuild outline / cast / rules before drafting more
   - ready for finale / not ready for finale

## Sampling Rules For Long Projects

For short projects, inspect every accepted chapter and every control card.

For long projects where reading every chapter would exceed the available context:

- still inventory every file name
- read all standard canon files
- read latest `3-5` accepted chapters
- read source chapters for active callbacks, overdue foreshadow, or suspected contradictions
- read first chapter, latest chapter, and all volume/phase boundary chapters when available
- sample chapters from each phase if quality drift is the audit target
- clearly report which chapters were read and which were only inventoried

Do not claim a full prose audit of unread chapters. Say "file inventory complete; prose audit sampled" when sampling is used.

## Output Shape

Use this report shape:

```markdown
# Full Project Audit

## Scope
- mode:
- project_root:
- files_inventoried:
- chapters_read:
- chapters_inventoried_only:
- control_cards_read:
- standard_files_read:

## Executive Decision
- status: pass / pass_after_repairs / blocked
- next_action:
- marathon_safe: yes/no
- canon_writeback_safe: yes/no

## File Inventory
- missing_standard_files:
- orphan_chapters:
- orphan_control_cards:
- duplicate_numbers_or_titles:
- stale_or_empty_files:

## Canon Consistency
- latest_chapter_agreement:
- dynamic_state_agreement:
- roadmap_agreement:
- cast_and_relationship_agreement:
- plotline_agreement:
- foreshadow_agreement:
- world_rule_agreement:

## Story Health
- line_heat:
- character_continuity:
- relationship_pressure:
- foreshadow_pressure:
- style_and_paragraph_mode:
- repeated_failure_patterns:

## Required Repairs
| Priority | File / Area | Problem | Evidence | Repair |
|---|---|---|---|---|

## Optional Improvements
- 

## Files To Update
- 
```

## Writeback Rules

Do not change canon silently during audit.

If the user asked only for an audit, produce the report and ask before editing project files.

If the user explicitly asked to audit and repair:

- repair highest-priority canon contradictions first
- update `08-dynamic-state.md` only after accepted canon is identified
- update `07-chapter-roadmap.md`, `06-foreshadow-ledger.md`, relationship map, cast bible, and worldbuilding only where evidence supports the change
- append a writing-log entry describing the audit and repairs
- do not use the writing log as the only place where repaired story truth exists
