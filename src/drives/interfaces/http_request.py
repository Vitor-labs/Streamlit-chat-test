"""
This module defines an abstract class to handle HTTP requests
"""
from abc import abstractmethod, ABCMeta

from httpx import AsyncClient


class HttpRequestInterface(metaclass=ABCMeta):
    """
    Abstract class to handle HTTP requests

    implements methods to request an authentication token
    and create a client to be used in future requests also
    the calling method to send the request
    """
    
    @classmethod
    @abstractmethod
    def request_token(cls, endpoint:str, headers:dict) -> str:
        """
        tries to request a authentication token to be used in future requests

        Args:
            endpoint (str): url of the API key generation
            headers (dict): headers of the request

        Raises:
            NotImplementedError: method not implemented

        Returns:
            str: API key to be used in future requests
        """
        raise NotImplementedError("HttpRequest.request_token() not implemented")
    
    @abstractmethod
    def create_client(self) -> AsyncClient:
        """
        creates a client to be used in future requests

        Raises:
            NotImplementedError: method not implemented
        """
        raise NotImplementedError("HttpRequest.create_client() not implemented")
    
    @abstractmethod
    def send_request(self, headers:dict, data:dict) -> dict:
        """
        sends a request to the API

        Args:
            headers (dict): headers of the request
            data (dict): data of the request

        Raises:
            NotImplementedError: method not implemented

        Returns:
            dict: response of the request (status code and content)
        """
        raise NotImplementedError("HttpRequest.send_request() not implemented")
