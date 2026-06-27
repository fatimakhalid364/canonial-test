from flask import Blueprint, request, jsonify
from storage.memory import transactions
from services.csv_service import parse_csv

transactions_bp = Blueprint("transactions", __name__)

@transactions_bp.route("/transactions", methods=["POST"])
def upload_transactions():

    """
    Accepts a CSV file upload, checks for empty or invalid utf-8 files, validates each row, stores valid
    transactions in memory, and returns a summary of the upload.
    """


    if "data" not in request.files:
        return jsonify({
            "message": "No file provided"
        }), 400

    file = request.files["data"]

    if file.filename == "":
        return jsonify({
            "message": "Empty file uploaded"
        }), 400

    try:
        content = file.read().decode("utf-8", errors="strict")
    except UnicodeDecodeError:
        return jsonify({
            "message": "Invalid file encoding. Please upload a UTF-8 encoded CSV."
        }), 400

    new_transactions, errors = parse_csv(content)

    transactions.extend(new_transactions)

    return jsonify({
        "message": "upload processed",
        "added": len(new_transactions),
        "errors": errors
    }), 200