import csv
import io
from validators.csv_validation import (
    is_skippable_row,
    validate_row,
)

def parse_csv(file_content: str):
    """
    Parses CSV and returns:
    - valid transactions
    - validation errors
    """

    transactions = []
    errors = []

    csv_reader = csv.reader(io.StringIO(file_content))

    for index, row in enumerate(csv_reader):

        if is_skippable_row(row):
            continue

        is_valid, error = validate_row(row, index)

        if not is_valid:
            errors.append(error)
            continue

        date, type_, amount, memo = row

        transactions.append({
            "date": date.strip(),
            "type": type_.strip(),
            "amount": float(amount),
            "memo": memo.strip()
        })

    return transactions, errors