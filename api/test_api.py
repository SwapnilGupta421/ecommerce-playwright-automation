import pytest
from api.api_assertions import assert_field_exists, assert_field_value, validate_response
from api.test_data import CREATE_USER_PAYLOAD, UPDATE_USER_PAYLOAD


def test_get_users(api_client):
    response = api_client.get("/users")

    validate_response(response, 200)

    users = response.json()

    assert len(users) > 0
    assert users[0]["id"] == 1
    assert users[0]["name"] == "Leanne Graham"
    assert users[0]["username"] == "Bret"

    first_user = users[0]
    assert_field_exists(first_user, "id")
    assert_field_exists(first_user, "name")
    assert_field_exists(first_user, "username")
    assert_field_exists(first_user, "email")


def test_create_user(api_client):

    response = api_client.post("/users", CREATE_USER_PAYLOAD)

    validate_response(response, 201)

    created_user = response.json()

    assert_field_value(created_user, "name", CREATE_USER_PAYLOAD["name"])
    assert_field_value(created_user, "username", CREATE_USER_PAYLOAD["username"])
    assert_field_value(created_user, "email", CREATE_USER_PAYLOAD["email"])

@pytest.mark.parametrize("user_id", [9999, 10000, 10001])   
def test_get_non_existing_user(api_client,user_id):
    response = api_client.get(f"/users/{user_id}")

    validate_response(response, 404)

def test_update_user(api_client):

    response = api_client.put("/users/1", UPDATE_USER_PAYLOAD)

    validate_response(response, 200)

    updated_user = response.json()

    assert_field_value(updated_user, "name", UPDATE_USER_PAYLOAD["name"])
    assert_field_value(updated_user, "username", UPDATE_USER_PAYLOAD["username"])
    assert_field_value(updated_user, "email", UPDATE_USER_PAYLOAD["email"])


def test_delete_user(api_client):
    response = api_client.delete("/users/1")
    validate_response(response, 200)

def test_get_user_by_id(api_client):
    response = api_client.get("/users/1")

    validate_response(response, 200)

    user = response.json()

    assert_field_value(user, "id", 1)
    assert_field_value(user, "name", "Leanne Graham")
    assert_field_value(user, "username", "Bret")
    assert_field_value(user, "email", "Sincere@april.biz")