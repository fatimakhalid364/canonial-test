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
├── routes/
│   ├── transactions.py
│   └── report.py
│
├── services/
│   ├── csv_service.py
│   └── report_service.py
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

## 1. Clone the repository

```bash
git clone <repository-url>
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

```bash
curl.exe -X POST http://127.0.0.1:5000/transactions -F "data=@sample-data/data.csv"
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

Example:

```
2020-07-01,Expense,18.77,Fuel
2020-07-04,Income,40.00,347 Woodrow
2020-07-06,Income,35.00,219 Pleasant
```

---

# Validation

Each row is validated before being stored.

Current validation checks include:

- Row contains four columns
- Transaction type must be either:
  - Income
  - Expense
- Amount must be a valid numeric value

Rows that fail validation are skipped and returned as validation errors in the API response.

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

- Uploaded files are valid CSV files encoded in UTF-8.
- Data is stored only while the application is running.
- Multiple uploads append transactions to the existing in-memory collection.
- Validation errors do not prevent valid transactions from being stored.

---

# Shortcomings

Current limitations include:

- No persistent database.
- Uploaded data is lost when the server stops.
- Duplicate transactions are not detected.
- CSV header validation is not implemented.
- Date format is not validated.
- Comment lines and blank lines are currently treated as invalid rows instead of being ignored.
- Authentication and authorization are not implemented.

---

# Future Improvements

With additional development time, the following improvements would be made:

- Store transactions in a relational database such as PostgreSQL.
- Add transaction deduplication.
- Validate dates and CSV headers.
- Ignore blank lines and comment rows during parsing.
- Add logging and centralized error handling.
- Implement request schema validation.
- Improve test coverage with edge cases and integration tests.
- Containerize the application using Docker.
- Add API documentation using Swagger/OpenAPI.
- Support larger CSV uploads through streaming instead of loading the entire file into memory.

---

# Author

Saad Salman Zahid