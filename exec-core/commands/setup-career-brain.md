---
description: "Create your private Career Brain from the scaffold, run a short interview to seed it, and connect your Product Brains"
argument-hint: "<optional: folder to create it in>"
---

# /setup-career-brain

Input: $ARGUMENTS

Bootstraps the Career Brain: the persistent, private record every exec-* workflow reasons over.

## Invocation

```
/setup-career-brain
/setup-career-brain ~/Documents/career-brain
```

## Workflow

### Step 1: Choose the location

Load **exec-core:brain-protocol**. Its skill directory contains `scaffold/career-brain/`.

- If a path was given, use it. Otherwise propose `~/Documents/career-brain/` and confirm.
- Check the location is private: not inside a shared drive, a team repo, or a Product Brain that others can read. If the proposed parent is a git repo with a remote, warn and suggest another location.
- If a `CAREER-BRAIN.md` already exists there, stop: this is an existing Brain. Offer to check it against the current scaffold instead.

### Step 2: Interview

Ask in short batches and confirm back before writing. Skip anything the user has already provided. Accept pasted documents (review packets, ladder docs, org charts) in place of answers.

- **A. Role and company:** title, company and what it sells, time in role, manager and skip-level, what the user owns, decision rights (what they decide without asking), what they're measured on, what their manager is measured on.
- **B. Ambitions:** next role and horizon, the one after, why, what they'd trade, here or elsewhere.
- **C. People:** the 5-12 people who most affect their trajectory: manager, skip-level, key executives, peers, and anyone who has advocated for them (set the ladder level from evidence, whatever the user calls them). For each: title and relationship, plus one or two recent interactions if easy to recall.
- **D. Level model:** the official ladder for current and next level, if it exists; recent promotions to the next level and what those people had done; how promotions are decided.
- **E. Product Brains:** paths to the user's Product Brains. Check each path exists. Detect type: a folder with `INDEX.md` titled "PM Brain" is `pm-brain`; anything else is `other`. If a parent folder holds several brains, register each.
- **F. Preferences:** weekly review day; autonomy (keep defaults unless the user wants otherwise).

### Step 3: Copy the scaffold

Copy every file and folder from the scaffold into the chosen location, including dotfiles (`.gitignore`, `.gitkeep`).

- Bash: `cp -R <scaffold>/career-brain/. <dest>/`
- PowerShell: `Copy-Item -Recurse -Force <scaffold>\career-brain\* <dest>\` then `Copy-Item -Force <scaffold>\career-brain\.gitignore <dest>\`

Then rename the two templates in the destination: `CAREER-BRAIN.md.tmpl` to `CAREER-BRAIN.md` and `CLAUDE.md.tmpl` to `CLAUDE.md`. (They ship with a `.tmpl` suffix so the plugin's own copy is never mistaken for a live Brain or loaded as an operating manual.)

Verify by listing the destination: `CAREER-BRAIN.md`, `CLAUDE.md`, `INDEX.md`, `self/`, `people/`, `evidence/`, `models/`, `meetings/`, `reviews/`, `inbox/` must all exist, and no `.tmpl` files remain.

### Step 4: Populate

- Replace `{{PLACEHOLDERS}}` from interview answers. Leave `TODO` where the user didn't answer.
- `self/current-role.md`: fill decision rights carefully; posture diagnoses depend on them.
- One `people/<slug>.md` per person from batch C, facts only, plus rows in `people/INDEX.md`. Sponsorship level defaults to `contact` or `ally` unless the user describes dated acts that qualify a higher level (see exec-influence sponsorship ladder).
- `brains.md`: one row per Product Brain. For `other` types, do the adapter discovery once and record the mapping. If a person has a `stakeholders/<slug>.md` in a Product Brain, link it from their person file.
- Any concrete events from the interview become evidence entries with `source: self-assessment` or `direct` as appropriate.
- `models/trajectory.md`: propose an initial H-T1 at low confidence, marked as a starting hypothesis built on self-report. No rate estimate until the evidence supports medium confidence.

### Step 5: Pointer

Ask permission to add one line to the user's `~/.claude/CLAUDE.md` so every session can find the Brain:

```
Career Brain: <absolute path>
```

Do not edit that file without a yes.

### Step 6: Self-test

- Every link in `INDEX.md` resolves.
- Every Product Brain path in `brains.md` exists.
- No `{{PLACEHOLDER}}` remains outside fields the user skipped.
- `CAREER-BRAIN.md` and `CLAUDE.md` are present at the root, with no `.tmpl` copies left.
- Every `[Name](../people/<slug>.md)` link written during setup resolves.

### Step 7: Report and next steps

Write-back summary, the list of TODOs that matter most (usually decision rights, the revealed ladder, and what the manager is measured on), and:

- "Paste or point me at recent 1:1 notes and I'll `/capture` them."
- "Run `/review-my-week` at the end of the week to start the loop."

## Notes

- The interview should take 10-20 minutes. Don't turn it into a questionnaire; partial is fine and fills in over time.
- Nothing about named people goes anywhere except this Brain.
