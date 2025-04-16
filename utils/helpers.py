import os
import allure
import json
from pathlib import Path
from requests import Response
from settings import settings


def attach_request_and_response(response: Response):
    req = response.request

    with allure.step(f"Request details"):
        allure.attach(
            f"{req.method} {req.url}\n\nHeaders:\n{req.headers}\n\nBody:\n{req.body}",
            name="Request",
            attachment_type=allure.attachment_type.TEXT
        )

    with allure.step(f"Response details"):
        try:
            body = json.dumps(response.json(), indent=2, ensure_ascii=False)
            attachment_type = allure.attachment_type.JSON
        except Exception:
            body = response.text
            attachment_type = allure.attachment_type.TEXT

        allure.attach(
            f"Status: {response.status_code}\n\nHeaders:\n{response.headers}\n\nBody:\n{body}",
            name="Response",
            attachment_type=attachment_type
        )


def find_file(root_path: str, name: str) -> str:
    for root, dirs, files in os.walk(root_path):
        if name in files:
            return os.path.join(root, name)


def load_cases(filename: str, folder: str = settings.test_data_dir) -> list[dict]:
    path = Path(folder) / filename
    with path.open(encoding="utf-8") as f:
        return json.load(f)
