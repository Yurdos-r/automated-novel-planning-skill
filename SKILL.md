---
name: novel-control-station
description: Use when writing, planning, continuing, repairing, revising, auditing, or running marathon/"疯狂写作"/auto continuation mode for Chinese long-form fiction with recurring characters, multiple plotlines, persistent world rules, chapter-by-chapter continuity needs, full-project review needs, or style-specific constraints.
---

# 自动化规划写小说skill

## Overview

Run Chinese long-form fiction as a controlled project system, not a one-shot prompt. Align the premise, cast pressure, ending direction, project files, chapter control cards, accepted manuscripts, style rules, anti-AI profile, review gates, and writeback logs before letting the story advance.

Default language is simplified Chinese unless the user explicitly asks otherwise.

## Hard Rules

- Do not start formal novel design until the main plot direction, core character tension, and ending direction are aligned.
- Do not start chapter drafting before presenting the full outline and full cast dossier.
- Do not draft any chapter before reading the required project files.
- Do not draft the next chapter, generate its control card, or continue in marathon mode before reading the previous accepted chapter manuscript, its matching control card, and every source chapter required by callbacks, quoted dialogue, recurring objects, payoff scenes, repeated events, relationship bridges, foreshadow returns, or direct continuity.
- Do not continue from `08-dynamic-state.md`, chapter summaries, writing logs, roadmap notes, or memory alone. If source chapters are unclear, build a retrieval slice from `08-dynamic-state.md`, `06-foreshadow-ledger.md`, `07-chapter-roadmap.md`, `04-relationship-map.md`, `05-main-plotlines.md`, and `control-cards/`, then read the accepted chapters named by that slice.
- Do not treat a single flat plot as enough for long-form fiction. Default to multiple active lines unless the user deliberately wants a small single-line work.
- Do not copy a sample work's signature setup, role shell, twist engine, scene pattern, or language texture.
- Do not treat benchmark logic as doctrine. Adapt it to user intent, genre, and target readership.
- Do not let trope convenience, fake depth, or decorative structure override human truth, causal pressure, social texture, or character cost.
- Do not treat marathon mode as permission to skip chapter control, rewrite escalation, dynamic updates, review, or logging.
- Do not let a secondary graph, recall map, scratch index, or writing log override standard project files. They are support views, not truth sources.
- Do not satisfy forgotten-element checks with token cameos or cosmetic mentions. Re-entry must change pressure, debt, choice, or expectation.
- Do not run de-AI cleanup as blind flattening. Preserve genre register, era texture, narrator stance, necessary type terms, and character voice.
- Do not treat AI flavor as a universal blacklist. When a project anti-AI profile exists, calibrate against its allowed type-canon terms, high-risk shells, action inventory, motif syntax, and scene-specific risks.
- Do not let narration or interiority slide into review copy, theory-heavy explanation, empty abstract words, or professional jargon unless the point of view, era, setting, or plot task truly requires it.
- Default paragraph mode is `web-serial-natural` unless `09-style-guide.md` or the chapter control card explicitly switches to `long-paragraph`.
- Under `web-serial-natural`, most narrative paragraphs should hold `2-4` sentences. Single-sentence narrative paragraphs are for emphasis, reveal, shock, cut, hook, or emotional stall, and should not chain by habit.
- Do not split one speaker's continuous beat into multiple paragraphs unless interruption, stage movement, or a pressure turn changes the beat.
- Do not use chapter titles as spoiler summaries, empty riddles, or labels detached from chapter pressure.
- Do not answer a request for full project audit, whole-book review, phase review, or "全面审查" with only a single-chapter review or state-health check. Use `full-project-audit.md`.
- After every accepted chapter, update dynamic state and required structural files before moving on.

## Standard Files

Maintain these files for every project:

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

Accepted manuscripts go in `chapters/`. One persisted chapter control card per accepted chapter goes in `control-cards/`.

Default filenames:

- `chapters/NN-<chapter-title>.md`
- `control-cards/NN-<chapter-title>-control-card.md`

If chapters are numbered-only, replace `<chapter-title>` with a stable short slug.

Read [document-templates.md](references/document-templates.md) when creating or restoring project files.

## Startup

When starting a new project:

1. Run the interview flow in [interview-and-handoff-flow.md](references/interview-and-handoff-flow.md).
2. Use [character-construction-methods.md](references/character-construction-methods.md) to build desire, fear, shame, debt, contradiction, speech signature, and arc direction.
3. Use [mechanics-calibration-template.md](references/mechanics-calibration-template.md) when the project has fragile world, profession, law, magic, biology, game, mystery, or other rules.
4. Use [project-anti-ai-profile.md](references/project-anti-ai-profile.md) when repeated AI-flavor complaints, dense type-canon vocabulary, professional diction, style-sensitive texture, or recurring motif syntax needs project-level calibration.
5. Create the standard files and `codex-continue-novel.ps1` in the project root.

Build `codex-continue-novel.ps1` from [assets/codex-continue-novel.ps1](assets/codex-continue-novel.ps1). On Windows, write the root script as UTF-8 with BOM and preserve the template's UTF-8 console setup, log writing, forced writeback constraint, and disk write verification.

Do not assume the user will remember the launch command. Record:

```powershell
powershell -ExecutionPolicy Bypass -File .\codex-continue-novel.ps1
```

## Reference Loading

Load only the references required by the current stage.

Foundational or high-level review:

- [foundational-literary-principles.md](references/foundational-literary-principles.md)
- [critical-evaluation-standards.md](references/critical-evaluation-standards.md)
- [epoch-and-people-resonance.md](references/epoch-and-people-resonance.md)
- [reader-retention-and-ai-failure-modes.md](references/reader-retention-and-ai-failure-modes.md)

Benchmark and outline:

- [popular-fiction-common-laws.md](references/popular-fiction-common-laws.md)
- [genre-benchmark-rules.md](references/genre-benchmark-rules.md)
- [benchmark-trigger-matrix.md](references/benchmark-trigger-matrix.md)
- [chapter-architecture-rules.md](references/chapter-architecture-rules.md)
- [chapter-title-method.md](references/chapter-title-method.md) when titled chapters are active

Chapter drafting and revision:

- Always load [chapter-architecture-rules.md](references/chapter-architecture-rules.md).
- Load [chapter-control-card.md](references/chapter-control-card.md) before drafting.
- Load [continuity-and-marathon-mode.md](references/continuity-and-marathon-mode.md) when continuing long fiction or auto-advancing.
- Load [graph-and-recall-control.md](references/graph-and-recall-control.md) when recurrence density, cast rotation, or source-chapter retrieval pressure is high.
- Load [dialogue-writing-rules.md](references/dialogue-writing-rules.md) when dialogue carries pressure.
- Load [suspense-and-reveal-design.md](references/suspense-and-reveal-design.md) when concealment, clue fairness, or reveal work is active.
- Load [scene-execution-patterns.md](references/scene-execution-patterns.md) when the chapter needs scene-by-scene or pressure-unit control.
- Load [forgotten-elements-and-line-heat.md](references/forgotten-elements-and-line-heat.md) when serialized recurrence risk is meaningful.
- Load [project-anti-ai-profile.md](references/project-anti-ai-profile.md) when creating, updating, or applying a project-local anti-AI profile.
- Load [authenticity-and-de-ai-pass.md](references/authenticity-and-de-ai-pass.md) only after a structurally acceptable draft exists.
- Load [pre-landing-gates.md](references/pre-landing-gates.md) before accepting the chapter into `chapters/`.
- Load [chapter-review-protocol.md](references/chapter-review-protocol.md) for formal single-chapter acceptance review.
- Load [state-health-check.md](references/state-health-check.md) when dynamic state is stale, contradictory, duplicated, or too long.

Full audit:

- Load [full-project-audit.md](references/full-project-audit.md).
- Use [chapter-review-protocol.md](references/chapter-review-protocol.md) only for single-chapter deep dives inside the audit.
- Use [state-health-check.md](references/state-health-check.md) only for dynamic-state repair inside the audit.

Style modules:

- Route through [style-modules/index.md](references/style-modules/index.md).
- Load only selected `core.md` module files first.
- Load deeper module documents only if the chapter needs them.

Available internal modules: humor, suspense, mystery, romance, horror, fantasy, literary.

## Project Anti-AI Profile

When generic authenticity cleanup is not precise enough, create or update a project-local profile such as:

- `10-anti-ai-profile.md`
- `11-anti-ai-profile.md`
- `anti-ai-profile.md`
- `.claude/memory/feedback-anti-ai-profile.md`

Use [project-anti-ai-profile.md](references/project-anti-ai-profile.md) to record:

- allowed type-canon terms and when they are legitimate
- terms that become suspicious only by density, misuse, or context
- high-risk phrasing shells, static labels, punctuation habits, and over-neat contrast patterns
- repeated gestures, body reactions, action inventory, and micro-expression limits
- motif or callback sentence shapes that must vary across chapters
- genre mechanism risks that must create choice, cost, consequence, or pressure
- scene-specific anti-AI cards, score targets, and over-defense risks

Apply the profile before generic de-AI cleanup. Its job is to preserve necessary project texture while targeting real local patterning.

## Chapter Workflow

For every chapter:

1. If the project is launching, redirecting, or under high-level review, load the foundational references.
2. Read required project files: `00`, `02`, `03`, `05`, `06`, `07`, `08`, `09`, any local mechanics calibration file, and any local anti-AI profile when style or authenticity risk is active.
3. Read the previous accepted chapter manuscript, especially its final scene, object state, body distance, emotional temperature, unresolved location, and social position.
4. Read the previous chapter's matching control card.
5. Read every accepted source chapter required by callbacks, quoted dialogue, recurring objects, payoff scenes, repeated events, relationship bridges, foreshadow returns, or direct continuity.
6. If source chapters are unclear, build a retrieval slice first, name the source chapters, and read those accepted manuscripts before generating the control card.
7. Load selected style modules and execution references for this chapter.
8. Scan for setting conflicts, character drift, relationship breaks, forgotten debts, cold lines, dropped foreshadowing, unsupported payoffs, mechanics drift, trope convenience, social-pressure loss, paragraph-mode drift, jargon drift, and project-specific AI-flavor risks.
9. Generate and persist the chapter control card in `control-cards/`.
10. If chapter titles are active, generate `3-5` candidate titles, choose a working title, and record it in the card and roadmap.
11. Draft from the control card. Use scene or pressure-unit drafting when control needs to be tighter.
12. Run the chapter benchmark check.
13. If the benchmark check fails, apply rewrite escalation before accepting the chapter.
14. Run the authenticity pass. Apply the project anti-AI profile first when it exists, then remove generic AI habits, false depth, abstract summaries, over-professionalized diction, and reader-hostile jargon; finally restore concrete detail, rhythm variation, speaker distinction, and project voice.
15. Run a post-authenticity mini recheck for continuity facts, character voice, relationship pressure, hook/closure integrity, paragraph mode, readability, necessary terminology, and approved type texture.
16. Run pre-landing gates. Use `scripts/chapter_lint.py` when available.
17. Save the accepted manuscript into `chapters/` only after active gates pass.
18. If titled chapters are active, run the final title-fit check and rename files if the chapter center moved.
19. Run formal single-chapter review with [chapter-review-protocol.md](references/chapter-review-protocol.md).
20. Only after review passes, or after the user explicitly accepts the risk, update `08-dynamic-state.md`, affected canon files, roadmap, foreshadow ledger, control cards, and `logs/writing-log.md`.

## Rewrite Escalation

If a chapter benchmark check fails:

1. First failure: rewrite the full chapter by the issue list.
2. Second failure: rewrite only the failed dimensions with tighter control.
3. Third failure: stop blind whole-chapter rewriting, identify root causes, and decide whether the repair belongs in outline, character design, pacing, mechanics, or theme-bearing structure.

## Full Project Audit

When the user asks for "全面审查", "全书体检", whole-book review, phase review, finale readiness, or checking all project files, use [full-project-audit.md](references/full-project-audit.md).

Audit file inventory, canon consistency, chapter-control alignment, continuity, line heat, foreshadow pressure, style drift, anti-AI profile fit, dynamic-state health, and readiness for continuation or finale.

Do not claim every chapter's prose was reviewed unless every accepted chapter was actually read. For long projects, clearly separate "read" from "inventoried only".

## Marathon Mode

Marathon mode begins only after the user approves the current outline and cast dossier.

Before handoff:

- load [bootstrap-and-marathon-handoff.md](references/bootstrap-and-marathon-handoff.md)
- verify or repair `codex-continue-novel.ps1`
- tell the user to close the current session
- give the launch command
- tell the user that `Ctrl+C` stops the runner

In marathon mode, do not ask chapter by chapter, but keep every internal control step active: file reads, previous/source chapter reads, retrieval slice when needed, control card, title control, style loading, forgotten-element scan, benchmark checks, rewrite escalation, project anti-AI profile, authenticity pass, pre-landing gates, formal review, writeback, and logging.

Continue automatically only after the current chapter is accepted and written back. Stop only when the approved outline has naturally concluded, not merely because a fixed chapter count or word target was reached.

## Validation And Writeback

Use [quality-and-writeback-checks.md](references/quality-and-writeback-checks.md) for adaptive weighting, originality discipline, chapter quality gates, final writeback, and common-failure review.

After every accepted chapter:

- update `08-dynamic-state.md` using [dynamic-state-template.md](references/dynamic-state-template.md)
- update changed canonical files in `03/04/05/06/07/02` as needed
- keep `chapters/` and `control-cards/` aligned by chapter number and title
- sync optional secondary notes only after canonical files are current
- apply [logging-rules.md](references/logging-rules.md)

Run [state-health-check.md](references/state-health-check.md) every `10-20` chapters in marathon mode, after major rewrites, before volume finales, and whenever dynamic state, roadmap, review reports, or foreshadow ledger disagree.
