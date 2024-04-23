# Shell CheatSheet backend

## Must have python3.10
It can be downloaded from https://www.python.org/downloads/ \
If this command runs, it's all OK. \
It is advised to be at least 3.10.8.

`python3.10 --version`

## Go to backend folder
If you are already in the folder 'backend', skip this step.\
Depending on your position in the files, the command below will not work.\
In order to do so, you must be at the root of this project.

`cd DEV/backend` 

# Installation 	
## Windows installation
To create a virtual environment and its dependencies on **Windows**.

`python3.10.exe -m venv venv`\
`.\venv\Scripts\activate`\
`pip3 install -r .\requirements.txt`\
`deactivate`

## macOS installation
To create a virtual environment and its dependencies on **Mac / Linux**.

`python3.10 -m venv venv`\
`source ./venv/bin/activate`\
`pip3 install -r ./requirements.txt`\
`deactivate`

# Development
## Windows run
To activate and update the requirements in your virtual environment on **Windows**.

`.\venv\Scripts\activate`\
`pip3 install -r .\requirements.txt -q`

## macOS run
To activate and update the requirements in your virtual environment on **Mac / Linux**.

`source ./venv/bin/activate`\
`pip3 install -r ./requirements.txt -q`

# Save changes
## Windows save
Save the changes to the requirements that you made on **Windows**.\
(In case you installed something with pip)

`pip3 freeze > .\requirements.txt`\
`deactivate`

## Mac / linux save
Save the changes to the requirements that you made on **Mac / Linux**.\
(In case you installed something with pip)

`pip3 freeze > ./requirements.txt`\
`deactivate`