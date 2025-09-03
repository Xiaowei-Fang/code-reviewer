# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

This is a VSCode extension that provides Python code review functionality using pylint. The extension adds a button to the editor title bar when a Python file is opened, which triggers a code review process.

## Architecture

The extension consists of two main components:

1. **TypeScript Extension** (`src/extension.ts`):
   - Registers a command that appears as a button in the editor title bar for Python files
   - Reads the content of the active Python file
   - Spawns a Python subprocess to execute the review script
   - Handles communication with the Python script via stdin/stdout
   - Displays results in VSCode's output panel

2. **Python Review Script** (`review_script.py`):
   - Receives Python code via stdin
   - Writes code to a temporary file
   - Runs pylint on the temporary file
   - Returns the pylint report via stdout
   - Handles various encoding issues for international characters

## Key Features

- Unicode/UTF-8 encoding handling for international characters
- Error handling for missing pylint installation
- Temporary file management for pylint analysis
- VSCode output channel integration for displaying results

## Common Development Tasks

### Building/Compiling
```bash
npm run compile
```

### Watch Mode
```bash
npm run watch
```

### Testing the Extension
1. Press F5 to launch the extension in a new VSCode window
2. Open any Python file in the test window
3. Click the "Review Python Code" button in the editor title bar

### Project Structure
- `src/extension.ts` - Main extension code
- `review_script.py` - Python script that performs pylint analysis
- `out/extension.js` - Compiled JavaScript output
- `package.json` - Extension manifest and scripts

## Dependencies
- VSCode Extension API
- Node.js child_process module
- Python 3.x with pylint installed (`pip install pylint`)