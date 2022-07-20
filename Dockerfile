FROM python:3
WORKDIR autobahn_info
ADD autobahn_info/
RUN pip install mysql-connector-python requests
CMD ["python", "./autobahn_job_docker.py"]