## Python

### Static type checking

- start using [mypy](https://mypy.readthedocs.io/en/stable/getting_started.html) on my future python type annotations
- regardless of whether a type check is done, include type annotations for better readability, python type annotations are essentially treated as comments by python and won't break code.

### Use existing libraries whenever possible

- for example, if the datetime library is not fun to use, try to find an alternative packages like pendulum to use instead of making something from scratch (unless absolutely necessary)

### Follow PEP8

- Use a linter!!!

### UnitTest

- include tests as new functionality is created. Use builtin unittest framework or another like pytest
- include test data if necessary
- tests should run "no strings attached", should be able to git clone and simply python unittest with tests passing

### Fail gracefully

- include exception types when catching (know what to expect) and print any "unknown" exceptions as well. Failing gracefully != Failing silently. 
- applications can be disgned as if ready to run in an infinite loop. When an error occurs the program should not just exit, but produce an error indicating the issue and continue to run. 
