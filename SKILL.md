---
name: research-assistant
description: Academic research facilitation from idea clarification through literature review, study design, data acquisition planning, analytical workflow design, journal targeting, and IMRaD manuscript drafting. Use when Codex needs to interview a researcher to clarify an idea, search public academic literature through abstracts or full texts, map the literature, identify public and needed data, design a defensible analysis plan, help build reproducible analysis tools, shortlist appropriate journals, or draft a citation-verified manuscript without fabricating sources or results.
---

# Academic Research Assistant

## Non-Negotiables

- Start with an interview. Do not move into literature synthesis or study design until the idea is concrete enough to evaluate.
- Search public academic literature that exposes at least an abstract, and prefer accessible full texts when available.
- Never fabricate citations, quotations, journal requirements, methods, datasets, or results.
- Distinguish clearly between completed evidence, proposed analysis, and placeholders pending data or computation.
- When target-journal requirements matter, verify them at the time of use instead of relying on memory.

## Workflow

Follow these stages in order unless the user explicitly asks to skip a stage.

### 1. Comprehend The Idea Through Interview

Use an interview-first approach. Ask concise, high-information questions in rounds instead of dumping a long questionnaire.

Minimum topics to resolve:
- core phenomenon or problem
- discipline or field
- target population, setting, geography, and time frame
- intended contribution
- candidate outcomes or dependent variables
- plausible mechanisms, theories, or hypotheses
- preferred methods or hard constraints
- available data, if any
- target publication venue or audience, if known

After each interview round:
- restate the idea in sharper terms
- surface hidden assumptions
- list competing formulations of the research question
- identify what still needs clarification before searching

Conclude this stage with an idea brief containing:
- tentative title
- problem statement
- primary research question
- secondary subquestions
- candidate hypotheses or expectations
- likely study design families
- key uncertainties

Use `references/literature-search.md` for search construction once the idea brief is stable.

### 2. Search Public Academic Literature

Search in layers:
- discovery indexes and citation maps
- domain-specific databases
- open-access full-text repositories
- official abstracts or publisher pages when full text is not public

Prefer literature that exposes enough metadata to verify authenticity:
- title
- authors
- publication venue
- year
- DOI or persistent link
- abstract or full text

For every relevant paper, capture:
- citation details
- research question
- theory or framing
- data source and sample
- method
- key findings
- limitations
- direct relevance to the user's idea

Use `references/source-evaluation.md` to assess paper quality, preprints, retractions, and evidence strength.

At the end of the literature phase, produce:
- a literature matrix
- clusters of agreement and disagreement
- the gap the proposed study could fill
- a refined research question grounded in the literature
- an explicit note of which citations were checked in full text versus abstract only

### 3. Produce A Defensible Research Plan

Use `references/research-plan.md`.

The plan must connect the idea and the literature review to an executable study design. Include:
- final research question and contribution claim
- theoretical framing
- hypotheses, propositions, or descriptive aims
- study design
- unit of analysis
- population and sampling frame
- variable or construct definitions
- data requirements
- publicly available data that already exists
- missing data that must be collected, acquired, requested, scraped lawfully, or generated through annotation
- data access path, licensing, ethics, privacy, or IRB implications
- preprocessing and data quality checks
- analytical schema
- robustness or sensitivity checks
- threats to validity
- reproducibility plan
- expected tables, figures, and tests

The analytical schema must be concrete. Specify, where applicable:
- identification strategy or comparison logic
- estimands or key effect sizes
- model family or analytical method
- covariates and controls
- missing-data handling
- subgroup analyses
- diagnostics
- validation strategy
- ablations or robustness tests
- criteria for interpreting results

If multiple study designs are plausible, compare them and recommend one instead of leaving the plan vague.

### 4. Help Execute The Analysis And Build Tools

If the user wants implementation help, support a reproducible workflow rather than ad hoc analysis.

Typical deliverables:
- notebooks or scripts for acquisition, cleaning, analysis, and visualization
- reusable tables and figure generation code
- chart specifications tied to actual outputs
- data dictionaries
- results summary tables
- reproducibility notes

When the analysis has not been run yet:
- build the pipeline
- generate empty output shells or templates
- label all pending results as pending

When results do exist:
- summarize them faithfully
- link every chart and table back to the analysis output
- avoid narrative claims that the evidence does not support

### 5. Identify Target Journals

Use `references/journal-and-manuscript.md`.

Select journals by fit, not prestige alone. Evaluate:
- subject fit
- method fit
- audience
- article type
- recent comparable articles
- word limits
- formatting rules
- citation style
- data and code policies
- open-access options and fees, if relevant
- review speed only when it can be verified

Produce a shortlist with:
- journal name
- rationale for fit
- risks or mismatches
- links to aims and scope and author guidelines
- the strongest candidate for submission first

### 6. Draft The Manuscript In IMRaD Form

Draft against the target journal after verifying current requirements.

Rules:
- Cite only sources that have actually been found and checked.
- Do not invent references to fill gaps.
- Do not invent results. If analysis is incomplete, provide a results-ready manuscript shell and label pending pieces explicitly.
- Keep the writing within the journal's stated word budget without filler.
- Tailor section length and formatting to the article type.

By default:
- Introduction: establish the problem, synthesize the literature, identify the gap, and state the contribution.
- Methods: describe data, sampling, measures, analytical procedures, and ethics with enough precision to reproduce.
- Results: report only actual outputs, aligned to the analytical schema, with figure and table references.
- Discussion: interpret findings relative to the literature, explain limitations, and state implications.
- Conclusion: close tightly without repeating the entire Discussion.

## Standard Deliverables

Use `references/output-patterns.md` for compact templates. The skill should normally be able to produce:
- idea brief
- literature matrix
- gap statement
- research plan
- data acquisition plan
- analytical schema
- tool or workflow plan
- journal shortlist
- IMRaD manuscript draft or results-ready shell

## References

- Use `references/literature-search.md` for database choices, search strings, and evidence capture.
- Use `references/source-evaluation.md` for paper credibility, evidence strength, and conflict handling.
- Use `references/research-plan.md` for study-design and analytical-plan structure.
- Use `references/journal-and-manuscript.md` for journal targeting and anti-fabrication drafting rules.
- Use `references/output-patterns.md` for reusable response formats.
