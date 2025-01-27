# Requirements  
This project requires Docker Compose.  
See the Docker documentation for installation details on your host system:
>https://docs.docker.com/compose/install/


## Project structure  
```
project/  
├── README.md               # this file  
├── Dockerfile              # test suite docker file  
├── docker-compose.yml      # configuration of test suite container services  
├── sweetshop/              # test folder projects - mapped to `/app`  
│   └── reports/            # test reports  
│       ├── screenshots     # screenshots of any test failures
│       tests               # the project tests
│       ├── pages/          # Page Object Model used by the tests
│       conftest.py         # pytest configuration  
│       Pipfile             # Python environment configuration file  
│       Pipfile.lock        # Python environment configuration lock file  
│       sweetshop-tests.sh  # bash script to execute the tests in the container
```

## Preparing the environment  
In a terminal, navigate to this projects directory and execute the command:
```
docker compose up --build --detach
```

## Running the tests  
In a terminal, navigate to this projects directory and execute the following commands:  
```
docker compose run sweetshop-pytest /app/sweetshop-tests.sh
```
This will execute the tests - you will see the tests being executed and the test results will be displayed.


## Getting the test results  
The test results are captured in an HTML report located in the `sweetshop/reports` folder.  
Screenshots are displayed in the test report HTML page but if you want to seem them separately you can locate them in 
the `sweetshop/reports/screenshots` folder.  


## Test structure  
Although we are not using a BDD framework - such as `pytest-bdd` - I have written the tests in a BDD style structure.  
The `tests` folder contains the main `test_login.py` file.  
The `pages` folder contains the Page Object model files used by the test. The `site.py` file contains methods that are 
common to the whole site.  


## Page Object Model class structure
I have separated each of the Page Object Model class methods into three separate groups:
* Charactersitics - Properties or conditions of the page such as the address, or whether it has finished loading.  
* Elements - Specific parts of the page such as a title, a specific form field or a link.  
* Actions - Actions that can be performed on parts of the page such as _filling_ in a form field, clicking a link etc.   


## Further improvements
* Implement Firefox browser to execute with the tests  
* Page Object Model - Investigate frameworks that work with Pytest and see if any of these could provide POM features 
that are useful but do not over-complicate the project.  
* Improve the docker-compose configuration so that the environment can be built and tests run from a single `docker compose run` command.  
