FROM python:3.9
MAINTAINER Shubhendra Kushwaha
ADD . /usr/src/app
WORKDIR /usr/src/app
COPY requirements.txt ./
RUN pip install -r requirements.txt
CMD exec gunicorn quizzes.wsgi:application --bind 0.0.0.0:$PORT