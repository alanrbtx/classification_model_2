ARG PYTHON_VERSION=3.9.6
FROM python:${PYTHON_VERSION} as base

WORKDIR /app

COPY . .

RUN python -m pip install -r requirements.txt

EXPOSE 8000

CMD python3 service/app.py