# Stargazers Dockerfile definition that runs tests then returns final image
FROM python:3.8 as test
RUN python -m pip install pipenv
WORKDIR /stargazers
COPY Pipfile* /stargazers/
COPY stargazers /stargazers
COPY tox.ini /stargazers
COPY .pylintrc /stargazers
RUN python -m pipenv lock --requirements > requirements.txt
RUN python -m pipenv install --dev
RUN python -m pipenv run coverage run -m unittest && \
    python -m pipenv run coverage report --fail-under 100 stargazers.py utilities.py
RUN python -m pipenv run pycodestyle . && \
    python -m pipenv run pylint .

FROM python:3.8 as stargazers
WORKDIR /stargazers
COPY --from=test /stargazers/requirements.txt ./
COPY stargazers /stargazers
RUN rm -r tests/ && python -m pip install -r requirements.txt
ENTRYPOINT ["/stargazers/cli.py"]
