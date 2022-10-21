FROM python
RUN pip install flask
RUN pip3 install psycopg2
RUN pip3 install sqlalchemy

ENV API_PORT=${API_PORT}
VOLUME [ "/app" ]
WORKDIR /app
EXPOSE ${API_PORT}