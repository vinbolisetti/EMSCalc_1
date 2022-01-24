FROM python:3
ENV PYTHONUNBUFFERED=1

RUN mkdir -p /home/node/app
WORKDIR /home/node/app

COPY requirements.txt /home/node/app
RUN pip install -r requirements.txt
COPY . /home/node/app

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]