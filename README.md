# Research Assistant

Academic research facilitation skill for Codex. It is designed to take a rough research idea and help turn it into a structured academic workflow: idea clarification, literature search, research design, analysis planning, journal targeting, and IMRaD manuscript drafting.

## What This Skill Does

- interview the researcher to clarify the idea before searching
- search public academic literature using abstracts and accessible full texts
- build a literature matrix and identify the research gap
- produce a defensible research plan with data and analysis requirements
- help create reproducible analysis workflows, tables, and figures
- identify journals that fit the study
- draft citation-verified IMRaD manuscripts without fabricating references or results

## Repository Contents

This repository contains the skill itself:

- `SKILL.md`
- `agents/openai.yaml`
- `references/`
- `scripts/install.py`
- `scripts/install.ps1`

## Install

### Option 1: Clone anywhere, then install

```powershell
git clone https://github.com/danlinyu/research-assistant.git
cd research-assistant
python .\scripts\install.py
```

On Windows PowerShell you can also run:

```powershell
.\scripts\install.ps1
```

The installer places the skill at:

- `$CODEX_HOME/skills/research-assistant` if `CODEX_HOME` is set
- otherwise `~/.codex/skills/research-assistant`

To replace an existing install:

```powershell
python .\scripts\install.py --force
```

### Option 2: Clone directly into the Codex skills directory

```powershell
git clone https://github.com/danlinyu/research-assistant.git ~/.codex/skills/research-assistant
```

## Use

Invoke the skill in Codex with prompts such as:

- `Use $research-assistant to interview me about a study idea.`
- `Use $research-assistant to search the literature for this idea and produce a research plan.`
- `Use $research-assistant to identify target journals and draft an IMRaD manuscript shell.`

## Requirements

- Codex with skill support
- Python available in `PATH` if you want to use the installer script

`PyYAML` is only needed if you want to run the optional skill validator locally.

## Notes

- The skill is academic-focused, not general-purpose web research.
- It is opinionated about citation integrity: it should never fabricate citations, journal requirements, datasets, or results.
- The repository `README.md` is for GitHub users; the installer intentionally does not copy it into the installed skill folder.
