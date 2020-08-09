"""Test stargazers.py"""
# pylint: disable=C,R,W
import mock
import requests
import unittest

import stargazers


class TestStargazers(unittest.TestCase):

    def setUp(self):
        self.star_class = stargazers.Stargazers(repo_owner='test', repo_name='test')
        self.test_json_data = {'stargazers_count': 100}

    def _mock_response(self, status=200, content="CONTENT", json_data=None, raise_for_status=None):
        """Requests has lots of data so mock it more formally."""
        mock_resp = mock.Mock()

        mock_resp.raise_for_status = mock.Mock()
        if raise_for_status:
            mock_resp.raise_for_status.side_effect = raise_for_status

        mock_resp.status_code = status
        mock_resp.content = content

        if json_data:
            mock_resp.json = mock.Mock(return_value=json_data)
        return mock_resp

    @mock.patch('requests.get')
    def test_get_raw_response_no_raise(self, mock_request):
        """Test that _get_raw_response() does not raise on 202."""
        mock_request.return_value = self._mock_response(status=202)
        star_obj = self.star_class._get_raw_response(params={})
        self.assertTrue(star_obj.raise_for_status.called)

    @mock.patch('requests.get')
    def test_get_raw_response_raise(self, mock_requests):
        """Test that _get_raw_response() raises a HTTPError on 404."""
        mock_requests.return_value = self._mock_response(status=404,
                                                         raise_for_status=requests.HTTPError('Error!'))
        with self.assertRaises(requests.HTTPError):
            self.star_class._get_raw_response(params={})

    @mock.patch('stargazers.Stargazers._get_raw_response')
    def test_get_stars(self, mock_stargazer):
        """Test that _get_stars() returns integer value."""
        mock_stargazer.return_value = self._mock_response(json_data=self.test_json_data)
        num_stars = self.star_class._get_stars()
        self.assertEqual(num_stars, 100)

    @mock.patch('stargazers.Stargazers._get_raw_response')
    def test_get_stars_unknown(self, mock_stargazer):
        """Test that _get_stars() returns UNKNOWN on HTTPError."""
        mock_stargazer.side_effect = requests.HTTPError('Error!')
        num_stars = self.star_class._get_stars()
        self.assertEqual(num_stars, "UNKNOWN")

    @mock.patch('stargazers.Stargazers._get_stars')
    def test_stars(self, mock_stars):
        """Test that stars property returns defined output."""
        mock_stars.return_value = 25
        print_stars = self.star_class.run()
        self.assertEqual(print_stars, 'Repository: test/test -> Stars: 25')


if __name__ == '__main__':
    unittest.main()
