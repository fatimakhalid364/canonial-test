import csv
import io


def validate_row(row, index):
    """
    Validates a single CSV row.
    Returns (is_valid, error_message)
    """

    if len(row) < 4:
        return False, f"Row {index + 1}: invalid column count"

    date, type_, amount, memo = row

    # Validate type
    if type_.strip() not in ["Income", "Expense"]:
        return False, f"Row {index + 1}: invalid type '{type_}'"

    # Validate amount
    try:
        float(amount)
    except:
        return False, f"Row {index + 1}: invalid amount"

    return True, None


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