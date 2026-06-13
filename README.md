# To-Do CLI

A simple command-line interface application for managing to-do lists built with Python.

## Features

- Add multiple to-do items at once
- Track task details including:
  - Category
  - Task description
  - Completion status (Done/Not Done)
  - Creation date
  - Completion date
- View tasks in formatted table output
- Date validation for proper YYYY-MM-DD format

## Requirements

- Python 3.x
- tabulate library

## Installation

1. Clone or download this repository
2. Install the required dependency:
   ```bash
   pip install tabulate
   ```

## Usage

1. Run the application:
   ```bash
   python Main.py
   ```

2. Follow the prompts:
   - Enter how many to-do items you want to add
   - For each item, provide:
     - Category (e.g., Work, Personal, Shopping)
     - Task description
     - Completion status (True for Done, False for Not Done)
     - Creation date (YYYY-MM-DD format)
     - Completion date (YYYY-MM-DD format, if applicable)

3. The application will display your to-do list in two formats:
   - A grid-formatted table using the tabulate library
   - A manually formatted table with custom alignment

## Example

```
How many to-do items do you want to add? 2

Category: Work
Task: Complete project proposal
Done (True/False): True
CreatedAT (YYYY-MM-DD): 2026-06-01
CompletedAt (YYYY-MM-DD): 2026-06-10

Category: Personal
Task: Buy groceries
Done (True/False): False
CreatedAT (YYYY-MM-DD): 2026-06-13
CompletedAt (YYYY-MM-DD): 

=== Output Tables ===
```

## Files

- `Main.py` - Main application entry point
- `Function.py` - Contains helper functions for displaying the to-do list
- `ToDoCLI/` - Python virtual environment (for development)

## How It Works

1. The application collects user input for multiple to-do items
2. Each item is stored as a list containing: [Category, Task, Done status, Creation date, Completion date]
3. The data is passed to two display functions:
   - `todo()` - Uses tabulate library for grid formatting
   - `todo_manual()` - Custom formatting function for aligned table display
4. Both formats are printed to the console for easy viewing

## Notes

- Dates must be entered in YYYY-MM-DD format
- The application performs basic date validation
- Completion date can be left blank for incomplete tasks
- The Done field accepts "True" or "False" and converts to "Done" or "Not Done" for display

## License

This project is open source and available for personal and educational use.

