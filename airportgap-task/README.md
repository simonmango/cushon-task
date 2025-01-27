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
├── airportgap/             # test folder projects - mapped to `/app`  
│   └── reports/            # test reports  
│       tests               # the project tests
│       conftest.py         # pytest configuration  
│       Pipfile             # Python environment configuration file  
│       Pipfile.lock        # Python environment configuration lock file  
│       airportgap-tests.sh # bash script to execute the tests in the container
```

## Preparing the environment  
In a terminal, navigate to this projects directory and execute the command:
```
docker compose up --build --detach
```


## Running the tests  
In a terminal, navigate to this projects directory and execute the following commands:  
```
docker compose run sweetshop-pytest /app/airportgap-tests.sh
```
This will execute the tests - you will see the tests being executed and the test results will be displayed.


## Getting the test results  
The test results are captured in an HTML report located in the `airportgap/reports` folder.  


## Test structure  
The `tests` folder contains the main `test_login.py` file.  
The `pages` folder contains the Page Object model files used by the test. The `site.py` file contains methods that are 
common to the whole site.  


## Problems & Further Improvements
* The Rate limit for AirportGap requests is 100 requests per endpoint per minute per source IP address. This means 
that all other tests for the same endpoint will have an impact on these rate limit tests if coming from the same IP 
address. Need to think about how we can execute these tests without affecting the other tests. Perhaps provisioning
a different test agent to execute these tests from.
* Leverage Service Object Model (similar to Page Object Model) to improve separation of concerns and maintainability.
* Improve the docker-compose configuration so that the environment can be built and tests run from a single
`docker compose run` command.  


