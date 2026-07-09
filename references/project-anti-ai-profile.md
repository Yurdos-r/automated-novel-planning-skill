# Project Anti-AI Profile

Use this reference when a novel needs project-specific calibration for AI-flavor review. It is a reusable method, not a genre-specific content library.

The goal is to keep the precision of a project-local anti-AI analysis library without copying any one project's vocabulary, scenes, relationship model, or private source material.

## When To Create Or Read The Profile

Create or update a project-local file such as:

- `10-anti-ai-profile.md`
- `11-anti-ai-profile.md` when `10-mechanics-calibration.md` already exists
- `anti-ai-profile.md`
- `.claude/memory/feedback-anti-ai-profile.md`

Use it when:

- the project has strong genre-canon words, invented terms, professional terms, setting mechanics, or recurring motifs
- the user reports repeated "AI flavor" or generic prose even after normal cleanup
- chapters repeatedly overuse the same gestures, labels, dialogue tags, emotional summaries, or motif phrasing
- the project needs to distinguish necessary type texture from empty jargon
- a formal chapter review needs evidence-based prose diagnosis rather than vague taste comments

Do not create a large profile for a simple short scene unless the user asks for sustained style control.

## Core Principles

- Context beats wordlists. A word is not AI-flavor by itself; density, function, point of view, and scene pressure decide.
- Type-canon terms are allowed when they are needed for genre promise, world rules, character knowledge, or reader orientation.
- A term becomes risky when it replaces choice, consequence, body distance, dialogue failure, or material scene pressure.
- Over-defense creates new AI-flavor. Do not delete every genre word, professional term, or bodily reaction until the prose becomes evasive or flavorless.
- Micro-detail is not automatically life. Do not over-disassemble a bodily reaction into slow, mechanical fragments unless the point of view actually notices it that way.
- Repetition is judged by inventory, not isolated lines. Track repeated gestures, static labels, punctuation habits, motif syntax, and scene shells across recent chapters.
- Repair should make the scene more alive, not merely less detectable.

## Project-Local Template

Use this compact structure for a project profile:

```markdown
# Project Anti-AI Profile

## Type Canon Terms
- allowed_terms:
- allowed_when:
- overuse_warning:
- must_not_replace:

## High-Risk Shells
- banned_phrases:
- risky_sentence_shapes:
- punctuation_risks:
- static_labels:

## Action Inventory Watch
- repeated_gestures:
- repeated_body_reactions:
- micro_expression_limits:
- replacement_strategy:

## Motif And Callback Syntax
- recurring_motifs:
- forbidden_fixed_syntax:
- required_variation:
- source_chapters_to_check:

## Genre Mechanism Risks
- mechanism:
  - useful_for:
  - must_not_replace:
  - consequence_required:
  - review_checks:

## Scene Cards
- scene_type:
  - type_canon_allowed:
  - over_defense_risk:
  - required_human_pressure:
  - hard_failures:

## Scoring
- target_range:
- hard_blocker_threshold:
- current_project_notes:
```

## Scoring Model

Score each meaningful paragraph, dialogue exchange, or pressure unit from `0` to `3`:

- `0`: natural for this project; terms and rhythm serve scene pressure
- `1`: mild generic drift; revise locally
- `2`: visible AI-flavor or over-managed prose; revise the unit and recheck nearby paragraphs
- `3`: template prose, hollow mechanism, repeated shell, or scene-level falseness; rewrite the pressure unit

Whole-chapter guide:

- `0-8`: basically natural; only polish local roughness
- `9-18`: AI-flavor visible; run a focused authenticity pass
- `19-35`: obvious patterning; rewrite affected scenes or pressure units
- `36+`: likely template frame; return to the control card, scene mission, or project profile before rewriting

Adjust thresholds only when the chapter is unusually short or unusually long, and record the reason.

## Five Human-Presence Checks

For each scene or pressure unit, confirm:

- concrete trouble: someone faces an immediate material, social, emotional, or tactical problem
- life anchor: the scene contains a specific observable object, place, bodily constraint, habit, or memory point
- dialogue failure: speech can dodge, miss, interrupt, overreach, or expose pressure rather than perfectly explain
- body and action: gestures change distance, status, timing, or consequence instead of decorating emotion
- mechanism landing: genre rules, clues, powers, institutions, or professional terms force choices and costs rather than replacing them

If a unit fails all five, the problem is probably not wording. Rebuild the scene pressure first.

## Three-Step Repair

1. Delete author conclusions: remove lines that explain what the reader should think or feel.
2. Add observable facts: replace abstract judgment with action, dialogue, object state, social reaction, or consequence.
3. Leave incompleteness: let characters misunderstand, avoid, understate, or fail when that is more human than a neat summary.

After repair, re-score the affected unit. If the score improved but the scene lost genre promise or character voice, restore the necessary project texture and recheck density.

## Use In Chapter Control Cards

Before drafting, write the active risks into the chapter control card:

- `anti_ai_profile_reference`
- `type_canon_terms_allowed`
- `project_ai_risks`
- `scene_specific_ai_risks`
- `action_inventory_watch`
- `motif_syntax_watch`
- `genre_mechanism_risk`
- `over_defense_risk`
- `ai_flavor_score_target`

Keep this short. The control card should identify the active risks for this chapter, not paste the whole profile.

## Use In Review

During formal review:

- list the project anti-AI profile in `Sources Read` when used
- cite concrete evidence for high-risk shells, repeated action inventory, motif fixed syntax, or type-canon overuse
- do not penalize a project-approved term merely because it is common in the genre
- do penalize a project-approved term when it lets the prose skip choice, cost, sensory pressure, or relationship movement
- record whether repair should happen at line level, scene-unit level, control-card level, or project-profile level

## Exit Questions

- Which words are necessary project texture, and which are doing fake work?
- Which gestures, labels, or sentence shapes have become stock buttons?
- Did the cleanup remove genre promise or only remove genericity?
- Did the scene become more observable, more pressured, and more character-specific?
- Is the remaining roughness human voice, or is it still template drift?