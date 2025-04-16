import allure
from typing import List
from requests import Response
from clients.http.clients import APIClient
from utils.routes import PoetryAPIRoutes
from models.author_models import AuthorQueryParams
from models.query_enums import SearchTerm, SearchType, OutputField, ResponseFormat


class AuthorClient(APIClient):
    @allure.step('Getting all authors')
    def get_all_authors(self):
        return self.client.get(url=PoetryAPIRoutes.AUTHOR)

    def get_author(self, author_name: str) -> Response:
        with allure.step(f'Getting information about author with the name {author_name}'):
            return self.client.get(url=f'{PoetryAPIRoutes.AUTHOR}/{author_name}')

    def get_author_by_abs_name(self, author_name: str,
                               format_type: str = None) -> Response:
        with allure.step(f"Searching author name with full value of the name {author_name}"):
            params = AuthorQueryParams(
                search_terms=[SearchTerm.author],
                search_type=SearchType.abs
            )
            if format_type:
                params.format = ResponseFormat(format_type)
            return self.client.get(url=f'{PoetryAPIRoutes.AUTHOR}/{author_name}{params.to_url_path()}')

    def get_author_with_output_fields(self, author_name: str,
                                      output_fields: List[str],
                                      format_type: str = None) -> Response:
        with allure.step(f"Searching author with the name {author_name} and corresponding output_fields:"
                         f"{', '.join(output_fields)}"):
            output_fields_types = [OutputField(field) for field in output_fields]
            params = AuthorQueryParams(
                output_fields=output_fields_types
            )
            if format_type:
                params.format = ResponseFormat(format_type)
            return self.client.get(url=f'{PoetryAPIRoutes.AUTHOR}/{author_name}{params.to_url_path()}')
