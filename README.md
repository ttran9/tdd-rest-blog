# Testing and CI/CD Course

- Section 2 / Video 11:
  - [Coverage](https://coverage.readthedocs.io/en/coverage-5.2.1/): A tool to help you measure the coverage.
  - coverage run manage.py test
    - tells coverage to run your tests.
    - this does not exclude the virtualenv (env) directory.
  - coverage run --omit="_/env/_" manage.py test
  - coverage report
    - generate the coverage report
  - coverage html
    - generate html document for us
      - htmlcov directory.
  - coverage xml
    - generate xml document for us
      - can be useful when using coverage with CI (continuous integration)
