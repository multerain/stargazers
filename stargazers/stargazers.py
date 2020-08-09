"""Module to print number of 'stars' of a given GitHub repository."""
import logging
import threading
import requests

_log = logging.Logger(__name__)


class Stargazers(threading.Thread):
    """GitHub API Stargazers object.

    Inherit from threading.Thread so we can service lots of calls to GitHub API quickly.

    :param str repo_owner: GitHub repository owner
    :param str repo_name: GitHub repository repo_name
    :cvar dict DEFAULT_REST_OPTIONS: Default parameters to pass to the GitHub Rest Stargazers API call
    """

    DEFAULT_REST_OPTIONS = {'accept': 'application/vnd.github.v3+json'}

    def __init__(self, repo_owner, repo_name):
        super(Stargazers, self).__init__()
        self.repo_owner = repo_owner
        self.repo_name = repo_name
        self.endpoint = f'https://api.github.com/repos/{self.repo_owner}/{self.repo_name}'

    def _get_raw_response(self, params):
        """Method to make a requests.get call to stargazers endpoint.

        :param dict params: Passthrough dictionary, list of tuples or bytes for Requests module
        :rtype: requests.Response
        """
        response = requests.get(self.endpoint, params)
        response.raise_for_status()
        return response

    def _get_stars(self):
        """Method to get the number of Stars associated with the given GitHub repository."""
        try:
            api_response = self._get_raw_response(params=self.DEFAULT_REST_OPTIONS)
        except requests.HTTPError as ex:
            _log.error(f'Caught HTTP Error: {ex}, setting stars to UNKNOWN')
            return 'UNKNOWN'

        return api_response.json().get('stargazers_count')

    def run(self):
        """Override Thread.run that prints a nice description of the repo and number of stars."""
        stars = self._get_stars()
        output_str = f'Repository: {self.repo_owner}/{self.repo_name} -> Stars: {stars}'
        print(output_str)
        return output_str
