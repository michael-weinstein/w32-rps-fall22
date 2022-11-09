FROM python:3.11.0 #the default python docker image run on Debian linux

RUN apt update

COPY requirements.txt /opt/

RUN pip3 install -r /opt/requirements.txt

RUN mkdir /opt/rps

COPY main.py /opt/rps

COPY rpnsSupport /opt/rps/rpsSupport

CMD ["python3", "/opt/rps/main.py"]