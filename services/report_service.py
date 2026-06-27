def generate_report(transactions):

    """
    Calculates financial summary from a list of transactions.

    Rules:
    - Income is treated as gross revenue
    - Expense is treated as total expenses
    - Net revenue = gross - expenses

    Returns:
        dict: A summary containing gross-revenue, expenses, and net-revenue
    """
    gross = 0
    expenses = 0

    for t in transactions:
        if t["type"].lower() == "income":
            gross += t["amount"]
        else:
            expenses += t["amount"]

    return {
        "gross-revenue": round(gross, 2),
        "expenses": round(expenses, 2),
        "net-revenue": round(gross - expenses, 2)
    }