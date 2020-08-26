# Testing and CI/CD Course

- Section 2 / Video 10:
  - The requestfactory doesn't have a session and middleware included so you can't test to see if a message is sent.
  - The rf is similar to using the Django client but the rf to test a view similar to how you would test a python function.
  - Using a request factory can be useful in case you want to remove as much of the request response cycle as possible.