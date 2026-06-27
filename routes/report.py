from flask import Blueprint, jsonify
from storage.memory import transactions
from services.report_service import generate_report

report_bp = Blueprint("report", __name__)

@report_bp.route("/report", methods=["GET"])
def get_report():

    """
    Generates and returns a financial summary based on the
    transactions currently stored in memory.
    """
    result = generate_report(transactions)
    return jsonify(result), 200