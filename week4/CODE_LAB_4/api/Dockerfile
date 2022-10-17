FROM python:3.8-slim-buster

WORKDIR /python-docker

COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

#creating volume and making it as the work directory
VOLUME /app
WORKDIR /app


EXPOSE ${API_PORT}

CMD ["python3", "api.py" ]
