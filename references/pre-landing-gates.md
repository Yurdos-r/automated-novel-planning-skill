# Pre-Landing Gates

Use this after a chapter draft exists but before accepting it into `chapters/`.

Goal: keep cheap, measurable failures out of the accepted manuscript layer. A draft can be promising and still fail pre-landing. Fix the draft first, then accept it.

## Landing Model

Preferred chapter states:

- draft: temporary manuscript in `drafts/` or `.claude/tmp/`
- pre-landed: draft has passed the gates below
- accepted: manuscript is saved in `chapters/` and is ready for final review and writeback

Do not update `08-dynamic-state.md`, foreshadow ledgers, relationship maps, or writing logs from a draft that has not passed pre-landing gates.

## Gate 0: Size And Completeness

Check:

- chapter has a title or numbered header when the project requires it
- no placeholder markers remain
- no obvious truncation or dangling scene note remains
- net body length meets the project floor
- word count is based on real body text, not line count

Default Chinese web-serial floor:

- red floor: `>= 3000` CJK characters
- natural target: `3500-4500` CJK characters
- yellow zone: `3000-3199`, mark as thin
- over `5000`, check for padding, repeated interiority, or inert environment prose

If the project sets another length target in `09-style-guide.md` or the chapter control card, use that instead and record the active target.

If size fails, repair by adding missing scene pressure, consequence, dialogue, or aftershock. Do not add filler just to reach the number.

## Gate 1: Text Hygiene And AI Pattern Scan

Check:

- English quotes in Chinese prose
- unpaired Chinese quotes
- nonstandard quote style when the project locks one quote style
- repeated adjacent lines or duplicated sentences
- chapter number leakage in body text
- excessive em dashes
- dense "not X but Y" / "not only X but Y" contrast shells
- question sentences ending with a period when the project treats this as punctuation drift
- overly neat summary or theme-translation sentences
- static abstract labels replacing action, distance, voice, or consequence
- fixed motif phrases repeated in the same grammar across recent chapters

Use `scripts/chapter_lint.py` before manual review when available.

If this gate finds hard blockers, fix them before saving the manuscript into `chapters/`.

## Gate 5: Paragraph And Rhythm Compliance

Check the active `paragraph_mode` from `09-style-guide.md` and the control card.

For `web-serial-natural`:

- most narrative paragraphs should carry `2-4` sentences
- single-sentence narrative paragraphs need a real pressure job
- three or more consecutive single-sentence narrative paragraphs need a merge check
- one speaker's continuous beat, attached action, and short follow-up usually stay together
- blank lines should mark scene, time, point-of-view, speaker, or pressure turns
- punctuation should support rhythm, not replace action or emotional consequence

For `long-paragraph`:

- allow continuous interiority or literary movement
- still break on speaker change, scene/time shift, point-of-view shift, or major pressure turn
- do not let continuity become inert exposition

## Gate 8+: Control Card And Light Continuity

This gate is a fast intent and continuity check. It does not replace final chapter review.

Compare the draft with the current control card:

- did the scene units or pressure units execute
- did the chapter's core goal actually land
- did the required prior debt get answered or consciously deferred
- did the ending hook match the actual ending
- did `forbidden_drift` stay avoided
- did style, paragraph, dialogue, suspense, or authenticity tasks land when active

Also check:

- emotional state, relationship state, or plot pressure changed from opening to ending
- characters behave within their current relationship and arc phase
- point of view does not solve core moments by reading inaccessible information
- world rules in play do not contradict `02-worldbuilding.md` or the project calibration file
- foreshadows and roadmap obligations are not skipped, paid off too early, or inflated beyond their pressure level
- any high-pressure intimacy, violence, magic, illness, or rule-break scene preserves agency, boundary, consequence, and follow-through

## Pass / Fail Rules

Pre-landing passes only when all active gates are in the pass band:

- `A`, `A-`, or `B`: may land
- `C` or `D`: must repair and rerun the failed gate

If only one localized hygiene issue remains and the fix is deterministic, fix it directly and rerun that gate.

If Gate 8+ fails because the control card was wrong but the draft is better, record this as a positive deviation, repair the control card and roadmap during writeback, and still verify continuity before landing.

## Output Shape

Record a compact pre-landing note in the review report or writing log:

```markdown
## Pre-Landing Gates
- gate_0_size: pass/fail, metrics
- gate_1_text_hygiene: pass/fail, blockers
- gate_5_paragraph_rhythm: pass/fail, blockers
- gate_8_control_continuity: pass/fail, blockers
- chapter_lint_ran: yes/no
- landed_to_chapters: yes/no
```

