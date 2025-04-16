import pytest
from clients.http.clients import HTTPClient
from clients.api.author_client import AuthorClient
from settings import settings, Settings
from utils.helpers import find_file


@pytest.fixture(scope="session", autouse=True)
def base_config() -> Settings:
    return settings


def pytest_configure(config) -> None:
    config.option.allure_report_dir = settings.allure_dir


@pytest.fixture(scope='class')
def authors_api_client() -> AuthorClient:
    """
    Create API Client
    :return:
    """
    base_url = settings.api_url
    http_client = HTTPClient(base_url=base_url)
    return AuthorClient(client=http_client)


@pytest.fixture
def get_schema():
    def _find_schema_file(schema_name: str) -> str:
        schema_name = schema_name + '.json'
        schema_root_dir = settings.schemas_dir
        full_path = find_file(schema_root_dir, schema_name)
        return full_path

    return _find_schema_file
