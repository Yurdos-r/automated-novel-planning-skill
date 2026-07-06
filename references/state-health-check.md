# State Health Check

Use this when a project is long, in marathon mode, after a major rewrite, before phase review, or when `08-dynamic-state.md` feels too long, stale, contradictory, or hard to trust.

Goal: keep dynamic state as current project truth, not a second novel, not a writing log, and not a graveyard of old partial states.

## What Dynamic State Should Contain

`08-dynamic-state.md` should answer:

- what chapter is latest accepted canon
- what changed most recently
- where each major character, relationship, plotline, foreshadow, and world rule currently stands
- what is hot, cold, due, overdue, closed, or pending confirmation
- what must carry into the next chapter

It should not:

- preserve every old chapter summary
- include obsolete draft facts
- contain failed review claims as truth
- duplicate the writing log
- leave contradictory "latest chapter" markers
- store important truth only in prose paragraphs that cannot be scanned

## Health Checklist

Run these checks:

### Latest Canon

- exactly one latest accepted chapter is named
- next chapter or completion state is clear
- if the book is complete, it says complete and does not still point to a next chapter
- any draft or failed chapter is marked as draft/failed, not canon

### Cross-File Agreement

Compare with:

- `chapters/`
- `control-cards/`
- `review/reports/`
- `06-foreshadow-ledger.md`
- `07-chapter-roadmap.md`
- `logs/writing-log.md`

Check:

- latest chapter number matches accepted files
- chapter title matches accepted file name
- control card exists for latest accepted chapter
- review status is pass or user-accepted risk before canon writeback
- roadmap status agrees with chapter acceptance
- foreshadow statuses do not claim future payoffs already completed or vice versa
- writing log is not the only place a key truth appears

### Stale Or Duplicated State

Flag:

- repeated chapter summaries
- old "current" relationship states that conflict with later summaries
- old status tables that were never updated
- temporary assumptions that have been resolved but not removed
- copied review warnings that are no longer true after repair

### State Shape

Prefer current-state tables or short structured bullets over long historical paragraphs.

For each major moving piece, preserve:

- current state
- last meaningful change
- next pressure or closure state
- unresolved debt or active risk

Move long history to:

- `logs/writing-log.md`
- `10-synopsis.md`
- phase review reports
- archived notes

## Repair Procedure

1. Freeze the latest accepted manuscript and canon files.
2. Identify the latest accepted chapter and final review result.
3. Rebuild current truth from accepted chapters and canon files.
4. Compress old chapter-by-chapter history into short phase summaries.
5. Remove obsolete draft facts and duplicate "current" states.
6. Preserve unresolved hooks, debts, and assumptions.
7. Update `06-foreshadow-ledger.md` and `07-chapter-roadmap.md` if they disagree with the repaired state.
8. Append a writing-log entry describing the state repair, but do not put new story truth only in the log.

## Recommended Compact Shape

```markdown
# Dynamic State

## Latest Canon
- latest_chapter:
- accepted_at:
- next:
- completion_state:

## Current Story Position
- time:
- location:
- active_stage:
- current_reader_promise:

## Character Current States
| Character | Current State | Last Meaningful Change | Next Pressure |
|---|---|---|---|

## Relationship Current States
| Relationship | Current State | Last Bridge | Unresolved Debt |
|---|---|---|---|

## Plotline Heat
| Line | Status | Last Advance | Next Required Touch |
|---|---|---|---|

## Foreshadow And Payoff Pressure
| Item | Status | Last Touch | Due / Closed |
|---|---|---|---|

## World Rule State
- 

## Temporary Assumptions Pending Confirmation
- 

## Carryover Into Next Chapter
- 
```

## When To Run

Run this:

- every `10-20` chapters in marathon mode
- after a D-grade repair or major rewrite
- before a volume finale
- before starting a new volume
- when review reports mention state drift
- when two canonical files disagree
- when dynamic state grows so large that new chapter setup becomes error-prone

