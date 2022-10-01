#as of 9/29/22 -latest version
FROM python:3.10.7

USER root

# Installing all the tools and softwares needed for the assignment
RUN pip3 install jupyter
RUN apt-get update
RUN apt-get install wget

# Setting the environment variable as JUPYTER_USER 
ENV JUPYTER_USER our_user
RUN useradd -ms /bin/bash $JUPYTER_USER

# Exposes port 8888 -Docker to get all its information required during the runtime from a this Port.
EXPOSE 8888

# Making a directory 'notebook' for our user 
RUN mkdir /home/$JUPYTER_USER/notebook

#Setting 'notebook' as working directory of our Docker container
WORKDIR /home/$JUPYTER_USER/notebook
 
#Downloading the required files from github
RUN wget https://raw.githubusercontent.com/Shaheenzr/Python/main/Group_by/cleaned_survey.csv
RUN wget https://raw.githubusercontent.com/Shaheenzr/Python/main/Group_by/module%206%20group%20by%20-%20complete.ipynb
#Copying the requirement.txt and running it
COPY requirements.txt ./
#Disabling the Cache and installing everything mentioned in requirement.txt
RUN pip3 install --no-cache-dir -r requirements.txt

USER $JUPYTER_USER
CMD jupyter notebook --ip=0.0.0.0 --port 8888


