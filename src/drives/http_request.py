"""
This module implements a class to handle HTTP requests asynchronously
"""
import httpx
import asyncio
from typing import Dict

from src.drives.interfaces.http_request import HttpRequestInterface


class HttpRequest(HttpRequestInterface):
    """
    This class implements methods to request an authentication token
    and create a client to be used in future requests also
    the calling method to send the request
    """
    def __init__(self, url:str) -> None:
        self.__url = url       

    @classmethod
    def request_token(cls, endpoint:str, headers:dict) -> str:
        """
        TODO: refact this use case later for real use
        tries to request a authentication token to be used in future requests

        Args:
            endpoint (str): url of the API key generation
            headers (dict): headers of the request

        Returns:
            str: API key to be used in future requests
        """
        response = httpx.get(endpoint, headers=headers)

        if response.status_code == 200:
            return response.json()['key']

        raise httpx.RequestError("HTTP request failed")

    def create_client(self) -> httpx.AsyncClient:
        """
        TODO: refact this use case later for real use
        creates a client to be used in future requests

        Returns:
            AsyncClient: client to be used in future requests
        """
        return httpx.AsyncClient()

    def send_request(
            self, headers:Dict[str,str], data:Dict[str,str]
        ) -> Dict[str, int | str]:
        """
        TODO: refact this use case later for real use
        sends a request to the API

        Args:
            headers (dict): headers of the request
            data (dict): data of the request

        Returns:
            dict: response of the request (status code and content)
        """
        response = httpx.post(self.__url, headers=headers, json=data)

        return {
            'status_code': response.status_code,
            'content': response.json()['content'],
        }
