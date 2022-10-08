FROM python

COPY requirements.txt /tmp/
RUN pip3 install -r /tmp/requirements.txt

#create a volume called app
VOLUME /vol_app

#creating working directory
WORKDIR /app 

EXPOSE 8000
