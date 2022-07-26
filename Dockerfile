FROM python:3.7.1

COPY requirements.txt /
RUN pip install --upgrade pip && pip install -r requirements.txt
COPY . /app
WORKDIR /app

ENTRYPOINT ["./gunicorn.sh"]