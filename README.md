# xyzbank_webtesting
testing xyzbank website playwright
To setup npm (npm init).
it will ask github link and author name 
it will generate a "ackage.json file" in which we will give few required package names for npm setup  as mention below
    "setup": "python3 -m pip install --upgrade pip && pip install -r requirements.txt && npm install && npm i -d allure-commandline && playwright install && pip install --upgrade setuptools && pip install --upgrade distribute",
    "test": "echo \"Error: no test specified\" && exit 1",
    "login_test": "pytest -s -v --alluredir=allure-results",
    "gen-allure": "allure generate ./allure-results --clean && allure open ./allure-report",
    "clean-allure": "del-cli --force allure-results && del-cli --force allure-report",
    "e2e": "npm run clean-allure && npm run login_test && npm run gen-allure" 
    we will going paste this sourcecode from line "7 to 12"
    this code will generate end to end allure report and clears the previous report.
    by giving this source code we dont need to give commands manully for the required packages it will automatically it invokes them while 
    give command like "npm install" in terminal
  if we get errors (pytest not recognized) while setting up npm we need to run this 2 commands in terminal   
       "pip install --upgrade setuptools
        pip install --upgrade distribute"
To get an proper idea  about list of  files which are installed  
we use "pip list" command 
once setup is done we will check working of npm with command (npm run setup).
if it working well we will run npm and  genrates e2e allure report with (npm run e2e)  command   

