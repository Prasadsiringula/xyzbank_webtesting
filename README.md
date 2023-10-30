# xyzbank_webtesting
testing xyzbank website playwright
To setup npm we will use command (npm init).
it will ask github link and author name 
it will generate a "package.json file" in which we will give few required package names for npm setup  as mention below
    "setup": "python3 -m pip install --upgrade pip && pip install -r requirements.txt && npm install && npm i -d allure-commandline && playwright install && pip install --upgrade setuptools && pip install --upgrade distribute",
    "test": "echo \"Error: no test specified\" && exit 1",
    "login_test": "pytest -s -v --alluredir=allure-results",
    "gen-allure": "allure generate ./allure-results --clean && allure open ./allure-report",
    "clean-allure": "del-cli --force allure-results && del-cli --force allure-report",
    "e2e": "npm run clean-allure && npm run login_test && npm run gen-allure" 
we will going to paste this sourcecode from line "7 to 12" in json file.
when we run command "npm run setup" on terminal it will automatically install required dependencies which we mention in setup line code at 7th line json.file,
After upgrading pip, the script installs Python packages listed in the requirements.txt file. These packages are essential for the Python-based aspects of the project.
The setup command process installs the Allure command-line tool, which is used to generate and view test reports
by giving this source code we dont need to give commands manully to install the required packages it will automatically invokes them while we give command like "npm install" in terminal
  if we get errors (pytest not recognized) while setting up npm we need to run this 2 commands in terminal   
       "pip install --upgrade setuptools
        pip install --upgrade distribute"
        After the  Python package installation, the setup  command upgrades two important Python packages, setuptools and distribute. These upgrades are necessary for compatibility and functionality.
To get an proper idea  about list of  files which are installed  
we use "pip list" command 
once setup is done we will check working of npm with command (npm run setup).
if it working well we will run npm and  genrates e2e allure report with (npm run e2e)  command   

