# Low-Code Automation: Python + Playwright

This repository contains homework assignments for the Low-Code Automation course.

## Project Structure

- `tests/`
  - `test_contacts_app.py` – Module 2: API Automation with Playwright
  - Other Python test scripts – Module 1: Low-Code Automation with Python + Playwright
- `.gitignore` – ignores temporary and sensitive files
- `README.md` – project overview

This repository contains homework assignments for the Low-Code Automation course. It demonstrates automated testing using Python and Playwright, including both UI and API automation.

---

## Project Structure

low-code-automation/
├── tests/
│ ├── test_contacts_app.py # Module 2: API automation with Playwright
│ ├── test_module1_ui.py # Module 1: Low-Code UI automation with Python + Playwright
├── .gitignore # Excludes temporary and sensitive files
├── README.md # Project overview
├── requirements.txt # Python dependencies

---

## Requirements

- Python 3.13+
- Playwright
- pytest

Install dependencies using:

```bash
pip install -r requirements.txt
playwright install
```

## How to Run Tests
1. Open terminal in the project root.
2. Run all tests:
```bash
pytest tests/
```
3. Run a specific test file:
```bash
pytest tests/test_contacts_app.py
```

## Homework Overview
## Module 1: Low-Code Automation

Automated UI tests for a demo contact list application.

Tests include filling forms, adding and verifying contacts.

## Module 2: API Automation

Automated API tests using Playwright’s APIRequestContext.

Login via API, retrieve auth token from browser context cookies.

Intercept and modify requests to add additional fields (e.g., country).

Update contacts using PATCH requests and verify changes.

Clean up server state after tests.

## Module 3: Version Control

Git workflow including branching, pull requests, and merge conflict resolution.

Repository structured with proper .gitignore to exclude temporary and sensitive files.

## Notes

All test scripts are located in the tests/ folder.

Auth tokens and sensitive information are never committed.

The project demonstrates integration of low-code automation with proper version control practices.
