# Python Automation Scripts

This repository contains a collection of Python scripts designed to automate various tasks. Each script uses the `pywinauto` and `pyautogui` libraries to interact with GUI applications on Windows. Below is a brief overview of each script.

## Scripts

### 1. Calculator Automation (`example1.py`)
This script automates basic interactions with the Windows Calculator application. It demonstrates how to open the calculator, perform button clicks, and fetch results from the display.

### 2. Window Title Fetcher (`example2.py`)
Using `pyautogui`, this script lists the titles of all open windows on the system. It's useful for understanding which applications are currently running and their window titles.

### 3. Notepad++ Automation (`example3.py`)
`example3.py` automates opening and typing text into Notepad++. It shows how to start Notepad++, wait for it to be ready, and then programmatically enter text into the editor.

### 4. Zoom Meeting Joiner (`example4.py`)
This script is designed to automate the process of joining a meeting in Zoom. It opens the Zoom application, navigates to the 'Join Meeting' window, and inputs a predefined meeting ID and participant name.

## Installation

To run these scripts, you'll need Python installed on your system along with the `pywinauto` and `pyautogui` libraries. You can install these libraries using pip:

```bash
pip install pywinauto pyautogui
```

## Usage

To use any of the scripts, simply run them with Python. For example:

```bash
python example1.py
```

Replace `example1.py` with the name of the script you wish to run.

## Contributing

Contributions to this project are welcome. Please feel free to fork the repository, make changes, and submit a pull request.

