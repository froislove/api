import pytest
import allure
from utils.helpers import load_cases
from clients.api.author_client import AuthorClient
from models.author_models import Author
from validations.validate_schema import validate_schema
from validations.assertions import assert_status_code, assert_response_field


@allure.epic('API validation testing')
@pytest.mark.validation
class TestValidationAuthors:

    @allure.title("Validate schema of /author response")
    def test_get_all_author(self, authors_api_client, get_schema):
        client: AuthorClient = authors_api_client
        response = client.get_all_authors()
        assert_status_code(response)

        validate_schema(response_json=response.json(), schema_path=get_schema("Authors"))

    @allure.title("Validate schema of /author/<author> response")
    def test_get_author(self, authors_api_client, get_schema):
        client: AuthorClient = authors_api_client
        response = client.get_author(author_name='Algernon Charles Swinburne')

        assert_status_code(response)
        schema_path = get_schema("Author")

        for element in response.json():
            validate_schema(response_json=element, schema_path=schema_path)

    @allure.title("Validate schema of /author/<author>/author response")
    def test_get_author_all_output_fields(self, authors_api_client, get_schema):
        client: AuthorClient = authors_api_client
        response = client.get_author_with_output_fields(
            author_name='Algernon Charles Swinburne',
            output_fields=['all'])

        assert_status_code(response)
        schema_path = get_schema("AuthorAllFieldsPresence")
        for element in response.json():
            validate_schema(response_json=element, schema_path=schema_path)


@allure.epic('API functional testing')
class TestAuthors:
    @allure.title("Non existent author")
    def test_non_existent_author(self, authors_api_client):
        client: AuthorClient = authors_api_client

        response = client.get_author(author_name='Invalid')

        assert_status_code(response, 200)
        assert_response_field(response_json=response.json(),
                              field='status',
                              expected=404)
        assert_response_field(response_json=response.json(),
                              field='reason',
                              expected='Not found')

    @allure.title("Proper amount of lines is present")
    @pytest.mark.parametrize("case", load_cases("authors_lines.json"))
    # actual results can be retrieved from db
    def test_line_counts(self, authors_api_client, case):
        client: AuthorClient = authors_api_client

        response = client.get_author_with_output_fields(author_name=case.get('author'),
                                                        output_fields=['linecount'])

        assert_status_code(response, 200)
        for element in response.json():
            result = Author.model_validate(element)
            with allure.step(f"Assert count of lines is equal {case.get('expected_count')}"):
                assert int(result.linecount) == case.get('expected_count')
