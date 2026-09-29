# exec-core

Foundation for the exec-skills marketplace. Every other plugin inherits its standards. Install it first.

## Overview

This plugin holds the four standards the system runs on (how claims are made, how prose is written, how posture is diagnosed, how the Career Brain is read and written), the researched source library, and the front-door commands.

## Skills (5)

- **brain-protocol**: How exec-* skills locate, read, and write the user's private Career Brain and read their Product Brains (pm-brain scaffolds or others). Defines what to load for each job, the Product Brain adapter, write rules, provenance, privacy boundaries, staleness checks, and degraded mode when no Brain exists.
- **doctrine-library**: Runtime access to the researched source doctrine behind the exec-* skills: Campbell, Cagan, Doshi, Grove, Hughes Johnson, Charan, McCord, Horowitz, Scott, Slootman, Pfeffer, Hewlett, Watkins, Ibarra, Minto, Lencioni, Larson, Bezos/Amazon, Duke, Rumelt, and others.
- **evidence-discipline**: The epistemic and candor standard for executive-development coaching. Separates observation, evidence, inference, hypothesis, and recommendation; calibrates confidence from longitudinal evidence; forbids stating motives or perceptions as fact; refuses flattery.
- **executive-posture**: Diagnose the organizational posture a behavior, message, or meeting contribution signals (coordinator, project manager, subject-matter expert, product manager, product leader, organizational leader, executive), identify the underlying behavior producing that signal, and prescribe the behavior change rather than a wording change.
- **executive-prose**: The writing standard every exec-* output inherits, including the coach's own replies. Answer first, hierarchy over chronology, implications over activity, recommendations over option lists, ownership over coordination, density over completeness, natural operator cadence. Bans corporate filler and AI writing tells.

## Commands (3)

- `/capture`: Turn raw notes, a transcript, feedback, or a quick description into disciplined evidence entries in your Career Brain
- `/coach-me`: Get specific, evidence-based coaching on a real situation, reasoning across executive doctrine, your Career Brain, and your product context
- `/setup-career-brain`: Create your private Career Brain from the scaffold, run a short interview to seed it, and connect your Product Brains

## Install

```bash
claude plugin marketplace add <path-or-repo>/exec-skills
claude plugin install exec-core@exec-skills
```
