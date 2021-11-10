FROM alpine:3.13

RUN apk update
RUN apk add python3 py3-pip gcc g++ python3-dev libc-dev

COPY app/ /app/

COPY requirements.txt .
RUN pip install -r requirements.txt

EXPOSE 8000

CMD ["gunicorn", "--bind", "0.0.0.0:8000", "--chdir", "/app", "short_urls:create_app()"]
