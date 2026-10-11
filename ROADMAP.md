# Roadmap

This roadmap is a proposal based on the current source snapshot. Update checkboxes only after the work has been completed and verified.

## Reliability

- [ ] Fix the mismatch between `tests/testcore.py` and the current core API (`xor_encrypt` / `xor_decrypt`).
- [ ] Add end-to-end tests for embedding a message in an image and extracting it.
- [ ] Add tests for wrong keys, malformed images, missing terminators, and oversized messages.
- [ ] Ensure Unicode messages round-trip correctly.

## Security and correctness

- [ ] Decide whether the `xor` mode should be implemented correctly or removed/renamed.
- [ ] Review the use of Fernet and password-based key derivation.
- [ ] Handle wrong-password and corrupted-token errors consistently.
- [ ] Document capacity limits and the effect of image formats / pixel modes.

## Usability

- [ ] Improve CLI validation and return non-zero exit codes on failures.
- [ ] Let the user choose an output location consistently.
- [ ] Add screenshots and a short demo to the README.
- [ ] Improve GUI messages for unsupported files and failed extraction.

## Documentation and contribution

- [ ] Verify setup instructions on a clean Windows environment.
- [ ] Add a selected open-source license.
- [ ] Add GitHub issue templates and CI test workflow.
