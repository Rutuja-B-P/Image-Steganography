# Image Steganography

A Python application that hides a text message inside an image and extracts it later. It provides a graphical interface and a command-line interface, with selectable message-processing modes.

> **Project status:** This repository is being prepared for open collaboration. Verify the installation instructions and test suite on a clean environment before describing the project as production-ready.

## Features

- Hide a text message in image pixel data using least-significant-bit (LSB) modification.
- Extract a hidden message from an image.
- GUI built with CustomTkinter.
- CLI commands for encryption and decryption.
- AES/Fernet-based message encryption functions.
- Example images and a test directory.

## Technology

- Python
- Pillow (`PIL`) for image handling
- NumPy for pixel-array processing
- CustomTkinter for the GUI
- `cryptography` / Fernet for the AES-labelled encryption mode

## Project structure

```text
Image Steganography/
├── cli/
│   └── cli.py
├── examples/
│   └── flower.png
├── gui/
│   └── app.py
├── hided_imgs/             # generated output images; normally do not commit new outputs
├── steganography/
│   ├── core.py
│   └── encryption.py
└── tests/
    └── testcore.py
```

## Requirements

- Python 3.10 or later is recommended.
- `pip`
- A desktop environment for the GUI.

## Installation

Open a terminal in the repository root (the folder containing `cli`, `gui`, `steganography`, and `tests`).

### Windows PowerShell

```powershell
py -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
pip install pillow numpy customtkinter cryptography
```

If PowerShell blocks activation, you can use the environment's Python directly:

```powershell
.\.venv\Scripts\python.exe -m pip install pillow numpy customtkinter cryptography
```

## Run the GUI

From the repository root:

```powershell
python gui/app.py
```

## Run the CLI

From the repository root:

```powershell
python cli/cli.py --help
```

Encrypt a message (the output path is where the CLI writes the generated PNG):

```powershell
python cli/cli.py encrypt examples/flower.png output.png "Hello from steganography" "change-this-key" --method aes
```

Decrypt a generated image:

```powershell
python cli/cli.py decrypt hided_imgs/flower_encrypted.png "change-this-key" --method aes
```

The core function currently saves GUI/core-generated files in `hided_imgs/`. The CLI also saves the returned image at the output path you provide. Confirm the actual output path after running the command.

## Run tests

```powershell
python -m unittest discover -s tests -v
```

**Current note:** The checked-in test file imports `xor_encrypt` and `xor_decrypt` from `steganography.core`, but those functions are not present in the current `core.py` version. The test suite may fail until this mismatch is fixed. See the open issues / roadmap.

## How it works

1. The message is converted into a binary representation.
2. A terminator (`$$END$$`) is appended to mark the end of the message.
3. The bits are written into the least-significant bits of the image pixel values.
4. During extraction, pixel LSBs are read and converted back into text.
5. In the AES-labelled mode, the message is processed by the Fernet encryption helpers before being embedded.

**Security note:** LSB steganography is not a substitute for secure file transfer. The current `xor` mode in `core.py` appends the terminator but does not apply the XOR operation shown in the tests. Do not use that mode to protect sensitive messages until it is corrected and reviewed. Also, the current password-to-key derivation is a direct SHA-256 hash; consider a password KDF such as Scrypt or Argon2 for a security-focused implementation.

## Contributing

Contributions are welcome. Please read [CONTRIBUTING.md](CONTRIBUTING.md), check the issues, and open a pull request for review.

## Roadmap

See [ROADMAP.md](ROADMAP.md).

## License

No license has been selected in this documentation pack. Choose a license only after confirming that you have the rights to publish all project code and assets. Without a license, others generally do not receive broad permission to reuse, modify, or redistribute your code.
