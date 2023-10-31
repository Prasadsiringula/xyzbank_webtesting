# xyzbank_webtesting
testing xyzbank website playwright
#1. To setup npm we will use command ```npm init```. </br>
#2. Update Pacakage .json with the below
  "dependencies": {
    "@playwright/test": "^1.39.0",
    "allure": "^0.0.0",
    "allure-commandline": "^2.24.1",
    "allure-playwright": "^2.9.2",
    "del-cli": "^5.1.0",
    "express": "^4.18.2"
  } 
then execute ```npm update``` </br>

it will ask github link and author name 
it will generate a "package.json file" in which we will give few required package names for npm setup  as mention below
    "setup": "python3 -m pip install --upgrade pip && pip install -r requirements.txt && npm install && npm i -d allure-commandline && playwright install && pip install --upgrade setuptools && pip install --upgrade distribute",
    "test": "echo \"Error: no test specified\" && exit 1",
    "login_test": "pytest -s -v --alluredir=allure-results",
    "gen-allure": "allure generate ./allure-results --clean && allure open ./allure-report",
    "clean-allure": "del-cli --force allure-results && del-cli --force allure-report",
    "e2e": "npm run clean-allure && npm run login_test && npm run gen-allure" 
we will going to paste this sourcecode from line "7 to 12" in json file.
This code will generate end to end allure report and clears the previous report.
by giving this source code we dont need to give commands manully to install the required packages it will automatically invokes them while we give command like "npm install" in terminal
  if we get errors (pytest not recognized) while setting up npm we need to run this 2 commands in terminal   
       "pip install --upgrade setuptools
        pip install --upgrade distribute"
To get an proper idea  about list of  files which are installed  
we use "pip list" command 
once setup is done we will check working of npm with command (npm run setup).
if it working well we will run npm and  genrates e2e allure report with (npm run e2e)  command   

