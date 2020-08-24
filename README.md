# Testing and CI/CD Course

- Section1/Video3:
  - [Django Testing](https://docs.djangoproject.com/en/3.1/topics/testing/)
  - [Unit Testing Module](https://docs.python.org/3/library/unittest.html#module-unittest)
  -[Writing unit tests example](https://docs.djangoproject.com/en/3.1/topics/testing/overview/#writing-tests)
    - There is a test database that gets created and after all tests the test database is deleted.
    - Speeding up tests below (3 methods discussed)
        - There is a flag (test --keepdb) that can keep the database when we are running a great number of tests to speed tests up a bit.
        - We can also run the tests in parallel (-- parallel).
        - We can speed the tests up by using md5 hashing (when dealing with passwords).