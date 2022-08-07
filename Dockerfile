FROM python:3

WORKDIR /usr/src/app

COPY . .

RUN pip install -r requirements.txt

EXPOSE 8888

CMD ["python", "./app.py"]