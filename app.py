from flask import Flask

from routes.transaction import transactions_bp
from routes.report import report_bp

app = Flask(__name__)

# register blueprints
app.register_blueprint(transactions_bp)
app.register_blueprint(report_bp)

@app.route("/")
def home():
    return "Server is running!"

if __name__ == "__main__":
    app.run(debug=True)