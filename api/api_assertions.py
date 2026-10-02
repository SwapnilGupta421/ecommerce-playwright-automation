def assert_status_code(response, expected_status_code):
    assert response.status_code == expected_status_code, (
        f"Expected status code {expected_status_code}, "
        f"but got {response.status_code}"
    )

def assert_field_exists(data, field):
    assert field in data, (
        f"Expected field '{field}' to exist in response"
    )

def assert_field_value(data, field, expected_value):
    assert data.get(field) == expected_value, (
        f"Expected '{field}' to be '{expected_value}', "
        f"but got '{data.get(field)}'"
    )

def assert_header_exists(response, header_name):
    assert header_name in response.headers, (
        f"Expected header '{header_name}' to exist in response"
    )

def validate_response(response, expected_status_code):
    assert_status_code(response, expected_status_code)
    assert_header_exists(response, "Content-Type")