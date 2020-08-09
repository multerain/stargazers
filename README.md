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

## Notes
* GitHub API is rate limited - unauthorized requests are capped at ~60 per hour
    * Opportunity to improve - provide interface for authorizing against GitHub
