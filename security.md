# Security Overview

## Intended users
This repository is intended for the course staff and students enrolled in this class. It contains course programming assignments, notebooks, and supporting data used for educational purposes.

## Risk assessment
If the code or data in this repository fell into the wrong hands, the main risks would be academic integrity and misuse of assignment solutions. The datasets included appear to be educational / synthetic, but model artifacts, feature engineering, or analysis workflows could still be misused to shortcut coursework or misrepresent results. There is no credential material or production infrastructure in this repo, so risks like account compromise mainly come from accidentally committing secrets.

## Steps taken to secure the repo
- A `.gitignore` is used to avoid committing local or temporary artifacts such as virtual environments and cache files.
- A `CODEOWNERS` file is included to define ownership and review responsibility.
- GitHub branch rulesets are enabled on the default branch to prevent deletion and force-pushes and to require CODEOWNER review for pull requests.
- No secrets (API keys, passwords, or tokens) are stored in this repository.