FROM python:3.13-slim

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt
RUN pip install gunicorn

COPY . .
RUN chmod a+x boot.sh

ENV FLASK_APP=app.py

EXPOSE 5000
ENTRYPOINT ["./boot.sh"]
