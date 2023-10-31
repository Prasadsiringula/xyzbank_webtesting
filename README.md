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

#3.It will ask github link and author name  (we need to mention autor name and our github link)
#4.generate's a "package.json file" in which we will give few required package names for npm setup as mention below
    "setup": "python3 -m pip install --upgrade pip && pip install -r requirements.txt && npm install && npm i -d allure-commandline && playwright install && pip install --upgrade setuptools && pip install --upgrade distribute",
    "test": "echo \"Error: no test specified\" && exit 1",
    "login_test": "pytest -s -v --alluredir=allure-results",
    "gen-allure": "allure generate ./allure-results --clean && allure open ./allure-report",
    "clean-allure": "del-cli --force allure-results && del-cli --force allure-report",
    "e2e": "npm run clean-allure && npm run login_test && npm run gen-allure" 
#5.we will going to paste this sourcecode from setup script line "7 to 12" json file.
#6.when we run command ```npm run setup``` </br> 
   on terminal it will automatically install required dependencies which we mention in json.file,
#7.After upgrading pip, the script installs Python packages listed in the requirements.txt file. These packages are essential for the Python-based aspects of the project.
#8.The setup command process installs the Allure command-line tool, which is used to generate and view test reports
   by giving this source code we dont need to give commands manully to install the required packages it will automatically invokes them while we give command like "npm install" in terminal
#9.if we get errors (pytest not recognized) while setting up npm we need to run this 2 commands in terminal   
       "pip install --upgrade setuptools
        pip install --upgrade distribute"
        After the  Python package installation, the setup  command upgrades two important Python packages, setuptools and distribute. These upgrades are necessary for compatibility and functionality.
#10.To get an proper idea  about list of  files which are installed  
we use ```pip list``` </br> command 
#11.once setup is done we will check working of npm with command ```npm run setup```.
#12.if it working well we will run npm and  genrates e2e allure report with ```npm run e2e``` </br> command.  

