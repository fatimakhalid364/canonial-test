# Summer Break Tax Report API

## Overview

This project is a simple RESTful web service built using **Python** and **Flask**. It allows users to upload a CSV file containing income and expense transactions and generates a financial summary report consisting of:

- Gross Revenue
- Total Expenses
- Net Revenue

The application was developed as an MVP (Minimum Viable Product) with an in-memory data store, following a modular project structure.

---

# Tech Stack

- Python 3
- Flask
- Pytest

---

# Project Structure

```
summer-break/
│
├── app.py
│
├── routes/
│   ├── transaction.py
│   └── report.py
│
├── services/
│   ├── csv_service.py
│   └── report_service.py
│
├── validators/
│   └── csv_validation.py
│
├── storage/
│   └── memory.py
│
├── sample-data/
│   └── data.csv
│
├── tests/
│   └── test_app.py
│
├── requirements.txt
└── README.md
```

---

# Installation

## 1. Extract the project archive

### Windows

Right-click the `.tar.gz` file and select **Extract All...** (or use a tool such as 7-Zip or WinRAR).

### macOS / Linux

Open a terminal and run:

```bash
tar -xzf saad_salman_zahid_summer_break.tar.gz
cd summer-break
```
---

## 2. Create a virtual environment

### Windows

```bash
python -m venv venv
```

Activate it:

```bash
venv\Scripts\activate
```

---

### macOS / Linux

```bash
python3 -m venv venv
```

Activate it:

```bash
source venv/bin/activate
```
---

## 3. Install dependencies

```bash
pip install -r requirements.txt
```

---

# Running the application

Start the Flask server:

```bash
python app.py
```

The server will start at:

```
http://127.0.0.1:5000
```

---

# API Endpoints

## POST /transactions

Uploads a CSV file containing transaction data.

### Request

Content-Type:

```
multipart/form-data
```

Form field:

```
data -> CSV file
```

Example using curl:

#### Windows (Powershell / CMD)

```bash
curl.exe -X POST http://127.0.0.1:5000/transactions -F "data=@sample-data/data.csv"
```

#### macOS / Linux

```bash
curl -X POST http://127.0.0.1:5000/transactions -F "data=@sample-data/data.csv"
```


Example response:

```json
{
    "message": "upload processed",
    "added": 10,
    "errors": []
}
```

---

## GET /report

Returns a financial summary.

Example:

```bash
curl.exe http://127.0.0.1:5000/report
```

Example response:

```json
{
    "gross-revenue": 225.00,
    "expenses": 72.93,
    "net-revenue": 152.07
}
```

---

# CSV Format

The uploaded CSV should follow this format:

```
Date,Type,Amount,Memo
```

Each row represents a single transaction where:

- **Date** → transaction date (string)
- **Type** → either `Income` or `Expense`
- **Amount** → numeric value (decimal allowed)
- **Memo** → description of transaction

---

## Test Dataset (Important)

For evaluation purposes, the application is tested using a predefined dataset located at: `sample-data/data.csv`

This dataset produces deterministic results used in automated tests.

Expected computed results for this dataset:

- Gross Revenue: 225.00  
- Total Expenses: 72.93  
- Net Revenue: 152.07  

These values are asserted in the test suite to validate correctness of report generation.

---

# Validation & Preprocessing

Each row in the uploaded CSV goes through a two-step processing pipeline:

---

## 1. Preprocessing (Noise Removal)

Before validation, rows are filtered to remove non-data entries:

- Blank or empty rows are ignored
- Comment lines starting with `#` are ignored

These rows are not treated as errors and are not included in validation.

---

## 2. Validation

After preprocessing, each remaining row is validated before being stored.

Current validation checks include:

- Row contains exactly four columns
- Transaction type must be either:
  - Income
  - Expense
- Amount must be a valid numeric value

---

## Error Handling

- Rows that fail validation are recorded as errors
- Valid rows are stored in memory
- Preprocessed (comment/blank) rows are ignored silently and not included in error reporting

---

# Running Tests

Run all tests:

```bash
python -m pytest
```

Run a single test:

```bash
python -m pytest tests/test_app.py::test_report
```

---

# Solution Approach

The project follows a layered architecture:

- **Routes**
  - Handle incoming HTTP requests and responses.
- **Services**
  - Contain business logic such as CSV parsing and report generation.
- **Storage**
  - Maintains application state using an in-memory list.
- **Tests**
  - Verify endpoint functionality using Flask's testing client and Pytest.

---

# Assumptions

- The application accepts valid UTF-8 encoded CSV files for processing.
- The system is designed to handle arbitrary CSV uploads in production usage.
- However, the test suite evaluates correctness using a predefined dataset located at `sample-data/data.csv`.
- For this dataset, outputs are deterministic and used for automated assertions (gross revenue, expenses, and net revenue).
- Data is stored only while the application is running (in-memory storage).
- Multiple uploads append transactions to the existing in-memory collection.
- Validation errors do not prevent valid transactions from being stored.

---

# Shortcomings

Current limitations include:

- No persistent database.
- Uploaded data is lost when the server stops.
- CSV header validation is not implemented.
- Authentication and authorization are not implemented.

---

# Future Improvements

With additional development time, the following improvements would be made:

- Store transactions in a relational database such as PostgreSQL.
- Validate CSV headers.
- Add logging and centralized error handling.
- Implement request schema validation.
- Improve test coverage with edge cases and integration tests.
- Containerize the application using Docker.
- Add API documentation using Swagger/OpenAPI.
- Support larger CSV uploads through streaming instead of loading the entire file into memory.

---

# Author

Saad Salman Zahid