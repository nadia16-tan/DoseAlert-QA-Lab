import requests


def test_homepage():
    response = requests.get(
        "https://medication-reminder-service.onrender.com"
    )

    assert response.status_code == 200