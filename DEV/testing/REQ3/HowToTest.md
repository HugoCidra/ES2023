# Pre-requisites to run Selenium tests with Python

The easiest way to install Selenium on a Python environment is through the installer pip.
"pip install selenium"

"pip install webdriver-manager" for the executables to solve the problem where the Drivers aren't installed on the same Path as the scripts~


# Multiple Python tests in parallel

Usage of Python built-in unittest framework (PyUnit) and Py.test with the plugin pytest-xdist 
and plugin pytest-rerunfailures to run parallel tests and rerun failed tests,
logging output to a log.txt file. You could also use nose to run tests in parallel.

- pip install pytest

- pip install pytest-xdist

- pip install pytest-rerunfailures

- pip install pytest-selenium

- pip install pytest-variables

## ATTENTION
If you wanna make multiple tests on a script

- Your class should start with Test to be automatically picked up by the test discovery mechanism.
Or, subclass the unittest.TestCase:

- Make sure that your file name matches the pattern: test_*.py or *_test.py.

- Make sure that your function name starts with the test prefix.
