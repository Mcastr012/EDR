FROM python:3.7
WORKDIR /app
COPY . /app
COPY requirements.txt /app/tmp/

RUN apt-get -y update && apt-get install -y postgresql-client 
RUN pip install -r /app/tmp/requirements.txt
CMD ["./start.sh", "psql", "python", "app.py"]
