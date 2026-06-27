import io
from app import app
from storage.memory import transactions

client = app.test_client()


# -------------------------
# 1. Test home route
# -------------------------
def test_home():
    response = client.get("/")
    assert response.status_code == 200
    assert b"Server is running" in response.data


# -------------------------
# 2. Test CSV upload
# -------------------------
def test_upload_transactions():
    with open("sample-data/data.csv", "rb") as f:

        data = {
            "data": (io.BytesIO(f.read()), "data.csv")
        }

    response = client.post("/transactions", data=data, content_type="multipart/form-data")

    assert response.status_code == 200
    json_data = response.get_json()

    assert "added" in json_data
    assert json_data["added"] == 10


# -------------------------
# 3. Test report
# -------------------------
def test_report():
    response = client.get("/report")

    assert response.status_code == 200

    data = response.get_json()

    assert "gross-revenue" in data
    assert "expenses" in data
    assert "net-revenue" in data

    assert data["gross-revenue"] == 225.00
    assert data["expenses"] == 72.93
    assert data["net-revenue"] == 152.07


# -------------------------
# 4. Cleanup 
# -------------------------
def teardown_module(module):
    transactions.clear()