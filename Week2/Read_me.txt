Objective:
Build a ‘conserve’ Python data science artifacts with Docker

Technology:
Docker
Jupyter
Python

Process:
Pick your favorite Jupyter notebook
Setup a Docker container
Write a Dockerfile that sets up a basic container from python but specify a version (don’t use latest - think about why)
Create a new user -- use an environment variable to specify the username
Create a directory in the home directory of your user for the notebooks
Download your favorite notebooks into this folder
Make sure that your new user owns everything that is in the folder (think about this, when would you do this, when not)
Switch to the user (why would you do that?)
Start the Jupyter server

Test the notebook
Chances are that you don’t have everything installed
Use inline commands in the Jupyter file until you’re able to run it
Export your python libraries into a file called requirements.txt
Include the requirements
Copy the requirements.txt document into your Dockerfile
Install the python libraries that are included in the requirements.txt

Submit
Push results to github
Submit the link to the repo on Camino
