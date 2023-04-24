FROM python:3.11
WORKDIR /fastapi
COPY . /fastapi
RUN pip install -r requirements.txt
EXPOSE 8000
ENTRYPOINT ["./docker-entrypoint.sh"]