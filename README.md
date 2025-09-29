# Python Exercises

This repository contains Python programming exercises, including a toy tabular data manipulation library called Phoenixcel.

## Setup

### Prerequisites
- Python 3
- pipenv (install with `pip install pipenv`)

### Installation

1. Install dependencies:
```bash
pipenv install --dev
```

This will install:
- **jupyter** - for running Jupyter notebooks
- **pytest** - for running tests

2. Activate the virtual environment:
```bash
pipenv shell
```

## Running Tests

Run all tests:
```bash
pipenv run pytest
```

Run tests with verbose output:
```bash
pipenv run pytest -v
```

Run specific test file:
```bash
pipenv run pytest data_frame_exercise/phoenixcel/tests/test_dataframe.py
```

## Running Jupyter Notebooks

Start Jupyter:
```bash
pipenv run jupyter notebook
```

Or, if you've activated the virtual environment with `pipenv shell`:
```bash
jupyter notebook
```

The notebook server will open in your browser. Navigate to the different directories to access the exercise notebooks for the different exercises.

