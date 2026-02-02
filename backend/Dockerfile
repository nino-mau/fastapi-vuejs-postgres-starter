FROM python:3.11

COPY ./requirements.txt /app/

WORKDIR /app

RUN pip install --no-cache-dir --upgrade -r /app/requirements.txt

COPY . /app

CMD ["fastapi", "dev", "main.py", "--host", "0.0.0.0"]
