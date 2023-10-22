import pytest
from fastapi.testclient import TestClient
from src.homework_app.main import app


@pytest.fixture()
def client():
    client = TestClient(app)
    return client


def test_hello(client):
    response = client.get("/hello")
    assert response.status_code == 200
    content_type = response.headers.get("Content-Type", "")
    assert content_type == "text/plain; charset=utf-8"
    assert response.text == "HSE One Love!"


def test_set(client):
    response_good = client.post(
        "/set",
        headers={"Content-Type": "application/json"},
        json={"key": "my_key", "value": "my_value", "another_key": "blabla"},
    )
    assert response_good.status_code == 200
    assert len(response_good.text) == 0

    response_wrong_json = client.post(
        "/set",
        headers={"Content-Type": "application/json"},
        json={"key": "my_key", "not_a_value": "my_value"},
    )
    assert response_wrong_json.status_code == 415
    assert len(response_good.text) == 0

    response_wrong_content_type = client.post(
        "/set",
        headers={"Content-Type": "text/plain"},
        json={"key": "my_key", "value": "my_value", "another_key": "blabla"},
    )
    assert response_wrong_content_type.status_code == 415
    assert len(response_good.text) == 0


@pytest.fixture(
    params=[
        ({"key": "key1", "value": "value1"}, {"key": "key2", "value": "value2"}),
    ]
)
def set_values(client, request):
    client.post(
        "/set",
        headers={"Content-Type": "application/json"},
        json={
            "key": request.param[0]["key"],
            "value": request.param[0]["value"],
            "another_key": "blabla",
        },
    )
    client.post(
        "/set",
        headers={"Content-Type": "application/json"},
        json={
            "key": request.param[1]["key"],
            "value": request.param[1]["value"],
            "another_key": "blabla",
        },
    )
    return request.param


def test_get(client, set_values):
    for i in range(len(set_values)):
        response = client.get(
            f'/get/{set_values[i]["key"]}',
        )
        assert response.status_code == 200
        assert response.json() == set_values[i]

    response_not_found = client.get(
        "/get/iamwrongkey/",
    )
    assert response_not_found.status_code == 404


@pytest.mark.parametrize("dividend", [10, 105, 93, 0])
@pytest.mark.parametrize("divider", [10, 5, 7, 2])
def test_divide_good(client, dividend, divider):
    response = client.post(
        "/divide",
        headers={"Content-Type": "application/json"},
        json={"dividend": dividend, "divider": divider},
    )
    assert response.status_code == 200
    content_type = response.headers.get("Content-Type", "")
    assert content_type == "text/plain; charset=utf-8"
    assert response.text == str(dividend / divider)


@pytest.mark.parametrize("dividend", [0])
@pytest.mark.parametrize("divider", [0])
def test_divide_bad(client, dividend, divider):
    response_divider_zero = client.post(
        "/divide",
        headers={"Content-Type": "application/json"},
        json={"dividend": dividend, "divider": divider},
    )
    assert response_divider_zero.status_code == 400

    response_bad_json = client.post(
        "/divide",
        headers={"Content-Type": "application/json"},
        json={"dividenv": dividend, "divider": divider},
    )
    assert response_bad_json.status_code == 415
