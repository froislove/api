import os
from typing import Final
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    api_url: str = 'https://poetrydb.org'

    project_root: Final[str] = os.path.dirname(os.path.abspath(__file__))
    schemas_dir: Final[str] = os.path.join(project_root, 'schemas')
    allure_dir: Final[str] = os.path.join(project_root, 'allure-results')
    test_data_dir: Final[str] = os.path.join(project_root, 'test_data')


settings = Settings()
