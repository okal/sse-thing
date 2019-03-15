FROM python:3.6

WORKDIR /usr/src/app

COPY . /usr/src/app
RUN pip install -r requirements.txt
ENV FLASK_APP=remote.py
EXPOSE 5000
CMD flask run --host=0.0.0.0