from api.api_assertions import assert_status_code, assert_field_exists
from api.test_data import CREATE_USER_PAYLOAD, UPDATE_USER_PAYLOAD


def test_get_users(api_client):
    response = api_client.get("/users")

    assert_status_code(response, 200)

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

    assert_status_code(response, 201)

    created_user = response.json()

    assert created_user["name"] == "Swapnil"
    assert created_user["username"] == "swapnil123"
    assert created_user["email"] == "swapnil@example.com"

def test_get_non_existing_user(api_client):
    response = api_client.get("/users/9999")

    assert_status_code(response, 404)

def test_update_user(api_client):

    response = api_client.put("/users/1", UPDATE_USER_PAYLOAD)

    assert_status_code(response, 200)

    updated_user = response.json()

    assert updated_user["name"] == "Swapnil Updated"
    assert updated_user["username"] == "swapnil_updated"
    assert updated_user["email"] == "swapnil.updated@example.com"


def test_delete_user(api_client):
    response = api_client.delete("/users/1")
    assert_status_code(response, 200)