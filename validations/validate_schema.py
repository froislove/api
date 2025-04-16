import os
import json
import allure
import pytest
from jsonschema import validate, ValidationError


@allure.step('Validate json schema of response')
def validate_schema(response_json: dict, schema_path: str):
    """
    Validates JSON response against a given JSON Schema.
    Attaches both the response and the schema to Allure report on failure.

    :param response_json: dict — actual JSON from API response
    :param schema_path: str — path to schema file (relative to project root)
    :raises AssertionError: if validation fails
    """
    full_path = os.path.join(os.getcwd(), schema_path)

    with open(full_path, "r", encoding="utf-8") as f:
        schema = json.load(f)

    try:
        validate(instance=response_json, schema=schema)

    except ValidationError as e:
        with allure.step("Attach response JSON"):
            allure.attach(
                json.dumps(response_json, indent=2),
                name="Response JSON",
                attachment_type=allure.attachment_type.JSON,
            )

        with allure.step("Attach schema used for validation"):
            allure.attach(
                json.dumps(schema, indent=2),
                name=f"Schema ({schema_path})",
                attachment_type=allure.attachment_type.JSON,
            )

        pytest.fail(f"Schema validation failed:\n{e.message}\nAt: {list(e.path)}")
