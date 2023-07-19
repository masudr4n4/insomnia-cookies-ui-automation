## Insomnia Cookies


# Introduction 
Website Automation framework for Insomnia cookies.


## Getting Started
1.	Installation process
    
    1.1 Pycharm IDE
    1.2 Allure reporting library
    1.4 Pip    
    
    Import the code in Pycharm IDE and start off with coding
    
2.	Software dependencies
    
    2.1 All software dependencies are present in requirements.txt present in the same repository

## Build and Test
1. Import the code in Pycharm IDE.
2. Go to Settings > Tools > Python Integrated Tools
3. Go to Package requirements file 
4. Browse the location of requirements.txt file present in the repository and click OK.
5. Install the dependencies by clicking on Install requirements.

## Run Tests

1. Go to Add Configuration 
2. Select pytest from the dropdown
3. Set the location of the Testcase file starting with "test_" in the Target field.
4. Provide the additional arguments such as (-S <server_name> , -m <markers_to_be_executed>, -n <number_of_parallel_threads> ,-O <os_name> --alluredir =<path_to_results>)
5. The testcases can also be run from commandline using py.test <path_to_testcases> <arguments>
6. After merge command: pytest -s TestCases -v -m regression/smoke -S "web.stage"

## Allure report generation
1. Create a directory for collecting the Allure reports
2. Add the following argument when running the tests: 

        --alluredir=<allure_directory_path>

3. After finishing running the tests, run the following command: 

        allure serve <allure_directory_path>

# Docker

## Getting Started
1. Installation process
    1. Download and install [Docker](https://docs.docker.com/get-docker/)
        - You must have docker credentials in order to use docker containers (Free)
    3. Configuration:
        We use docker-compose to create our environment. In order to properly run test we need to update the `devops/docker-compose.yml` 
    2. Makefile
        - With Makefile you will need to run `make build` to build the environment
    

## Run Tests
1. Be sure containers are running
2. Makefile
    - `make start` - Start/Verify containers are running
    - `make tests` - Run All tests
    - `make single_run` - Run all test (start and stop e2e-container automatically, reports are generated)

## Reports
1. Reports are generated and can be viewed om in the `allure` and `junit` folder.
2. Makefile
    - `make perms` - will fix any permissions issue you may face with viewing/editing allure reports
    - `make cleanup`  - will remove the allure and junit folders.
      <img width="840" alt="image" src="https://github.com/masudr4n4/insomnia-cookies-ui-automation/assets/34313493/c367695d-0dd4-4aba-a4d5-870d65d4bb6f">

## HTML reports
<img width="1276" alt="image" src="https://github.com/masudr4n4/insomnia-cookies-ui-automation/assets/34313493/a13ee5a7-0c12-44f3-878a-2491fb11098f">


## Running single test
1. To run a single test use the following command
    `docker-compose -f Devops/docker-compose.yml exec -T e2e-tests pytest -O Linux -n 1 -U "<URL>" <Test> -H "True" --junitxml=junit/test-results.xml --alluredir=allure`        

## Things to note:
    - Docker container is always running. if Command Entered into docker compose after the command executes the container will shutdown.
    - selenium session hub:
        - To view active selenium sessions
        - `http://{localIPAddress}:4444/wd/hub/static/resource/hub.html`
