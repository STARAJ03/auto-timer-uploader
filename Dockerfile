FROM python:3.9-slim-bookworm

RUN apt-get update && \
    apt-get install -y --no-install-recommends gcc libffi-dev musl-dev ffmpeg aria2 python3-pip && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

COPY . /app/
WORKDIR /app/
RUN pip3 install --no-cache-dir --upgrade -r requirements.txt

CMD gunicorn app:app & python3 modules/main.py
