# Project Status

This file describes the source snapshot used to prepare the repository documentation. Re-test after making changes.

## Present in the source

- Python core module for image pixel manipulation and message extraction.
- Fernet-based encryption helper functions.
- CustomTkinter GUI.
- CLI encrypt/decrypt subcommands.
- Example image and test file.

## Needs verification / follow-up

- The current tests import XOR helper functions not present in `steganography/core.py`; test execution may fail.
- The `xor` branch in the current core code does not apply XOR encryption to the message.
- Verify CLI output path behaviour and confirm the GUI's save behaviour.
- Add explicit dependency/version documentation and verify on a clean environment.
- Choose and add a license before inviting reuse.

## How to update this file

When a task is completed, run its tests, update this status, and reference the relevant pull request or issue.
