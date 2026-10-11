# Image Steganography

A Python project that explores image steganography: hiding information inside images and extracting it when needed.

## Features

- Hide and extract messages using image-based steganography.
- Command-line interface (CLI).
- Graphical user interface (GUI).
- Encryption helper functions.
- Example image and test files.

> **Note:** Encryption and steganography are different. Hiding a message does not by itself make the message secure. Review and test the encryption implementation before relying on it for sensitive data.

## Project Structure

```text
Image-Steganography/
├── cli/
├── examples/
├── gui/
├── hided_imgs/
├── steganography/
│   ├── core.py
│   └── encryption.py
├── tests/
├── .github/
│   └── ISSUE_TEMPLATE/
├── .gitignore
├── CONTRIBUTING.md
├── LICENSE
├── PROJECT_STATUS.md
└── ROADMAP.md
```

## Requirements

- Python 3
- Dependencies required by the project, such as Pillow, NumPy, CustomTkinter, and cryptography, depending on which features you use.

Install the dependencies listed in the project's dependency file, if one exists. If there is no dependency file, check the imports in the source files and document the required packages before installation.

## Getting Started

1. Clone the repository:

   ```bash
   git clone https://github.com/kasturihagawane/Image-Steganography.git
   cd Image-Steganography
   ```

2. Create and activate a virtual environment:

   **Windows PowerShell**

   ```powershell
   python -m venv .venv
   .\.venv\Scripts\Activate.ps1
   ```

3. Install the project's required dependencies.

4. Check the CLI and GUI source files for the supported commands and launch instructions.

## Running Tests

Run the test suite with:

```bash
python -m unittest discover -s tests -v
```

If tests fail, check that the test imports and function names match the current implementation.

## Contributing

Contributions are welcome! Read [CONTRIBUTING.md](CONTRIBUTING.md), check the repository's issues, and open a pull request with your changes.

## Roadmap

See [ROADMAP.md](ROADMAP.md) for planned improvements.

## License

This project is distributed under the MIT License. See [LICENSE](LICENSE) for details.
