import allure
from typing import Any
from requests import Response


def assert_status_code(response: Response, expected: int = 200) -> None:
    with allure.step(f"Assert response status code is {expected}"):
        actual = response.status_code
        if actual != expected:
            allure.attach(
                response.text,
                name="Response body",
                attachment_type=allure.attachment_type.TEXT
            )
            raise AssertionError(f"Expected status code {expected}, got {actual}")


def assert_response_field(response_json: dict, field: str, expected: Any) -> None:
    with allure.step(f"Assert response field {field} is {expected}"):
        actual = response_json.get(field, None)
        if response_json.get(field) != expected:
            allure.attach(
                response_json,
                name="Response body",
                attachment_type=allure.attachment_type.JSON
            )
            raise AssertionError(f"Expected {expected}, got {actual}")
