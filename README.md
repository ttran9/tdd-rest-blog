# Testing and CI/CD Course

- Section1/Video5:
  - When we are writing our unit tests we want to test one small piece of logic per test.
  - Example: One makes changes, writes tests and makes changes and then pushes to a remote branch. Another developer will then pull the changes onto his/her side and run the tests (to make sure the changes are working). The developer will write their code, run the tests, and then push the changes to the remote branch.
    - Developers will want to follow this general type of cycle where they will write code, write tests, and push it to a remote branch and if another developer writes code and tests, then it must be tested on another developer's side locally first before proceeding.