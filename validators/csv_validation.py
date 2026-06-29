from datetime import datetime

def is_skippable_row(row):
    """
    Returns True if row should be ignored:
    - blank line
    - empty cells only
    - comment line starting with #
    """

    if not row:
        return True

    if all(cell.strip() == "" for cell in row):
        return True

    if row[0].strip().startswith("#"):
        return True

    return False



def validate_row(row, index):
    """
    Validates a single CSV row.
    Returns (is_valid, error_message)
    """

    if len(row) != 4:
        return False, f"Row {index + 1}: invalid column count"

    date, type_, amount, memo = row

    if not date.strip():
        return False, f"Row {index + 1}: missing date"

    if not type_.strip():
        return False, f"Row {index + 1}: missing type"

    if not amount.strip():
        return False, f"Row {index + 1}: missing amount"

    if not memo.strip():
        return False, f"Row {index + 1}: missing memo"
    
    try:
        datetime.strptime(date.strip(), "%Y-%m-%d")
    except ValueError:
        return False, f"Row {index + 1}: invalid date format '{date}'"

    if type_.strip() not in ["Income", "Expense"]:
        return False, f"Row {index + 1}: invalid type '{type_}'"

    try:
        float(amount)
    except:
        return False, f"Row {index + 1}: invalid amount"

    return True, None


