# AI Coding for Science Workshop

Materials for the hands-on tutorial half of the *AI for Scientific Coding* workshop: an introduction to using AI coding tools (GitHub Copilot Chat in VS Code) for everyday research code.

This repo contains the practical lab. The conceptual/lecture half of the workshop (what LLMs are, how they're trained, prompting, responsible use) is covered separately in the accompanying slides.

## What's in here

| File | Purpose |
|---|---|
| `Part2_Hands_On_Lab.ipynb` | The guided lab notebook: nine short activities plus an optional bonus round |
| `environment.yaml` | Conda environment definition for the lab |

## Setup (do this before the session)

### 1. Install VS Code
Download and install from [code.visualstudio.com/download](https://code.visualstudio.com/download).

### 2. Create a GitHub account
Sign up at [github.com/signup](https://github.com/signup) if you don't already have one.

### 3. Get GitHub Copilot access
Free GitHub Copilot Pro is available to verified teachers, researchers, and staff via GitHub Education. Apply at **github.com/settings/education/benefits** (search GitHub's docs for "apply to GitHub Education as a teacher" if that link moves). Approval isn't instant, so apply well ahead of the workshop. Students can use the [Student Developer Pack](https://education.github.com/pack) instead — worth double-checking Copilot is currently included, as this has occasionally been paused for new sign-ups.

### 4. Clone this repo
```bash
git clone https://github.com/headmetal/AI-Coding-For-Science-Workshop.git
cd AI-Coding-For-Science-Workshop
```

### 5. Create and activate the conda environment
```bash
conda env create -f environment.yaml
conda activate ai_coding_workshop_env
```
This reads `environment.yaml` and builds a new conda environment called `ai_coding_workshop_env` with everything the notebook needs (Python, xarray, numpy, pandas, matplotlib, cartopy, and Jupyter). It only needs to be created once — after that, `conda activate ai_coding_workshop` is all you need each time you come back to this.

### 6. Launch and connect everything
1. Open this folder in VS Code (`code .`).
2. Sign in to GitHub via the Accounts icon (bottom-left) — this activates Copilot Chat.
3. Open `Part2_Hands_On_Lab.ipynb`.
4. Select **ai_coding_workshop** as the notebook kernel (top-right kernel picker).

You're ready when Copilot Chat is visible in the sidebar and the notebook runs without import errors.

## Using the notebook

The lab is fully guided. Each activity has a short setup, a suggested task, and space to paste in and test what Copilot Chat produces. Work through them in order during the session; the optional bonus round at the end (building a custom AI skill and agent) is there for anyone who finishes early or wants to keep exploring afterward.

## Requirements

- VS Code with the GitHub Copilot and Copilot Chat extensions
- An active GitHub Copilot subscription (see setup step 3)
- Conda or Miniconda
- Internet access (needed for Copilot itself, and for the bonus skill/agent activity)

## Questions

Raise an issue in this repo, or ask during the workshop.
