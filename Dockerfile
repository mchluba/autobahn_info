FROM python:3.10.5-slim-bullseye
COPY . .
RUN pip install mysql-connector-python requests
CMD ["python", "autobahn_job_docker.py"]