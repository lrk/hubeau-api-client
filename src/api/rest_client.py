import logging

import requests

from . import API_BASE_URL, API_DEFAULT_VERSION


log = logging.getLogger(__name__)


class HubeauRestApi(object):
    default_headers = {'Content-Type': 'application/json',
                       'Accept': 'application/json'}

    def __init__(self, api_base_url=API_BASE_URL, api_version=API_DEFAULT_VERSION):
        """Default constructor."""
        self.api_base_url = api_base_url
        self.api_version = api_version

    def merge_headers(self, headers=None):
        """Merge headers."""
        if headers:
            merged_headers = self.default_headers.copy()
            merged_headers.update(headers)
            return merged_headers
        else:
            return self.default_headers

    def get_endpoint_url(self, endpoint):
        """Return endpoint URL."""
        logging.debug(f"endpoint URL for {endpoint}")
        return '/'.join([self.api_base_url, endpoint])

    def request(self, method='GET', path='/', params=None, headers=None):
        """Execute request."""
        url = self.get_endpoint_url(endpoint=path)
        logging.debug(f"Sending GET Request to {url} with params: {params}")
        response = requests.request(
            method=method, url=url, params=params, headers=self.merge_headers(headers))

        log.debug("Send request to {} {} -> {} {}".format(method,
                                                          path, response.status_code, response.reason))

        response.raise_for_status()
        return response

    def get(self, path, params=None, headers=None):
        """Execute GET request."""
        response = self.request(
            'GET', path=path, params=params, headers=headers)

        if (response.ok):
            return response.content
        else:
            response.raise_for_status()
