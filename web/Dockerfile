FROM python:3.10.7

RUN python -m pip install --upgrade pip

WORKDIR /opt/app
ADD requirements.txt /opt/app/requirements.txt
RUN pip install -r /opt/app/requirements.txt
ADD . /opt/app

COPY . .
