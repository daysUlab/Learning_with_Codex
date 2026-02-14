# AGENTS.md

## Agent Operating Rules (Learning_with_Codex)

### Mode Switch By Prefix

- Default behavior: treat user input as Act mode when no prefix is provided.
- Plan mode trigger: when the first token is `p` (examples: `p ...`, `p: ...`), execute analysis-only behavior.
- Act mode behavior: execute implementation actions end-to-end (edit files, run commands, tests, git operations).

### Prefix Parsing

- If input starts with `p` followed by whitespace or `:`, strip that prefix and treat the remainder as the actual request in Plan mode.
- If there is no `p` prefix, treat the request as Act mode.

### Collaboration Notes

- In Plan mode, return a short actionable plan and expected next command(s).
- In Act mode, execute end-to-end and report concrete results.
- In Act mode, when implementation changes behavior or workflow, update `SPEC.md` in the repository root to reflect the latest state.
- In every response, include a `Next Action（次アクション案）` section for the user.

### Git / PR Operation Policy

- Always work on the agent branch `work` unless the user explicitly instructs otherwise.
- For each task cycle, keep branch state clean and synchronized:
  - run `git fetch --all --prune`
  - run `git pull --ff-only` on the current branch before new changes when possible
  - if `git pull --ff-only` fails due to no upstream, set tracking first (`git branch --set-upstream-to=origin/work work`) and retry
  - if fast-forward is not possible, run `git rebase origin/work` first, then continue
  - if needed, synchronize with `main` (e.g., `git pull --ff-only origin main` or rebase/merge as instructed)
- After making changes:
  - run relevant tests/checks
  - commit on `work`
  - push to `origin/work`
  - create a Pull Request
  - provide the PR URL to the user
- For every interaction in Act mode, always run `git push origin work` and create/update a Pull Request.
- After sending a Pull Request, always include the PR URL in the user-facing report (if already included, no extra action is needed).
- If push/PR fails, report exact error and fallback steps immediately.

### Language / Communication Policy

- All deliverables must be in Japanese, including:
  - commit messages
  - PR title/body
  - status reports to the user
- Keep instructions concise but explicit enough for reproducibility.

### GitHub CLI / Remote Bootstrap

Before push/PR, run the bootstrap below to ensure `gh` and `origin` are ready in ephemeral environments.
If `GITHUB_TOKEN` is available, authenticate immediately in the same session and then unset the variable.

```bash
set -euo pipefail

if ! command -v gh >/dev/null 2>&1; then
  if command -v apt-get >/dev/null 2>&1; then
    apt-get update -y -qq
    apt-get install -y -qq gh
  fi
fi

if [ -n "${GITHUB_TOKEN:-}" ]; then
  token="$GITHUB_TOKEN"
  unset GITHUB_TOKEN

  echo "$token" | gh auth login --with-token
  gh auth setup-git
fi

if ! git remote get-url origin >/dev/null 2>&1; then
  git remote add origin https://github.com/daysUlab/Learning_with_Codex.git
else
  git remote set-url origin https://github.com/daysUlab/Learning_with_Codex.git
fi
```

### PR Creation Fallback (GitHub CLI)

If PR URL is not available via other tools, run GitHub CLI directly and return the URL.
Use single quotes in examples to avoid shell interpolation issues with parentheses/backticks.

```bash
gh pr create --base main --head work --title 'docs: AGENTS.md運用ルールを更新' --body 'AGENTS.mdの運用ルールを更新'
gh pr list --head work --state all
```
