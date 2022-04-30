FROM python:3.9.2

# RUN mkdir /projectsInstaAPI

# WORKDIR /projectsInstaAPI

# COPY . /projectsInstaAPI/

# RUN pip install -r requirements.txt

# ENTRYPOINT ["uvicorn", "main:app", "--reload"]

WORKDIR /code

COPY ./requirements.txt /code/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

COPY ./app /code/app

ENTRYPOINT ["uvicorn", "app.main:app", "--log-config", "./log.ini" , "--host", "0.0.0.0", "--port", "8000"]


