def assert_status_code(response, expected_status_code):
    assert response.status_code == expected_status_code, (
        f"Expected status code {expected_status_code}, "
        f"but got {response.status_code}"
    )

def assert_field_exists(data, field):
    assert field in data, (
        f"Expected field '{field}' to exist in response"
    )