# Simple Basic Authentication API

This project is a simple API that demonstrates Basic Authentication using Python and Flask. The API includes one model: User, and stores user data via serialization/deserialization in files.

## Learning Objectives

- Understand what authentication means
- Learn about Base64 encoding
- Implement Basic authentication on a simple API
- Understand how to send the Authorization header

## Requirements

### Python Scripts

- All files are compatible with Python 3.7
- All files end with a new line
- The first line of all files is `#!/usr/bin/env python3`
- Code follows the `pycodestyle` style (version 2.5)
- All files are executable
- Documentation is included for all modules, classes, and functions
- Documentation is not just a word but a real sentence explaining the purpose of the module, class, or method

## Setup and Installation

1. **Download the Project**
    ```bash
    wget [URL_TO_ARCHIVE]
    unzip archive.zip
    cd 0x01-Basic_authentication
    ```

2. **Install Required Packages**
    ```bash
    pip3 install -r requirements.txt
    ```

3. **Start the API Server**
    ```bash
    API_HOST=0.0.0.0 API_PORT=5000 python3 -m api.v1.app
    ```

## Usage

After starting the API server, you can test the `/api/v1/status` endpoint using `curl`:

```bash
curl "http://0.0.0.0:5000/api/v1/status" -vvv
