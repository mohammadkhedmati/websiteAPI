FROM python:3.9.2

WORKDIR /webapi

COPY ./requirements.txt /webapi/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /webapi/requirements.txt

COPY ./app /webapi/app

ENTRYPOINT ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8002"]


