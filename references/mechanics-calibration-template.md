# Mechanics Calibration Template

Use this when a project has fragile genre rules, invented systems, specialist domains, or user-authorized exceptions that generic genre knowledge may misread.

Examples:

- invented biology, transformation, or bond rules
- cultivation ranks, tribulation costs, spiritual tools
- magic systems and spell costs
- game rules, survival loops, dungeons, stat systems
- legal, medical, academic, military, palace, or corporate procedures
- mystery clue fairness and reveal rules
- alternate history institutions

Create a project-local calibration file such as:

- `10-mechanics-calibration.md`
- `mechanics-calibration.md`
- `.claude/memory/feedback-mechanics-calibration.md`

## Purpose

The calibration file is not a lore dump. It is an executable rule layer for writing and review.

It should answer:

- what rules are active in this project
- what the project intentionally changes from common genre convention
- what counts as allowed, risky, or forbidden
- what must be written back when a new rule appears
- how reviewers should rank conflicting sources

## Priority Order

Use this default priority order unless the project overrides it:

1. user's latest explicit instruction
2. project calibration file
3. current project canon files
4. accepted manuscript facts
5. general genre convention
6. external reference material

If a user-authorized rule conflicts with older canon, do not simply reject the new rule. Mark the conflict, repair the relevant canon files, and preserve consequence.

## Required Sections

```markdown
# Mechanics Calibration

## Rule Priority
- latest user instruction:
- project calibration:
- canon files:
- genre convention:

## Core Mechanics
- rule:
  - how it works:
  - what it costs:
  - who knows it:
  - how it appears in scene:
  - what cannot happen:

## Project-Specific Overrides
- generic convention:
- project override:
- required support:
- required consequence:
- writeback target:

## Scene-Level Checks
- when this mechanic appears, check:

## Review Do-Not-Penalize List
- do not penalize X merely because it exists; review whether it has support, agency, boundary, cost, and continuity.

## Hard Contradictions
- contradiction:
- why it breaks canon:
- repair target:

## New Rule Registration
- where to record new world rules:
- where to record temporary assumptions:
- where to record changed character knowledge:
```

## Calibration In Chapter Planning

Before drafting a chapter with active mechanics:

- read `02-worldbuilding.md`
- read the calibration file
- identify the rules in play
- put those rules into the chapter control card under `world_rules_in_play`
- list the likely failure modes under `forbidden_drift`
- define the scene consequence, not only the spectacle

## Calibration In Review

When reviewing active mechanics:

- judge by project priority order first
- separate "allowed but under-supported" from "contradicts canon"
- ask whether the mechanic changes agency, cost, public knowledge, power, relationship, or future constraints
- if it introduces a new long-term rule, require writeback to `02-worldbuilding.md`, `08-dynamic-state.md`, `03-cast-bible.md`, or another canonical file
- do not let mechanics solve emotional, moral, or plot work for free

## Fragile Scene Adapter

Use this adapter for high-pressure scenes such as intimacy, violence, illness, magic backlash, interrogation, possession, courtroom testimony, or irreversible transformation.

Check:

- attention: what the POV character notices first
- distance: who moves closer or away
- contact: what physically or socially crosses a boundary
- body or system response: what changes because of the contact
- agency: who chooses, resists, asks, consents, refuses, or delays
- boundary action: what makes the scene not purely coercive or mechanical
- consequence: what remains afterward
- writeback: which state or rule files must change

The stronger the scene, the more it needs agency, cost, aftermath, and continuity.
