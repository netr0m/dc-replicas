FROM python:3.9-slim

WORKDIR /app

COPY ./app.py ./
COPY ./requirements.txt ./

RUN pip3 install -r requirements.txt

CMD ["python3", "-m" , "flask", "run", "--host=0.0.0.0"]
