from flask import Blueprint, request, jsonify
from storage.memory import transactions
from services.csv_service import parse_csv

transactions_bp = Blueprint("transactions", __name__)

@transactions_bp.route("/transactions", methods=["POST"])
def upload_transactions():

    """
    Accepts a CSV file upload, validates each row, stores valid
    transactions in memory, and returns a summary of the upload.
    """

    if "data" not in request.files:
        return jsonify({"error": "No file provided"}), 400

    file = request.files["data"]
    content = file.read().decode("utf-8")

    new_transactions, errors = parse_csv(content)

    transactions.extend(new_transactions)

    return jsonify({
        "message": "upload processed",
        "added": len(new_transactions),
        "errors": errors
    }), 200