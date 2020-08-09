#!/usr/bin/env python
"""GitHub Stargazers CLI."""
import logging
import sys

import stargazers
import utilities

_log = logging.Logger(__name__)


def cli_header():  # pylint: disable=missing-function-docstring
    print("""GitHub Stargazers CLI
Author: Daniel Suhr <danielmsuhr@gmail.com>
Please enter a comma or space separate list of GitHub repositories
The CLI will return the number of people who have Starred that repository.

Format: owner/repo  -->  ie, EbookFoundation/free-programming-books
Type help to see this message again, or quit to exit the CLI.""")


def main():
    """GitHub Stargazers CLI."""
    cli_header()
    while True:
        user_input = input('==>')
        repositories = utilities.input_to_list(user_input)

        if user_input in ('quit', 'exit'):
            sys.exit()
        elif user_input in ['help']:
            cli_header()
        elif repositories is None:
            _log.warning('Invalid format, please enter a comma or space separated list of GitHub repos.')
        else:
            threads = []
            for repo in repositories:
                owner = repo.split('/')[0]
                name = repo.split('/')[1]

                get_star = stargazers.Stargazers(owner, name)
                get_star.start()
                threads.append(get_star)

            for thread in threads:
                thread.join()


if __name__ == '__main__':
    main()
