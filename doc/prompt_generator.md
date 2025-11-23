**Prompt Generator**

This document explains the intent and usage of the prompt generator patterns used by RunescapeGPT. It provides a short template, examples, and best-practices so contributors can create consistent, testable prompts for gameplay assistance, NPC interactions, and content generation.

## Prompt Generator

This document explains the intent and usage of the prompt generator
patterns used by RunescapeGPT. It provides a short template, examples,
and best practices so contributors can create consistent, testable
prompts for gameplay assistance, NPC interactions, and content
generation.

## Purpose

- Provide canonical prompt templates for tasks the app performs
	(conversation, summarization, retrieval-augmented responses).
- Make prompts easy to review, test, and iterate in PRs.

## Prompt template

- **Instruction:** A short sentence describing the agent's role (e.g.,
	"You are a helpful RuneScape guide").
- **Context:** Any game state, player inventory, or retrieval results to
	include.
- **Goal:** The expected output format or constraints (e.g., "Return
	JSON with keys 'advice' and 'items'").
- **Examples (optional):** 1–3 short examples showing inputs and
	desired outputs.

Example:

```
Instruction: You are a helpful RuneScape guide.
Context: Player level 60 Attack, has Rune scimitar, 50 food.
Goal: Suggest an optimal PvM rotation and short gear checklist. Return
plain text with bullet points.
```

## Variables and interpolation

- Use explicit variable names when generating prompts (for example:
	`{{player_level}}`, `{{inventory}}`, `{{location}}`).
- Validate that all required variables are present before sending the
	prompt to the model.

## Safety and rate-limiting

- Avoid sending long raw logs as a single prompt; prefer summarized
	retrieval results.
- For any user-provided text, sanitize or truncate to avoid prompt
	injection and keep token usage predictable.

## Testing prompts

- Add unit-style examples in PRs demonstrating a small input →
	expected output. Keep examples deterministic where possible.
- When changing a core prompt, include a short rationale in the PR
	description and the expected model behavior.

## PR checklist for prompt changes

- Include the before/after prompt text in the PR description.
- Add 1–2 tests/examples verifying expected outputs.
- Note any changes in token usage or cost implications.

If you want, I can also add a tiny test harness (`tests/test_prompts.py`)
that loads prompt templates and validates interpolation and a few
example outputs.
