# Chapter Review Protocol

Use this for formal single-chapter acceptance review after a chapter has been saved to `chapters/`.

This protocol is stricter than a casual prose critique. It diagnoses blockers, records evidence, and decides whether the chapter can update project canon.

## Review Scope

Review the accepted manuscript against:

- current chapter manuscript in `chapters/`
- matching control card in `control-cards/`
- `00-project-overview.md`
- `02-worldbuilding.md`
- `03-cast-bible.md`
- `04-relationship-map.md`
- `05-main-plotlines.md`
- `06-foreshadow-ledger.md`
- `07-chapter-roadmap.md`
- `08-dynamic-state.md`
- `09-style-guide.md`
- previous chapter manuscript
- source chapters for callbacks, quoted dialogue, recurring objects, payoff scenes, or repeated events
- project calibration files when world mechanics, genre conventions, intimacy, violence, law, magic, profession, medicine, or other fragile rules are active

For single-chapter review, do not accept "dynamic state only" or a summary-only read as source coverage. List the previous chapter and every actually read source chapter in `Sources Read`. If an expected source chapter was not read, mark continuity review as incomplete or blocked rather than guessing from memory.

Ignore `*.tmp.*`, scratch drafts, and obsolete review reports unless the user explicitly asks to audit history.

## Dimension Set

Use these default review dimensions. Rename or adapt them to the project's genre, but preserve the coverage.

### 0. Size, Completeness, And File Integrity

Check:

- manuscript exists in `chapters/`
- matching draft exists when the workflow uses drafts
- matching control card exists and is unique
- body is complete, readable, and not truncated
- no placeholder notes remain
- net body metrics meet the project target
- accepted title and file name align with the roadmap when titles are active

Recommended metrics:

- CJK character count
- non-whitespace character count
- total lines
- non-empty lines
- SHA256 if comparing draft and accepted manuscript

### 1. Text Hygiene, AI Pattern, And Prose Authenticity

Check:

- quote style and paired punctuation
- em dash, ellipsis, repeated punctuation, and sentence-fragment density
- repeated adjacent lines or duplicated phrasing
- formulaic contrast shells
- abstract summary replacing action
- theme-translation sentences
- static labels for voice, gaze, tone, or emotional state
- motif phrases becoming fixed buttons
- analysis-tone, report-tone, platform-copy, or industry jargon entering narration without point-of-view support

Use `authenticity-and-de-ai-pass.md` for repair after diagnosis.

### 2. Project Mechanics And World Rules

Check all active rules from `02-worldbuilding.md` and the project's calibration file:

- magic, law, medicine, profession, technology, biology, politics, rank, institutional process, social constraints, and genre-specific mechanics
- costs and limits
- public/private knowledge boundaries
- newly introduced rules that need registration
- whether a user-authorized exception has enough support, consequence, and writeback

Do not reject a project-specific exception merely because it differs from generic genre convention. Calibrate first.

### 3. Emotional, Relationship, Or Main Promise Progress

Check:

- the chapter changes at least one meaningful pressure state
- relationship shifts have an emotional bridge
- quiet chapters deepen cost, trust, threat, debt, or expectancy rather than sitting still
- sweetness, grief, fear, suspense, or wonder is earned by setup and consequence
- trope payoff does not replace character truth

For non-romance projects, replace relationship checks with the project's main promise: mystery fairness, survival pressure, moral cost, power struggle, quest progress, or thematic pressure.

### 4. POV And Narrative Distance

Check:

- point of view is anchored early
- the chapter does not enter inaccessible thoughts, offscreen facts, or behind-the-back images
- inference language is used where the point-of-view character is guessing
- narrative distance remains intentional
- repeated events are not retold from another perspective unless the new view reveals new pressure

### 5. Paragraph Rhythm And Readability

Check:

- active `paragraph_mode`
- decorative blank lines
- one-sentence paragraph chains
- same-speaker beat splitting
- punctuation substituting for action
- mobile-readable paragraph scale when web-serial mode is active
- long-paragraph mode does not become inert exposition

### 6. Character Voice And Behavior Continuity

Check:

- each major character sounds and acts like themselves under current pressure
- behavior changes have visible bridges
- stress response matches the cast bible or clearly evolves from it
- side characters bring their own objective, texture, or pressure instead of acting as tools
- character-specific action stocks do not become repetitive crutches

### 7. Dialogue, Fact, And Local Accuracy

Check:

- quoted prior dialogue matches source chapters or is clearly paraphrased
- numeric statements are true
- names, titles, directions, time, dates, and object continuity are correct
- question punctuation and dialogue formatting match project style
- message, letter, report, sign, or document excerpts use the project's locked format

### 8. Control Card Compliance And Intent Landing

Check:

- scene units or pressure units were executed
- positive deviations are better and recorded
- required callbacks, debts, or turns were handled
- forbidden drift was avoided
- language, dialogue, suspense, structure, style, and authenticity tasks landed
- ending hook matches the actual chapter
- if the chapter changed its center, the title and control card are repaired during writeback

### 9. Cross-Chapter Continuity And Canon Writeback Readiness

Check:

- previous chapter state carries naturally into this chapter
- dynamic state does not contradict the manuscript
- roadmap, foreshadow ledger, relationship map, and writing log can be updated from the accepted text
- callback source chapters were read when needed
- no unresolved failed review from a prior chapter is being mistaken for current canon
- chapter acceptance should update canon only after all blocking dimensions pass

## Rating

Use the lowest meaningful dimension as the chapter rating:

- `A`: passes cleanly
- `A-`: passes with minor notes
- `B`: passes with non-blocking warnings
- `C`: must fix the listed blocker and rerun affected dimensions
- `D`: structural, continuity, or hygiene failure; fix and rerun all dimensions unless the issue is provably isolated

Do not average scores. A single hard blocker blocks acceptance.

## Report Shape

```markdown
# Chapter NN Review

## Sources Read
- manuscript:
- control_card:
- prior_chapters:
- calibration_files:

## Integrity Metrics
- cjk_chars:
- non_whitespace_chars:
- total_lines:
- non_empty_lines:
- control_card_unique:
- draft_matches_accepted:

## Rating Table
| Dimension | Rating | Summary |
|---|---:|---|

## Must Fix
- 

## Dimension Notes
### Dimension 0: ...
- rating:
- evidence:
- blockers:
- warnings:

## Final Decision
- pass / needs fix / needs full rereview
- dimensions_to_rerun:
- canon_writeback_allowed: yes/no
```

Archive the report to `review/reports/NN-<chapter-title>-review.md` when the project uses review reports.
