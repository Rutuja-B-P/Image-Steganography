# Image Steganography

A Python project that explores image steganography: hiding information inside images and extracting it when needed.

## Features

- Hide and extract messages using image-based steganography.
- Command-line interface (CLI).
- Graphical user interface (GUI).
- Support for XOR and AES-labelled encryption methods.
- Example image and test files.

> **Note:** Encryption and steganography are different. Hiding a message does not by itself make the message secure. Review and test the encryption implementation before relying on it for sensitive data.

## Project Structure

```text
Image-Steganography/
├── cli/
│   └── cli.py
├── examples/
├── gui/
│   └── app.py
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
├── requirements.txt
├── README.md
└── ROADMAP.md
```

## Requirements

- Python 3
- Pillow for image processing
- NumPy for image pixel manipulation
- cryptography for encryption
- CustomTkinter for the graphical interface

The `requirements.txt` file contains the external Python packages used by the project.

## Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/kasturihagawane/Image-Steganography.git
cd Image-Steganography
```

If you are contributing to the project, clone your own fork instead.

### 2. Create a virtual environment

```bash
python -m venv .venv
```

**Windows PowerShell:**

```powershell
.\.venv\Scripts\Activate.ps1
```

**macOS/Linux:**

```bash
source .venv/bin/activate
```

### 3. Install dependencies

```bash
python -m pip install -r requirements.txt
```

## Running the CLI

Run CLI commands from the project's root directory.

### Hide a message using XOR

```bash
python cli/cli.py encrypt input.png output.png "Hello World" mysecretkey
```

### Hide a message using the AES option

```bash
python cli/cli.py encrypt input.png output.png "Hello World" mysecretkey --method aes
```

### Extract a message using XOR

```bash
python cli/cli.py decrypt output.png mysecretkey
```

### Extract a message using the AES option

```bash
python cli/cli.py decrypt output.png mysecretkey --method aes
```

Replace the example image paths and key with your own values. Use the same key and encryption method when extracting the message.

The encrypted image is saved to the output path specified in the CLI command, in PNG format.

To view the available CLI commands, run:

```bash
python cli/cli.py --help
```

## Running the GUI

The project includes a graphical interface built using CustomTkinter.

Launch it from the project's root directory:

```bash
python gui/app.py
```

### Hide a message

1. Click **Browse Image** and select an image.
2. Enter the message you want to hide.
3. Enter an encryption key.
4. Select AES or XOR.
5. Click **Encrypt & Save Image**.
6. Check the status message for the output location.

### Extract a message

1. Click **Browse Image** and select the image containing the hidden message.
2. Enter the encryption key.
3. Select the same encryption method used during encryption.
4. Click **Decrypt Message**.
5. Read the extracted message displayed in the application.

## Running Tests

The project contains a `tests/` directory. Inspect the test files and their imports to confirm the correct test runner and command.

The following command can be used if the tests are compatible with Python's built-in `unittest` discovery:

```bash
python -m unittest discover -s tests -v
```

Run the tests and check the results before submitting changes.

## Troubleshooting

### Python is not recognized

Make sure Python is installed and available in your system's PATH. On Windows, you can also try:

```bash
py --version
```

### Module not found

Activate the project's virtual environment and install the dependencies:

```bash
python -m pip install -r requirements.txt
```

### Image file not found

Check that the image path is correct and that the file exists. Use a supported image file and provide the correct path.

### Encryption fails

Check that the input image is valid, the required arguments are provided, and the output directory can be accessed.

### Decryption fails

Check that you selected the correct encrypted image and used the same key and encryption method as during encryption.

### GUI does not open

Make sure the dependencies are installed and run the GUI command from the project root. Check the terminal output for details about the error.

## Contributing

Contributions are welcome! Read [CONTRIBUTING.md](CONTRIBUTING.md), check the repository's issues, and open a pull request with your changes.

Before submitting, verify that installation instructions and usage examples match the current source code.

## Roadmap

See [ROADMAP.md](ROADMAP.md) for planned improvements and future work.
AP.md](ROADMAP.md) for planned improvements.

## License

This project is distributed under the MIT License. See [LICENSE](LICENSE) for details.
