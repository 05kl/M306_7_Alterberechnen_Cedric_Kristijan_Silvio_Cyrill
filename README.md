# M306_7_Alterberechnen_Cedric_Kristijan_Silvio_Cyrill

## Getting Started

This guide will help you set up and run the project.

### Prerequisites

Ensure you have Python installed on your system. You can download it from the official Python website: [https://www.python.org/downloads/](https://www.python.org/downloads/)

### Setup

Follow these steps to get the project running:

1. **Create a Virtual Environment**
    It's recommended to use a virtual environment to manage project dependencies. Open your terminal or command prompt in the project directory and run:

    ```bash
    python3 -m venv venv
    ```

    This command creates a new directory named `venv` in your project, containing the virtual environment.

2. **Activate the Virtual Environment**
    Before installing dependencies, activate the virtual environment:

    * **On macOS/Linux:**

        ```bash
        source venv/bin/activate
        ```

    * **On Windows (Command Prompt):**

        ```bash
        .\venv\Scripts\activate.bat
        ```

    * **On Windows (PowerShell):**

        ```bash
        .\venv\Scripts\Activate.ps1
        ```

3. **Install Dependencies**
    With the virtual environment activated, install the required packages using `pip`:

    ```bash
    pip install -r requirements.txt
    ```

You are now ready to run the project!

### Usage

To use the `alter.py` script, activate your virtual environment and run the script with a date in `DD.MM.YYYY` format as an argument.

```bash
source venv/bin/activate # On macOS/Linux
# or .\venv\Scripts\activate.bat (Windows Command Prompt)
# or .\venv\Scripts\Activate.ps1 (Windows PowerShell)

python alter.py 01.01.2000
```

The script will then output the age in years, months, and days, as well as the total number of days.
