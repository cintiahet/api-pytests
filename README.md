# API sample tests with pytest

## Setup & installation

### Python and VirtualEnv
- Install Python 3
    - https://www.python.org/downloads/
- Install virtualenv. Virtualenv allows you to create an isolated Python environment, with full control over which Python version to use and which Python packages to install.
    - If you have only Python 3 installed: ```pip install --user virtualenv```. 
    - If you need to figure out what you have installed, you can run ```python --version``` and/or ```python3 --version``` from the command line.

### Setup a virtual environment
We will be using this virtual environment both for running the tests
 
- Create a virtual python environment
	- Note that this will create the virtual environment in the current directory, so create a project folder and pick it
    - If you have only Python 3 installed: ```python -m virtualenv <venv-name>```. we suggest that the venv name represent the project name ( e.g. projectname-venv)
- Activate the virtualenv (linux, mac: `source <venv-name>/bin/activate`) or (win: ```<venv-name>\Scripts\activate```)
- Once you're done with the virtual environment, type ```deactivate``` to deactivate it.

### Download and install this repo

- Activate your venv
- Download this repository by clicking the green ```Clone or download```.
- Install requirements.txt (```pip install -r requirements.txt```)

### API reference from where base examples were created
- https://restful-booker.herokuapp.com/apidoc/index.html

### Pytest
#### Run tests from terminal

Pytest will collect tests based on the following criteria:

Search the current directory and all sub-directories for files named test_*.py or *_test.py that contain functions named test_*
To run the tests, execute pytest in the directory containing your tests, or specify the path: pytest <path_to_dir>.

Docs: https://docs.pytest.org/en/latest/getting-started.html#create-your-first-test

#### Asserts
Pytest allows you to use the standard python assert for verifying expectations and values in Python tests. For example, you can write the following:
```
<actual value> == <expected value> to check actual values against expected values
```
https://docs.pytest.org/en/3.0.1/assert.html


#### Fixtures

The purpose of test fixtures is to provide a fixed baseline upon which tests can reliably and repeatedly execute.

fixtures are implemented in a modular manner, as each fixture name triggers a fixture function which can itself use other fixtures.
fixture management scales from simple unit to complex functional testing, allowing to parametrize fixtures and tests according to configuration and component options, or to re-use fixtures across function, class, module or whole test session scopes.

To create a fixture, write a function and add the @pytest.fixture decorator to that function. Any test function can then use the return value(s) of your fixture, by using the function's name as an argument for the test function:

fixtures have explicit names and are activated by declaring their use from test functions, modules, classes or whole projects:

function is limited to a particular test (default)
module is limited to a particular file
session is executed once for all the tests you're running Here's how you'd modify your fixture decorator to limit the fixture to one test: @pytest.fixture(scope="function").
Note that not only tests can use fixtures, fixtures can also use other fixtures.

Docs: https://docs.pytest.org/en/latest/fixture.html

### Requests library - response object

All the HTTP methods of the requests library (requests.get(), requests.post(), etc.) return a response object. This object contains all the information we need for logging purposes:

response.status_code
response.headers
response.text
response.json() (json parsed to a Python dictionary)
response.request.url
response.request.method
response.request.headers
response.request.body
Docs: http://docs.python-requests.org/en/master/api/#requests.Response

### Advanced text editor
- Any advanced text editor with the following features will do:
    - syntax highlighting (easier to read)
    - word completion (avoids typos in names of variables, functions and methods)
- If you're note sure which one to use, Visual Studio Code is a good choice: https://code.visualstudio.com/
    - You can find VS Code's Python plugin here: https://marketplace.visualstudio.com/items?itemName=ms-python.python
    - To tell VS Code to use the interpreter in your virtual environment: https://code.visualstudio.com/docs/python/environments#_select-and-activate-an-environment
    - To enable autosave: https://code.visualstudio.com/docs/editor/codebasics#_save-auto-save 
- Using an IDE like PyCharm is fine too.
    - To tell PyCharm to use the interpreter in your virtual environment: https://www.jetbrains.com/help/pycharm/configuring-python-interpreter.html
    - To tell PyCharm to use pytest to run tests: https://www.jetbrains.com/help/pycharm/pytest.html#enable-pytest

### Allure reports

First you need to install Allure 
Manual installation
1 Download the latest version as zip archive from Maven Central.

2 Unpack the archive to allure-commandline directory.

2 Navigate to bin directory.

3 Use allure.bat for Windows or allure for other Unix platforms.

4 Add allure to system PATH.

5 Check the installation: ```allure --version```

doc: https://docs.qameta.io/allure/

Generate reports and display manually

- run tests pointing reports directory: 
```pytest --alluredir=<reports directory path>```
- display report:
```allure serve <reports directory path>```

### Locust performance
To run Locust locally with the example Locust file named locustfile.py you should:
 - Run ```locust --host https://restful-booker.herokuapp.com/ -f ./tests/locustfile.py```
 - Open up Locust’s web interface
    Once you’ve started Locust using the above command line, you should open up a browser and point it to http://localhost:8089
 - In the Start new Locust swarm page, set up the parameters
    - Number of total users to simulate: with the number of users you want to test
    - Hatch rate (users spawned/second)
    And Start swarming
 - Check the statistics and graph
 - Stop the run

Doc: https://docs.locust.io/en/stable/index.html

### Reference materials
- Python cheatsheet
https://github.com/ehmatthes/pcc/releases/download/v1.0.0/beginners_python_cheat_sheet_pcc.pdf
- Requests:
http://docs.python-requests.org/en/master/
- Pytest:
https://docs.pytest.org/en/latest/contents.html and https://docs.pytest.org/en/latest/reference.html
- Allure
https://docs.qameta.io/allure/

