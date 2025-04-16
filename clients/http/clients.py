import typing
import allure
import requests
from requests import Response
from requests.auth import AuthBase
from requests.cookies import RequestsCookieJar
from utils.helpers import attach_request_and_response


class HTTPClient(requests.Session):
    """
    Requests-based HTTP client with Allure-integrated steps.
    """

    def __init__(self, base_url: str):
        super().__init__()
        self._base_url = base_url

    @allure.step('Performing GET request to "{url}"')
    def get(
            self,
            url: str,
            params: typing.Optional[dict] = None,
            headers: typing.Optional[dict] = None,
            cookies: typing.Optional[typing.Union[dict, RequestsCookieJar]] = None,
            auth: typing.Optional[typing.Union[typing.Tuple[str, str], AuthBase]] = None,
            timeout: typing.Optional[typing.Union[float, typing.Tuple[float, float]]] = None,
            allow_redirects: bool = True,
            **kwargs
    ) -> Response:
        response = super().get(
            url=self._base_url + url,
            params=params,
            headers=headers,
            cookies=cookies,
            auth=auth,
            timeout=timeout,
            allow_redirects=allow_redirects,
            **kwargs
        )
        attach_request_and_response(response)
        return response

    @allure.step('Performing POST request to "{url}"')
    def post(
            self,
            url: str,
            *,
            data: typing.Optional[typing.Union[dict, str]] = None,
            json: typing.Optional[typing.Any] = None,
            files: typing.Optional[typing.Dict[str, typing.Any]] = None,
            params: typing.Optional[dict] = None,
            headers: typing.Optional[dict] = None,
            cookies: typing.Optional[typing.Union[dict, RequestsCookieJar]] = None,
            auth: typing.Optional[typing.Union[typing.Tuple[str, str], AuthBase]] = None,
            timeout: typing.Optional[typing.Union[float, typing.Tuple[float, float]]] = None,
            allow_redirects: bool = True,
            **kwargs
    ) -> Response:
        response = super().post(
            url=self._base_url + url,
            data=data,
            json=json,
            files=files,
            params=params,
            headers=headers,
            cookies=cookies,
            auth=auth,
            timeout=timeout,
            allow_redirects=allow_redirects,
            **kwargs
        )
        attach_request_and_response(response)
        return response

    @allure.step('Performing PATCH request to "{url}"')
    def patch(
            self,
            url: str,
            *,
            data: typing.Optional[typing.Union[dict, str]] = None,
            json: typing.Optional[typing.Any] = None,
            files: typing.Optional[typing.Dict[str, typing.Any]] = None,
            params: typing.Optional[dict] = None,
            headers: typing.Optional[dict] = None,
            cookies: typing.Optional[typing.Union[dict, RequestsCookieJar]] = None,
            auth: typing.Optional[typing.Union[typing.Tuple[str, str], AuthBase]] = None,
            timeout: typing.Optional[typing.Union[float, typing.Tuple[float, float]]] = None,
            allow_redirects: bool = True,
            **kwargs
    ) -> Response:
        response = super().patch(
            url=self._base_url + url,
            data=data,
            json=json,
            files=files,
            params=params,
            headers=headers,
            cookies=cookies,
            auth=auth,
            timeout=timeout,
            allow_redirects=allow_redirects,
            **kwargs
        )
        attach_request_and_response(response)
        return response

    @allure.step('Performing DELETE request to "{url}"')
    def delete(
            self,
            url: str,
            *,
            params: typing.Optional[dict] = None,
            headers: typing.Optional[dict] = None,
            cookies: typing.Optional[typing.Union[dict, RequestsCookieJar]] = None,
            auth: typing.Optional[typing.Union[typing.Tuple[str, str], AuthBase]] = None,
            timeout: typing.Optional[typing.Union[float, typing.Tuple[float, float]]] = None,
            allow_redirects: bool = True,
            **kwargs
    ) -> Response:
        response = super().delete(
            url=self._base_url + url,
            params=params,
            headers=headers,
            cookies=cookies,
            auth=auth,
            timeout=timeout,
            allow_redirects=allow_redirects,
            **kwargs
        )
        attach_request_and_response(response)
        return response


class APIClient:
    """
    API client based on HTTP client
    """

    def __init__(self, client: HTTPClient) -> None:
        self._client = client

    @property
    def client(self) -> HTTPClient:
        return self._client
