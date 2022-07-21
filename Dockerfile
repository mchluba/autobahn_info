FROM python:3.10.5-slim-bullseye
ADD /autobahnbot /autobahnbot
ADD /docker/autobahn_job_docker.py /autobahn_job_docker.py
RUN pip install mysql-connector-python requests
CMD ["dir"]