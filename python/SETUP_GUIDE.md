# Setup Guide for Beginners - user_application_20260213_093948 (Python)

This guide will help you run this project even if you're new to programming.

## Step 1: Install Python

### Windows
1. Go to https://www.python.org/downloads/
2. Download Python 3.11 or later
3. Run the installer
4. **IMPORTANT**: Check "Add Python to PATH" during installation
5. Click "Install Now"

### Mac
```bash
# Using Homebrew (recommended)
brew install python@3.11
```

### Linux (Ubuntu/Debian)
```bash
sudo apt update
sudo apt install python3.11 python3.11-venv python3-pip
```

## Step 2: Download the Code

### Option A: Using Git
```bash
git clone <repository-url>
cd user_application_20260213_093948/python
```

### Option B: Download ZIP
1. Go to the GitHub repository
2. Click "Code" -> "Download ZIP"
3. Extract the ZIP file
4. Open terminal/command prompt in the extracted folder

## Step 3: Set Up Virtual Environment

A virtual environment keeps your project's dependencies separate.

```bash
# Create virtual environment
python -m venv venv

# Activate it
# On Windows:
venv\Scripts\activate

# On Mac/Linux:
source venv/bin/activate
```

You should see `(venv)` in your terminal prompt.

## Step 4: Install Dependencies

```bash
pip install -r requirements.txt
```

Wait for all packages to install (this may take a few minutes).

## Step 5: Run the Application

```bash
python main.py
```

You should see:
```
INFO:     Uvicorn running on http://0.0.0.0:8000
INFO:     Started reloader process
```

## Step 6: Test the API

1. Open your browser
2. Go to http://localhost:8000/docs
3. You'll see the Swagger UI with all API endpoints
4. Click on any endpoint and "Try it out" to test

## Common Issues

### "python not found"
- Make sure Python is installed and added to PATH
- Try using `python3` instead of `python`

### "pip not found"
- Try using `python -m pip` instead of `pip`

### Port already in use
- Change the port: `uvicorn main:app --port 8001`

### Permission denied
- On Mac/Linux, you may need `sudo` for some commands

## Getting Help

- Check the README.md for more details
- Open an issue on GitHub
- Stack Overflow: search for "FastAPI" + your error message
