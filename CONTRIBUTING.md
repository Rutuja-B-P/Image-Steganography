# Contributing

Thank you for considering a contribution to Image Steganography!

## Before you start

1. Read the README and check the open GitHub Issues.
2. Comment on the issue you want to work on so work is not duplicated.
3. For a substantial change, discuss the proposed approach before coding.
4. Never commit passwords, API keys, personal data, or private images.

## Development setup

```powershell
py -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
pip install pillow numpy customtkinter cryptography
```

## Branch naming

Use a descriptive branch name, for example:

- `docs/improve-installation`
- `test/fix-core-tests`
- `fix/xor-mode`
- `feat/input-validation`

## Workflow

1. Sync your local `main` branch.
2. Create a branch for one issue.
3. Make a focused change.
4. Run the tests and manually check the relevant GUI or CLI workflow.
5. Commit with a clear message.
6. Push the branch and open a pull request.
7. In the PR description, explain what changed, how it was tested, and link the issue (for example, `Closes #3`).

## Commands

```bash
git checkout main
git pull origin main
git checkout -b fix/issue-number-short-description
python -m unittest discover -s tests -v
git add .
git commit -m "Fix: describe the change"
git push -u origin fix/issue-number-short-description
```

Replace the example branch name with your actual issue number and task.

## Pull request checklist

- [ ] The change addresses one issue or has a clear reason to be standalone.
- [ ] I tested the changed behaviour.
- [ ] I added or updated tests where appropriate.
- [ ] I updated documentation if behaviour or setup changed.
- [ ] I did not include generated files, local environments, secrets, or unrelated changes.
- [ ] I described any limitations or follow-up work.

## Code expectations

- Keep functions focused and readable.
- Validate file paths, image formats, message length, and required inputs.
- Avoid silently swallowing exceptions.
- Do not describe the XOR mode as encryption unless the implementation actually performs XOR and has suitable tests.
- Security-related changes should include tests for wrong keys, malformed input, and failure cases.
