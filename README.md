# Low-Code Automation: Python + Playwright

This repository contains homework assignments for the Low-Code Automation course.  
It demonstrates automated testing using Python and Playwright, including both UI and API automation.

## Project Structure

low_code_automation/
├── tests/                      # All test files
│   ├── contact_data.json       # Sample data for API tests
│   ├── test_contacts_app.py    # Module 2: API automation
│   ├── test_input_validation.py # Module 1: Input validation tests
│   └── test_search_product.py  # Module 1: Search tests
├── .gitignore                  # Ignore cache, venv, etc.
├── Pipfile                     # Dependency management
├── pytest.ini                  # Pytest config
└── README.md                   # Documentation


## Requirements

- Python 3.13+
- [Playwright](https://playwright.dev/python/)
- pytest

Dependencies are managed using `pipenv`. To set up the environment:

```bash
pip install pipenv
pipenv install
pipenv run playwright install


## Running Tests

Run all tests:
pipenv run pytest

Run a specific test:
pipenv run pytest test_contacts_app.py::test_api_examples


## Notes

This project uses Pipfile / Pipfile.lock for dependency management instead of requirements.txt.