import io
import pytest
from app import app
from storage.memory import transactions

client = app.test_client()


@pytest.fixture(autouse=True)
def clear_transactions():
    transactions.clear()   
    yield
    transactions.clear()   


def test_home():
    response = client.get("/")

    assert response.status_code == 200
    assert b"Server is running" in response.data



def test_upload_transactions():
    with open("sample-data/data.csv", "rb") as f:
        data = {
            "data": (io.BytesIO(f.read()), "data.csv")
        }

    response = client.post(
        "/transactions",
        data=data,
        content_type="multipart/form-data"
    )

    assert response.status_code == 200
    json_data = response.get_json()

    assert "added" in json_data
    assert json_data["added"] == 10



def test_report():
    with open("sample-data/data.csv", "rb") as f:
        data = {
            "data": (io.BytesIO(f.read()), "data.csv")
        }

    client.post(
        "/transactions",
        data=data,
        content_type="multipart/form-data"
    )

    response = client.get("/report")

    assert response.status_code == 200

    data = response.get_json()

    assert "gross-revenue" in data
    assert "expenses" in data
    assert "net-revenue" in data

    assert data["gross-revenue"] == 225.00
    assert data["expenses"] == 72.93
    assert data["net-revenue"] == 152.07