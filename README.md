# GitHub Stargazers Exercise

## Problem Statement
* The CLI must accept an arbitrary list of GitHub repository names (org/repo). It issues a request
to the server which returns the number of “stars” for each repository in one single response.
* The CLI must display the server response in human readable format.

### Bonus
* Set up minikube​ or​ kind​ and deploy the​ server​ application to your local test cluster.

## Build/test requirements: Docker
* The Dockerfile will only build if there is 100% unit test coverage, and pylint and pycodestyle checks pass
* Build: `docker build -t stargazers -f Dockerfile .`

## Use CLI: `docker run -it stargazers`

## Local Environment Setup
* Code was written using Python 3.8 on Ubuntu 20.04, using Pip + Pipenv as the dependency/package manager
    * `apt-get install python3.8` + `apt-get install python3-pip` + `python -m pip install pipenv`
    * I have had problems with Python and Pip where the Pip that was installed via Apt was setup for Python 3.6 so you might need to install Pip from source and use update-alternatives to align your Pip version with your Python version.
* Once you have Python + Pip + Pipenv
    * `python -m pipenv install --dev` will install both the CLI and test development dependencies
    * `python -m pipenv shell` will put your terminal into a Python subshell with your dependencies for quick development
* Tests & static code analysis:
    * While inside pipenv shell:
        * Run unit tests: `coverage run -m unittest`
        * View coverage report: `coverage report -m stargazers/stargazers.py stargazers/utilities.py`
        * Run pylint: `pylint stargazers/`
        * Run pycodestyle: `pycodestyle stargazers/`

## Notes
* GitHub API is rate limited - unauthorized requests are capped at ~60 per hour
    * Opportunity to improve - provide interface for authorizing against GitHub
